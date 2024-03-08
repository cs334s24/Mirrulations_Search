import React from "react";
import {render, screen, fireEvent} from "@testing-library/react";
import SearchBar from "../components/SearchBar";

test("SearchBar renders correctly", () => {
 render(<SearchBar />);

 expect(screen.getByPlaceholderText("Search...")).toBeInTheDocument();
});

test("SearchBar input changes correctly", () => {
 render(<SearchBar />);
 const inputElement = screen.getByPlaceholderText("Search...");

 fireEvent.change(inputElement, {target: {value: "test"}});
 expect(inputElement.value).toBe("test");
});
