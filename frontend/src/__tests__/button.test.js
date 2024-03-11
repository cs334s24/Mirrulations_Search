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

test("button is rendered", async () => {
 await page.goto("http://localhost:3000");
 await page.waitForSelector("button");
 const button = await page.$("button");
 expect(button).not.toBeNull();
});
