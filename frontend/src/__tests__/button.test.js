/*
* test to check if the button is rendered
*/

import React from 'react';
import { render, screen } from '@testing-library/react';
import SearchBar from '../components/SearchBar';

test('SearchBar renders with a search button', () => {
  render(<SearchBar />);

  const searchButton = screen.getByText('Search');
  expect(searchButton).toBeInTheDocument();
});
