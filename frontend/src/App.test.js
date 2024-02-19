import React from 'react';
import { render, waitFor } from '@testing-library/react';
import App from './App';

test('renders App component', () => {
  render(<App />);
});

test('renders Mirrulations Search', () => {
  const { getByText } = render(<App />);
  const linkElement = getByText(/Mirrulations Search/i);
  expect(linkElement).toBeInTheDocument();
});








