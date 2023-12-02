# Test Driven Development (TDD) Lab Guide
### What is TDD?
Test Driven Development (TDD) is a testing methodology that requires test cases to be written before any actual development of the code begins. This ensures that any code written adheres to and passes the test cases, which in turn produces solid, high-quality code with minimal bugs. TDD promotes frequent feedback as well, through the development of small sections of test cases and code together, which helps by immediately outlining which areas of the code need to be fixed instead of waiting for the entire code to be completed before the testing process begins.
### What is pytest?
Pytest is a commonly used testing framework in Python, and is widely popular due to its comprehensive and user-friendly features. Pytest is very useful for creating simple and efficient tests that are easy to read, and streamlines the testing process through automatic detection of all test files and functions within a given project. Though based on Behavior-Driven Development (BDD) principles, pytest is very flexible and can be applied to other testing methodologies as well, and additionally supports unit, functional and integration testing levels.

This lab will guide you through the process of using pytest to write and execute tests on a Flask-based bookstore web application.

- - -

## Learning Resources
- #### Documentation:
  - [Python Documentation:](https://docs.python.org/3/) The official Python guide.
  - [Pytest Documentation:](https://docs.pytest.org/en/7.1.x/contents.html) Details how to use and run pytest.
- #### Online Tutorials and Courses:
  - [Unit Testing and Test Driven Development in Python:](https://www.linkedin.com/learning-login/share?account=56744281&forceAccount=false&redirect=https%3A%2F%2Fwww.linkedin.com%2Flearning%2Funit-testing-and-test-driven-development-in-python%3Ftrk%3Dshare_ent_url%26shareId%3DFpSOpa0%252FQMOlU%252BPfWmg0AQ%253D%253D) A course from LinkedIn Learning covering unit testing and TDD with Python.
  - [Test-Driven Development (TDD) - Quick Guide:](https://brainhub.eu/library/test-driven-development-tdd) More information on TDD, including the TDD cycle, advantages & disadvantages, and common practices.
- #### Community Forums and Support:
  - [Stack Overflow:](https://stackoverflow.com/questions/tagged/pytest) Community forum for discussing pytest-related topics.

- - -

## Getting Started with Python, Pytest, and Required Packages
- #### Install Python:
  - Ensure Python (version 3.7 or higher) is installed on your system. If needed, download Python from [python.org](https://www.python.org/downloads/).
  - You can ensure Python is installed and check its version by opening a command line and running:
    - `python --version`
- #### Install Required Packages:
  - Open a command line interface inside of the ‘WebApp’ folder.
  - Run the requirements.txt file to install all required packages:
    - `pip install -r requirements.txt`

## Set Up Your Testing Environment
- #### Setting Up the Python Virtual Environment
  - Navigate to the ‘WebApp’ folder and open a command line. Initiate your Python virtual environment by running:
    - `python -m venv env`
- #### Run the Flask Application:
  - Navigate to your ‘WebApp’ folder in the command line and run:
    - `flask --debug --app main run`
  - If you receive the error ‘flask is not a recognized command’, alternatively run:
    - `python -m flask --debug --app main run`
  - The application should now be running at http://127.0.0.1:5000/ and will respond to changes you make in the code when you refresh the page. The flask application will need to be running for the lab to interact with it.

- - -

## Writing Pytest Tests
- #### Open Your Test File:
  - In your project folder, open the file named `test_main.py`.
  - This file will contain all your pytest tests.

- #### Basic Pytest Test Structure
  - ##### Assertions
    - An assertion is a check that the code makes when running to verify if the provided condition is true. The test passes if the provided condition is validated, and fails if it does not meet the assertion requirements.
    - The syntax of an assertion statement is:
      - `assert expression, message`
    - Where `expression` is the condition to check, and `message` is an optional error message in the event the test fails.
  - ##### Fixtures
    - A fixture is a mechanism that is established as a baseline in order to set up the testing environment or required data. In pytest, a fixture is a Python function that provides the necessary test data or other resources to test functions that require them.
    - A fixture in pytest is formatted as:
      - ```
        @pytest.fixture
        def function():
          # Function information goes here
  - ##### Parametrizing
    - Parametrizing allows the test function to run multiple times with different provided sets of data, which eliminates the need to write multiple tests to check for various situations.
    - Parametrizing tests in pytest is formatted as:
    - ```
      @pytest.mark.parametrize("string",[(value1)(value2)])
      def function(string):
        # Function information goes here
    - Where `string` is the name of the argument the function will take, and `value1` and `value2` are a list of tuples, with each representing a different test case and containing a set of values for the argument. There can be multiple arguments and multiple tuples.
  - ##### pytest.raises
    - pytest.raises checks that certain exceptions get raised when appropriate. The test passes if the exception is raised, otherwise the test fails.
  - A basic pytest test structure (included) looks like this:
    - 

- - -

## Test Examples
- #### Test 1 - Adding a New Book
  - This test validates that a new book can be successfully added.
  - 
- #### Test 2 - Error Handling
  - This test validates if an exception is raised when a user attempts to add a new book with empty inputs.
  - 

## Incomplete Test Scenarios
- #### Test 3 (Incomplete) - Getting CSV Data
  - Write a test that verifies that the data from the CSV file can be successfully loaded.
  - Instruction: 
- #### Test 4 (Incomplete) - Writing CSV Data
  - Write a test that verifies that the CSV file can successfully write data.
  - Instruction:

- - -

## Expected Test Results
- #### Test 1
  - In the "Adding a New Book" test, the new book title should be present in the page content after submission.
- #### Test 2
  - For the "Error Handling" test, an exception should be raised when attempting to submit a new book with empty inputs.
- #### Test 3
  - Expected results will depend on the specific implementation but should generally include successful loading of the CSV file data.
- #### Test 4
  - Expected results will depend on the specific implementation but should generally include successful writing of data to the CSV file.

- - -

## Running Tests
- Execute pytest tests with the following command:
  - `pytest test_main.py`
- If pytest is installed correctly, a passing test will issue the following output format:
  - ```
    ======================== test session starts =====================
    …
    collected 1 item
    test_main.py .                                   	[100%]
    ======================== 1 passed in 0.01s =====================

- - -

## Conclusion
- This lab should provide a good insight into the workings of pytest, how to automate testing, and the beneficial impact that something like automated web-testing can provide in a development environment. Through a mix of guided examples and interactive exercises, you will gain practical experience in testing web applications. This hands-on approach is designed to enhance your skills in both pytest and general web testing methodologies such as Test Driven Development.
