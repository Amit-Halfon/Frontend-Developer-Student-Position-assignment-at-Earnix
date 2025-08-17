# README

## Project Overview

This project contains automated UI tests for the ReactJS documentation website using [Playwright](https://playwright.dev/) in Python.  
The tests are organized in the `reactJS_tester` package, with page objects and components for maintainable test code.

## The tests being cheked

test_accessibility - cheks the website is accessible via keyboard.
test_code_editor - edit the code editor in on of the pages of the website and checks the display has changed accordingly.
test_language- checks the spanish button works as expected.
test_layout_and_the_theme- checks for header footer and that the toggle button works as expected.
test_navbar - checks that all the links in the navbar are working as expected.
test_search - checks the search is working as expected (followed the steps in the example given)

## Structure

- `reactJS_tester/pages/` — Page object classes for different documentation pages.
- `reactJS_tester/components/` — UI component abstractions (e.g., header, search modal).
- `reactJS_tester/Tests/` — Test cases using Playwright and the page/component objects.

## Setup

1. **Install dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

2. **Run tests:**
   ```sh
   pytest
   ```

## Notes

- Ensure you have Python 3.12+ installed.
- Set the `PYTHONPATH` to the project root if you encounter import errors:
  ```sh
  set PYTHONPATH=reactJS_tester
  ```
