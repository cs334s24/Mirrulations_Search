## CI/CD Pipeline

Github Actions are utilized in order to create a CI/CD pipeline for development. On the CI, when a pull request is made, 
Github will create a Github Runner to clone our code and test it. After a pull request is merged, we have 2 different
deploy scripts, one for deploying to our Lambda functions in AWS and another to deploy to our EC2 which is hosting 
test334.moraviancs.click

### webapp-testing.yml

This file has 5 steps that it takes. First, the file is set so that it creates 4 different runners to test across
4 different python versions to prevent any version issues. Each runner will then setup Nodejs in the environment as well as
install all node dependencies needed using our package-lock.json file. It then sets up Python, and then installs our
Python packages as well. At this point, it very simple calls `make` which calls the Makefile which is already set up
to test and lint the entire program. The purpose of using the Makefile for this is so that the testing is done
in a standardized way across all systems, including the testing environment. 

### deploy-to-ec2.yml

This file deploys all changes to our test instance with a downtime of 2-3 minutes. It also utilizes secret variables which must be
kept directly on the repository. To find and update them, you must go to the repo, go to the settings, go to Secrets and Variables on
the side panel, and then click Actions. From here, you can see the variables under Repository Secrets section. This script uses `TEST_EC2_PUBLIC_IP`
which is the IPv4 address found in AWS, `USER_NAME` which is `ec2-user`, and `SSH_PRIVATE_KEY` which is our pem file. 
The script copies the pem key into the GitHub runner and gives read access, and then uses SSH to connect to the EC2 instance.
From here, it brings down the docker containers, prunes the images cache to create more space, pulls the changes,
and then builds and puts the docker containers back up. 

### deploy-to-lambda.yml

This file deploys changes to our Lambda functions in AWS for our zip system. There are only 2 basic steps, it installs Node for one,
and then for the second step, it zips up the `lambda_function.py` file, and then uses the aws-cli to push the zip to 
update the function in AWS. It uses 2 Repository Secrets, `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` which can both be found 
in 1Password. 

For more information about how to use actions, seek the [Github Actions Documentation](https://docs.github.com/en/actions/learn-github-actions).