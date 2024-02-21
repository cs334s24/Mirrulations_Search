import React from 'react';
import { render, fireEvent } from '@testing-library/react';
import SearchBar from '../components/SearchBar';

test('SearchBar renders correctly', () => {
  const { getByPlaceholderText } = render(<SearchBar />);
  const inputElement = getByPlaceholderText('Search...');

  expect(inputElement).toBeInTheDocument();
});

test('SearchBar input changes correctly', () => {
    const { getByPlaceholderText } = render(<SearchBar />);
    const inputElement = getByPlaceholderText('Search...');
  
    fireEvent.change(inputElement, { target: { value: 'test' } });
    expect(inputElement.value).toBe('test');
  });