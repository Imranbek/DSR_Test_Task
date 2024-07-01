# Test task for UI test automation

## About

This is a frontend test automation project using Python, Pytest, and Playwright. 
In this project I automated tests for the web application
https://vladimirwork.github.io/web-ui-playground/, verifying user interface elements and their behaviour.

This implementation may seem complex at first, but over time it shows itself as the best approach.
Moreover, this method allows easy scaling of automated tests within a microservices architecture
by extracting the Page Object Model into a separate project library. 
Additionally, the structure of the objects, when copied to another repository, enables writing less code in the future.



## Project structure

- tests/ - tests catalogue.
- pages/ - Page Object Model catalogue.
- utils/ - helpful functions, which are not part of a test scripts.
- conftest.py - configurations and fixtures for test scripts.
- requirements.txt - requirements.
- checklist.md - document with checklists and names of test-scripts.

## Installation

1. Make sure you are using Python 3.7 or newer version on your machine.
2. Clone this repo:
    ```sh
    git clone https://github.com/Imranbek/DSR_Test_Task.git
    cd DSR_Test_Task/UI_tests
    ```
3. Install requirements:
    ```sh
    pip install -r requirements.txt
    ```

4. Install Playwright
    ```sh
    playwright install
    ```

## Run the tests

To run tests use this command from main project directory (DSR_Test_Task)

```sh
pytest /UI_tests
```