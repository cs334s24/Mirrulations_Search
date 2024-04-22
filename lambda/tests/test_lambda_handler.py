import unittest
from unittest.mock import patch
import boto3
import json
from botocore.stub import Stubber
from botocore.exceptions import ParamValidationError
from lambda_handler import lambda_handler

class TestLambdaFunction(unittest.TestCase):

    def setUp(self):
        self.secretsmanager = boto3.client('secretsmanager')
        self.stubber = Stubber(self.secretsmanager)

    def tearDown(self):
        self.stubber.deactivate()

    def test_successful_email_sending(self):
        # Mocking Secrets Manager response
        secret_name = "TestingZipSystemLambda"
        secret_data = {"sender_email": "sender@example.com", "sender_password": "password123"}

        # Activate the Stubber
        self.stubber.activate()

        # Define the expected params and response
        expected_params = {'SecretId': secret_name}
        response = {'SecretString': json.dumps(secret_data)}

        # Add the stubbed response to the Stubber
        self.stubber.add_response('get_secret_value', response, expected_params)

        # Input event
        event = {
            "to_email": "recipient@example.com",
            "docket_id": "12345"
        }

        # Call Lambda function
        with self.stubber:
            result = lambda_handler(event, None)

        # Assert the result
        self.assertEqual(result, "Email sent successfully!")

    @patch('smtplib.SMTP')
    def test_missing_to_email(self, mock_smtp):
        # Input event with missing 'to_email'
        event = {
            "docket_id": "12345"
        }

        # Call Lambda function
        result = lambda_handler(event, None)

        # Assert the result
        self.assertIn("Failed to send email:", result)
        mock_smtp.assert_not_called()  # Ensure SMTP server was not called

    @patch('smtplib.SMTP')
    def test_missing_docket_id(self, mock_smtp):
        # Input event with missing 'docket_id'
        event = {
            "to_email": "recipient@example.com"
        }

        # Call Lambda function
        result = lambda_handler(event, None)

        # Assert the result
        self.assertIn("Failed to send email:", result)
        mock_smtp.assert_not_called()  # Ensure SMTP server was not called

    @patch('boto3.client')
    def test_missing_secret(self, mock_secretsmanager):
        # Mock Secrets Manager response for missing secret
        mock_secretsmanager.return_value.get_secret_value.return_value = {}

        # Input event
        event = {
            "to_email": "recipient@example.com",
            "docket_id": "12345"
        }

        # Call Lambda function
        result = lambda_handler(event, None)

        # Assertions
        self.assertIn("Failed to send email:", result)

    @patch('boto3.client')
    def test_invalid_secret_format(self, mock_secretsmanager):
        # Mock Secrets Manager response with invalid JSON format
        mock_secretsmanager.return_value.get_secret_value.return_value = {'SecretString': '{"invalid_json"}'}

        # Input event
        event = {
            "to_email": "recipient@example.com",
            "docket_id": "12345"
        }

        # Call Lambda function
        result = lambda_handler(event, None)

        # Assertions
        self.assertIn("Failed to send email:", result)


if __name__ == '__main__':
    unittest.main()
