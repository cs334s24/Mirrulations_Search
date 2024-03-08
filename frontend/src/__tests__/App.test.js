import React from "react";
import {render, screen} from "@testing-library/react";
import App from "../App";

test("renders App component", () => {
 render(<App />);
});

test("renders Mirrulations Search", () => {
 render(<App />);
 expect(screen.getByText(/Mirrulations Search/i)).toBeInTheDocument();
});
