# Test Driven Development (TDD) Lab Guide
### What is TDD?
Test Driven Development (TDD) is a testing methodology that requires test cases to be written before any actual development of the code begins. This ensures that any code written adheres to and passes the test cases, which in turn produces solid, high-quality code with minimal bugs. TDD promotes frequent feedback as well, through the development of small sections of test cases and code together, which helps by immediately outlining which areas of the code need to be fixed instead of waiting for the entire code to be completed before the testing process begins.
### What is pytest?
Pytest is a commonly used testing framework in Python, and is widely popular due to its comprehensive and user-friendly features. Pytest is very useful for creating simple and efficient tests that are easy to read, and streamlines the testing process through automatic detection of all test files and functions within a given project. Though based on Behavior-Driven Development (BDD) principles, pytest is very flexible and can be applied to other testing methodologies as well, and additionally supports unit, functional and integration testing levels.

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

## Getting Started with Pytest
- #### Install Python:
  - Ensure Python (version 3.7 or higher) is installed on your system.
    - If needed, download Python from [python.org](https://www.python.org/downloads/).
- #### Install Pytest:
  - Open a command line interface/terminal and install pytest using pip:
    - `pip install pytest`
  - You can then verify if pytest was successfully installed with the following command:
    - `pytest --version`

## Set Up Your Testing Environment
- Create a new folder on your machine for this project.
- Download the provided `main.py` file and the incomplete `test_suite_pytest.py` file. Place these in the previously created folder.

## Running Tests
- Execute pytest tests with the following command:
  - `pytest test_suite_pytest.py`
- If pytest is installed correctly, a passing test will issue the following output format:
  - ```
    ======================== test session starts =====================
    …
    collected 1 item
    test_suite.py .                                   	[100%]
    ======================== 1 passed in 0.01s =====================

- - -

## Writing Pytest Tests
- #### Open Your Test File
  - 
- #### Basic Pytest Test Structure
  - 

- - -

## Test Examples
- #### Test 1 - Adding a New Book
  - This test validates if a user can successfully add a new book to the CSV file.
- #### Test 2 - Error Handling
  - This test validates if an exception is raised when a user attempts to add a new book with an invalid title.

## Incomplete Test Scenarios
- #### Test 3 - Getting CSV Data
  - This test attempts to successfullly load data from the CSV file.
  - Incomplete/for student to fill out.
- #### Test 4 - Writing CSV Data
  - This test attempts to successfully save data to the CSV file.
  - Incomplete/for student to fill out.

- - -

## Expected Test Results
- #### Test 1
  - 
- #### Test 2
  - 
- #### Test 3
  - 
- #### Test 4
  - 

- - -

## Conclusion
- What the lab taught
