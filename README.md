# CSC256 Team 8 Test Labs ReadMe
    
# Table of content 
- [Introduction](#global-introduction)
- [Objectives](#global-objectives)
- [Project Team](#project-team)
  
- [Selenium Lab](#selenium-title)
  - [Getting Python, Selenium, and Required Packages](#selenium-setup)
  - [Set Up Your Testing Environment](#selenium-testing-environment)
  - [Learning Resources](#selenium-resources)
  - [Writing Selenium Tests](#selenium-writing-tests)
  - [Test Scenarios](#selenium-examples)
  - [Running the Tests](#selenium-running-tests)
  - [Conclusion](#selenium-conclusion)
    
- [BDD Lab](#bdd-title)
  - [Getting Python, Behave and Required Packages](#bdd-setup)  
  - [Set Up Your Testing Environment](#bdd-environment)  
  - [Learning Resources](#bdd-resources)  
  - [Writing Behave Tests](#bdd-writing-tests)  
  - [Test Scenarios](#bdd-examples)
  - [Running the Tests](#bdd-running-tests)  
  - [BDD Conclusion](#bdd-conclusion)  
    
- [API Test LAB](#api-title)
  - [API Documentation](#api-documentation)
  - [Endpoints](#api-endpoints)
  - [Postman Installation and Lab Guide](#api-installation)
  - [Test Scenarios](#api-test-scenarios)

- [Test Driven Development (TDD)](#tdd-title)
  - [What is TDD?](#tdd-what-is)
  - [Getting Python, Pytest, and Required Packages](#tdd-setup)  
  - [Set Up Your Testing Environment](#tdd-environment)  
  - [Learning Resources](#tdd-resources)  
  - [Writing Pytest TDD Tests](#tdd-writing-tests)  
  - [Test Scenarios](#tdd-examples)  
  - [Expected Test Results](#tdd-results)
  - [Running the Tests](#tdd-running-tests)
  - [TDD Conclusion](#tdd-conclusion)
    
- [Playwrite Lab](#playwright-title)
  - [Getting Started with Playwright](#playwright-getting-started)
  - [Learning Resources](#playwright-resources)
  - [Writing Playwright Tests](#playwright-writing-tests)
  - [Test Scenarios](#playwright-test-examples)
  - [Expected Test Results](#playwright-results)
  - [Running the Tests](#playwright-running)
  - [Conclusion](#playwright-conclusion) 

<h1 id='global-introduction'>Introduction</h1>

<h2 id='global-objectives'>Objectives</h2>

-	Ensure the system meets the functional requirements as detailed in the SRS.
-	Validate the system’s non-functional requirements.
-	Identify and rectify defects prior to release.
-	Ensure the application accurately handles data and operations.
-	Confirm error handling and validation mechanisms.
-	Verify integration between different modules.
-	Ensure usability and efficiency of the command-line interface.

<h2 id='project-team'>Project Team</h2>

    1. Logan Bennett - Code Developer
    2. Samson Truelove - Code Developer
    3. Aiden Morris - Code Developer
    4. Ava VanDuinen - Tester
    5. Sydney Southerland - Tester
    6. Juan Gomez - Tester
    7. Abdul Caesar - Document Writer
    8. Luke Wainwright - Document Writer
    9. Stephen Rotich - Project Lead/Document Writer

- - -

<h1 id='selenium-title'>1. Selenium Lab</h1>
Selenium is an umbrella of tools and libraries used for web based automated testing. Selenium allows the user to emulate interacting with websites and browsers as if a real user was doing so, letting you test your websites across many different browsers easily and efficiently. This lab will guide you through the process of using Selenium to write and execute tests on a Flask-based bookstore web application.

<h2 id='selenium-setup'>Getting Python, Selenium and Required Packages:</h2> 

#### Install Python:
- Ensure Python (version 3.7 or higher) is installed on your system. You can download it from [Python's Official Website](https://www.python.org/downloads/).
- You can ensure Python is installed and check its version by opening a command line and running: `python --version`
#### Install Required Packages:
- Open a command line interface inside of the `WebApp` folder 
- Run the requirements.txt file to install all required packages: `pip install -r requirements.txt`

<h2 id='selenium-testing-environment'>Set Up Your Testing Environment:</h2>

#### Setting Up the Chrome Web Driver
- There are 2 ways to get a working Chrome web driver for this lab. The first and simpler option is to simply install Google Chrome at its default location.
- Alternatively, navigate to Google Chrome Labs to download the latest stable release of Chrome web browser to use as the Chrome Web Driver. To setup the Chrome Web Driver via this method, follow the instructions here depending on your operating system.
#### Setting Up the Python Virtual Environment
- Navigate to the `WebApp` folder and open a command line. Initiate your Python virtual environment by running: `python -m venv env`
#### Run the Flask Application:
- Navigate to your `WebApp` folder in the command line and run: `flask --debug --app main run`
- If you receive the error `flask is not a recognized command`, alternatively run: `python -m flask --debug --app main run`
- The application should now be running at `http://127.0.0.1:5000/` and will respond to changes you make in the code when you refresh the page.
- The flask application will need to be running for the lab to interact with it.
- You can close the flask application using `Ctrl + C` in your command line.
  
<h2 id='selenium-resources'>Learning Resources:</h2>

Official Selenium Documentation:
- [Selenium Documentation](https://www.selenium.dev/documentation/): The official docs for Selenium and how to use it.
  
Community Forums and Support:
- [Selenium Public Support Group](https://groups.google.com/g/selenium-users?pli=1): A public Google group for Selenium users to seek help from one another
- [Stack Overflow](https://stackoverflow.com/questions/tagged/selenium-webdriver): Community Q&A on Selenium-related topics.

<h2 id='selenium-writing-tests'>Writing Selenium Tests</h2>

#### Open Your Test File:
- In your project folder, open the file named selenium_test_suite.py
- This file will contain all your Selenium tests.
#### Basic Selenium Test Structure:
- A basic Selenium test structure (included) looks like this:
```
# Import driver
from selenium import webdriver
# Start web driver for Chrome
driver = webdriver.Chrome()
# Navigate to the Flask web application's URL.
driver.get("http://127.0.0.1:5000/")

# Define the test function
def test_loading_webpage():
    # Test to ensure the main page loads correctly.
    print("Starting test: test_loading_webpage")
    try:
		# Assert result
        assert "County Bookstore" in driver.title
        print("Passed: test_loading_webpage")
    except AssertionError:
        print("Failed: test_loading_webpage. Expected 'County Bookstore' in page title.")

# Call test function
test_loading_webpage()
# Close the driver when done
driver.close()
```

<h2 id='selenium-examples'>Test Examples</h2>

#### Test 1 – Validate that the new book “Pages” and “Release Year” fields only accept integers:
This test enters a single letter into the “Pages” and “Release Year” options in the new book field and asserts that it failed to enter them.
```
print("Starting test: test_001_nonint_input")
    	try:

        # Show the new book box
        new_book_button = driver.find_element(By.ID, "newBookToggle")
        new_book_button.click()
        # Wait half a second for the box to appear
        driver.implicitly_wait(0.5)
        # Grab the inputs
        pages_input = driver.find_element(By.ID, "pages")
        release_year_input = driver.find_element(By.ID, "releaseYear")
        # Attempt to put a character in them
        pages_input.send_keys("a")
        release_year_input.send_keys("a")
        # Get the current contents of the input
        pages_input_content = driver.find_element(By.ID, "pages").get_attribute("value")
        pages_inrelease_year_input_content = driver.find_element(By.ID, "releaseYear").get_attribute("value")
        # Assert results
        assert pages_input_content == ""
        assert pages_inrelease_year_input_content == ""
        print("Passed: test_001_nonint_input\n")
    except Exception as e:
        print("Failed: test_001_nonint_input. Error: " + str(e) + '\n')
```
#### Test 2 - Adding a New Book:
This test simulates adding a new book by interacting with the web elements.
	
 	# Send inputs
        driver.find_element(By.ID, "newTitle").send_keys("Fake Title")
        driver.find_element(By.ID, "newAuthor").send_keys("Fake Author")
        driver.find_element(By.ID, "newGenres").send_keys("Fiction")
        driver.find_element(By.ID, "pages").send_keys("100")
        driver.find_element(By.ID, "releaseYear").send_keys("2023")

        # Submit new book
        driver.find_element(By.ID, "submitNewBook").click()

        # Check to see if the book title is present in the page
        # 2 seconds of wait added to allow for the page to refresh
        driver.implicitly_wait(2)
        assert new_title in driver.page_source

<h2 id='selenium-exercises'>Incomplete Test Scenarios (Exercises YOU need to Complete):</h2>

#### Test 3 (Incomplete) - Search Functionality:
- Write a test that searches for a book and verifies the search results.
- Instruction: Fill in the search input, click the search button, and assert that the expected result is present in the page content.
#### Test 4 (Incomplete) - Error Handling:
- Write a test for handling an error, like submitting an empty form.
- Instruction: Try submitting the 'Add Book' form without filling in any details and assert that the appropriate error message is displayed.

<h2 id='selenium-results'>Expected Results from Testing</h2>

- Test 1: For the “Non-int input” test, the page and release year boxes in the ‘New Book’ section won’t be able to accept a non-numeric input.
- Test 2: In the "Adding a New Book" test, the new book title should be present in the page content after submission.
- Test 3: Expected results will depend on the specific implementation but should generally include successful execution of the search.
- Test 4:  Expected results will depend on the specific implementation but should either assert the present of a displayed error or other handling.
  
<h2 id='selenium-running-tests'>Running Selenium Tests</h2>

Execute your tests using the command: `python selenium_test_suite.py`
Observe the results to ensure all tests are functioning as expected. Your command line should indicate “Passed: __” or “Failed: __” for each test.

<h2 id='selenium-conclusion'>Conclusion</h2>

This lab should provide a good insight into the workings of Selenium Web Driver, how to automate testing, and the beneficial impact that something like automated web-testing can provide in a development environment. Through working with Selenium to implement these tests, we can assure that functionality does not break in the future when further additions are made to our program by simply running the tests again.

- - - 

<h1 id='bdd-title'>2. BDD Lab: Testing a Bookstore Web Application</h2>

BDD, meaning “Behavior-driven development” is a software development style that encourages collaboration between the dev team, QA, and non-technical partners such as investors or business participants. BDD is presented in natural language styles such as the Gherkin language which presents behavior in a given-when-then format. This lab will guide you through using the Python  based Behave Framework to utilize BDD methods in testing a book store web application.

<h2 id='bdd-setup'>Getting Python, Behave and Required Packages:</h2>

#### Install Python:
-	Ensure Python (version 3.7 or higher) is installed on your system. You can download it from [Python's Official Website](https://www.python.org/downloads/).
-	You can ensure Python is installed and check its version by opening a command line and running: `python --version`
#### Install Required Packages:
-	Open a command line interface inside of the ‘WebApp’ folder 
-	Run the `requirements.txt` file to install all required packages: `pip install -r requirements.txt`

<h2 id='bdd-environment'>Setup Your Testing Environment</h2>

#### Setting Up the Python Virtual Environment
- Navigate to the `WebApp` folder and open a command line. Initiate your Python virtual environment by running: `python -m venv env`
  
#### Run the Flask Application:
- Navigate to your ‘WebApp’ folder in the command line and run: `flask --debug --app main run`
- If you receive the error ‘flask is not a recognized command’, alternatively run: `python -m flask --debug --app main run`
- The application should now be running at `http://127.0.0.1:5000/` and will respond to changes you make in the code when you refresh the page. The flask application will need to be running for the lab to interact with it.
- Close the flask application with `Ctrl + C` in the command line

<h2 id='bdd-resources'>Learning Resources</h2>

Official Behave Documentation:
- [Behave Documentation](https://behave.readthedocs.io/en/latest/): The official docs for Behave and how to use it.
- [Official Behave GitHub Repo](https://github.com/behave/behave): The official Behave GitHub repository
  
Community Forums and Support:
- [Stack Overflow](https://stackoverflow.com/questions/tagged/python-behave): Community Q&A on Behave-related topics.

<h2 id='bdd-writing-tests'>Writing Behave Tests</h2>

#### Understanding the file structure and Behave:
-	In your WebApp folder, you will have a sub-folder called Features, this is where all Gherkin-based tests are stored for Behave in files noted as .feature files.
-	Inside the Features folder is another sub-folder called Steps, this is where the actual tests’ functionality goes in the form of Python scripts.
-	While multiple features can be put into a single file, they can also be split into multiple. 
-	Similarly, steps can be combined into single files or split into multiple such as steps focusing on a specific action that will be reused often. (Ex: A step that opens the website to be tested).
-	For this lab, each scenario in the feature file will be broken down into its own step file.
-	Behave is a BDD Python Testing Framework. This means for web-interaction, a framework such as Selenium Web-Driver or Splinter will need to be utilized. For this lab, Selenium Web-Driver will be used for all step-functionality.

#### Basic Behave Test Structure:
-	A base Behave feature written in Gherkin given-when-then looks like this:

```
Feature: showing off behave
     Scenario: Run a simple test
        Given we have behave installed
        When we implement a test
        Then behave will test it for us!
```

- This feature’s corresponding steps would be written as:	

```
from behave import *

@given('we have behave installed')
def step_impl(context):
    pass

@when('we implement a test')
def step_impl(context):
    assert True is not False

@then('behave will test it for us!')
def step_impl(context):
    assert context.failed is False
```

<h2 id='bdd-examples'>Test Examples</h2>

#### TC001: – Validate that only partial input for a new book shows an error

This test enters only a title in the new book box and upon trying to submit, will be met with an error instead.
```
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

@given('We have the bookstore and the new book box open')
def step_impl(context):
    # Get the bookstore page
    driver.get("http://127.0.0.1:5000/")
    # Show the new book box
    new_book_button = driver.find_element(By.ID, "newBookToggle")
    # Click the Add New Book button to display the book section if not displayed already
    if("none" in driver.find_element(By.ID, "addNewBook").get_attribute("style")):
        new_book_button.click()
    # Wait half a second for the box to appear
    driver.implicitly_wait(0.5)
    # Ensure the box is open
    assert "block" in driver.find_element(By.ID, "addNewBook").get_attribute("style")

@when('We type a title in for a new book and nothing else')
def step_impl(context):
    # Enter value into the title block
    driver.find_element(By.ID, "newTitle").send_keys("This is a test")
    # Nothing to assert, pass automatically
    pass

@then('It will not make a book and instead make an error')
def step_impl(context):
    # Click the submit button
    driver.find_element(By.ID, "submitNewBook").click()
    # Wait half a second for the box to appear
    driver.implicitly_wait(0.5)
    # Assert the error box came up
    assert "block" in driver.find_element(By.ID, "errorBox").get_attribute("style")
```

#### TC002: – Sorting by the page column shows the smallest page count book

This test sorts the page column, leaving the results from smallest to largest then ensures the smallest page count is the one at the top of the list.
```
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

@given('We have the bookstore open')
def step_impl(context):
    # Get the bookstore page
    driver.get("http://127.0.0.1:5000/")
    # Wait for the page to load
    driver.implicitly_wait(0.5)
    # Assert the page title to ensure its the correct page
    assert driver.title == "County Bookstore"
    

@when('We click the page count header')
def step_impl(context):
    # Click the page header one time to sort from smallest -> largest
    driver.find_element(By.ID, "pageHeader").click()
    # Nothing to assert, pass
    pass

@then('The book with the smallest page count will be at the top of the list')
def step_impl(context):
    # Establish smallest page count
    smallest_pages = None
    # Get the body of the table
    table_body = driver.find_element(By.ID, "tbody")
    rows = table_body.find_elements(By.TAG_NAME, "tr")
    # Loop through all rows
    for row in rows:
        # Find the third column in each row and cast its contents as an int
        col = int(row.find_elements(By.TAG_NAME, "td")[3].text)
        # If the smallest page variable is set to None or greater than the col value, replace it
        if smallest_pages == None or smallest_pages > col:
            smallest_pages = col

    # Get the page count of the first row 
    first_row_page = int(rows[0].find_elements(By.TAG_NAME, "td")[3].text)

    # Make final assert
    assert smallest_pages == first_row_page
```

##	Incomplete Test Scenarios (Exercises YOU need to Complete): 
#### TC003: (Incomplete) – Ensure the search bar only filters by titles:
```
	Write a test that uses the search bar to search for something other than a title of a book and get no results.
	Instruction: Fill in the search input with a value other than something present in a title of a book and ensure there are no results.
```
#### TC004: (Incomplete) – Add a new book:
```
	Write a test that adds a new book and find it in the list after submission.
	Instruction: Fill in the new book contents, submit the form, and check to see if the new book is present.
```
<h2 id='bdd-results'>Expected Results from Testing</h2>

- Test 1: After partial input of a book, it will display an error instead of submitting the new book.
- Test 2: The smallest page book will be the top row of the list.
- Test 3: After searching for a value not in a title, there will be no results in the books list.
- Test 4: The newly added book will be present in the list.

<h2 id='bdd-running-tests'>Running the Tests</h2>

- Execute your tests using the command: `behave`
- It will automatically run all feature files in the Features sub-folder. Observe the results to ensure all tests are functioning as expected. Your command line should indicate:
```
1 feature passed, 0 failed, 0 skipped
4 scenarios passed, 0 failed, 0 skipped
XX steps passed, 0 failed, 0 skipped, 0 undefined
```

<h2 id='bdd-conclusion'>Conclusion</h2>

This lab should provide a good insight into the workings of the Behave BDD testing framework and how to implement it into a workflow. Behave allows business partners, QA testers, and development teams all get involved in the testing process to allow everyone to better understand how the program should function.


- - -

    
<h1 id='api-title'>3. API Test Lab</h1>

<h2 id='api-documentation'>API Documentation</h2>

Welcome to the Wake County Bookstore. This API allows developers to access and interact with our online bookstore's features, including browsing books, managing a shopping cart, placing orders, and viewing order history.

#### Base URL

The base URL for all API endpoints is: `http://127.0.0.1:3000`

#### Authentication

Authentication is required to access specific API endpoints. We use API keys for authentication. To obtain an API key, please get in touch with our support team.

#### Request Headers 

 `Authorization: Bearer YOUR_API_KEY  supplied securely via sftp or other encrypted methodologies`  

<h2 id='api-endpoints'>Endpoints</h2>

Get the yaml representation using the openAPI 3.0 specification format here: ***[wc-booksore.yaml](./wc-booksore.yaml)***
1. #### List Books

 **Endpoint:** `/api/books` \
 **HTTP Method:** GET \
 **Description:** Get a list of books available in the bookstore. \
 **Parameters:** 
  - `search` : A search query to filter books by title, author, or genre. \
  - `category`: Filter books by category or genre. \
 **Response:** 
    - **Status Code:** 200 OK 
    - **Body:** JSON array containing book objects. Example response: 

```json
  [
    {
        "ISBN": "979-2591-85790-10-5",
        "authors": "Maria Garcia",
        "categories": "History",
        "num_pages": "962",
        "published_year": "2009",
        "subtitle": "The Mysteries",
        "title": "The Wind River"
    },
    {
        "ISBN": "971-4451-85690-10-5",
        "authors": "Charles Osborne;Agatha Christie",
        "categories": "Detective and mystery stories",
        "num_pages": "241",
        "published_year": "2000",
        "subtitle": "A Novel",
        "title": "Spider's Web"
    },
  ]
```

- **Status Code:** 500 OK

2. #### List Books by attribute e.g. published_year

 **Endpoint:** `/api/books?attribute=published_year&value=2007` \
 **HTTP Method:** GET \
 **Description:** Get a list of books available in the bookstore. \
 **Parameters:**

- `search` : A search query to filter books by title, author, or genre. \
- `category`: Filter books by category or genre. \
 **Response:**
  - **Status Code:** 200 OK
  - **Body:** JSON array containing book objects. Example response:

```json
  [
    {
        "ISBN": "979-2591-85790-10-5",
        "authors": "Maria Garcia",
        "categories": "History",
        "num_pages": "962",
        "published_year": "2009",
        "subtitle": "The Mysteries",
        "title": "The Wind River"
    },
    {
        "ISBN": "971-4451-85690-10-5",
        "authors": "Charles Osborne;Agatha Christie",
        "categories": "Detective and mystery stories",
        "num_pages": "241",
        "published_year": "2000",
        "subtitle": "A Novel",
        "title": "Spider's Web"
    },
  ]
```

- **Status Code:** 500 OK

3. #### Display single Book {by unique id e.g. isbn}

 **Endpoint:** `/api/books/{isbn}` \
 **HTTP Method:** GET \
 **Description:** Get detailed information about a specific book. \
 **Parameters:** \
   `book_id` : The unique identifier of the book. \
 **Response:** 
  - **Status Code:** 200 OK 
  - **Body:** JSON array containing book objects. Example response: 

  ```json
  {
  "id": "1",
  "title": "The Great Gatsby",
  "author": "F. Scott Fitzgerald",
  "price": 10.99,
  "description": "A classic novel...",
  "category": "Fiction"
  }
 ```

4. #### Add Book to Cart 

 **Endpoint:** `/api/{{userID}}/cart/add`  \
 **HTTP Method:** POST \
 **Description:** Add a book to the user's shopping cart. \
 **Response:** 
  - **Status Code:** 201 Created 
  - **Body:** Confirmation message. 
  - **Body:** JSON object containing book_id and quantity. 
  
```json
  {
  "book_id": "1",
  "quantity": 2
  }

```

5. #### View Cart 
**Endpoint:** `/api/{{userID}}/cart` \
**HTTP Method:** GET \
**Description:** Get the user's shopping cart contents. \
**Response:** 
  - **Status Code:** 200 OK 
  - **Body:** JSON array of cart items. 

  ```json
    [
        {
          "ISBN": "979-2591-85790-10-5",
          "authors": "Maria Garcia",
          "categories": "History",
          "num_pages": "962",
          "published_year": "2009",
          "subtitle": "The Mysteries",
          "title": "The Wind River"
        }
    ]
  ```

6. #### Remove Book from Cart 
**Endpoint:** /cart/remove/{book_id} \
**HTTP Method:** DELETE \
**Description:** Remove a book from the user's shopping cart. \
**Parameters:** 
`book_id`: The unique identifier of the book. \
**Response:** 
  - **Status Code:** 204 No Content 
  

7. #### Get Categories

**Endpoint:** /categories \
**HTTP Method:** GET \
**Description:** Get a list of available book categories or genres. \
**Response:**

- **Status Code:** 200 OK
- **Body:** JSON array of category objects. Example response:

```json
[
  "Fiction",
  "Non-Fiction",
  "Mystery",
  "Science Fiction"
]
```



<h2 id='api-installation'>Postman Installation and Lab Guide</h2>

Postman is a popular tool for API development and testing. It allows developers and Testers to build, test, and document APIs easily. This guide will help  with the installation process and provide  an overview of how to use Postman to test our wake county onlinebookstore

#### Step 1: Downloading Postman

1. Visit the Postman website to download the application. [Postman Downloads](https://www.postman.com/downloads/).
2. Choose the version suitable for your operating system (Windows, MacOS, Linux).
3. Click on the download link to start the process.

#### Step 2: Installing Postman

- After downloading, open the installer file.
- Follow the on-screen instructions to complete the installation.

## Getting Started With Postman

#### Creating an Account

- Upon opening Postman for the first time, you will be prompted to create an account. This can be done using an email address, Google account, or other sign-in methods.
- Creating an account allows you to sync your collections across devices and access more features.

#### Postman Interface

- Familiarize yourself with the Postman interface. Key areas include:
  - **Request Tab**: Where you create new requests.
  - **Response Section**: View responses to your requests.
  - **Collections**: Organize your requests and tests.

#### Making Your First API Request

1. Click on the `New` button and select `Request`.
2. Enter the details for your request:
   - **URL**: Enter the API endpoint you wish to test.
   - **Method**: Select the HTTP method (GET, POST, PUT, DELETE, etc.).
   - **Headers/Body**: Add as needed depending on your API requirements.
3. Click `Send` to execute the request.
4. The response will appear in the section below.
5. 
   ![Alt text](./Assets/send_request.png)

#### Saving Requests

- Save your requests in collections for easy access and organization.
- Click on the `Save` button after setting up your request and specify the collection to save it in.

#### Using Collections and Environments

- ***grab the collection and Environment files in the github repo inside API test lab folder and import it to your local installed postman***
  
- **Collections**: Group related requests for easier management and execution.

- **Environments**: Use environments to manage sets of variables for different setups (like development, testing, production).
- 
- ![Alt text](./Assets/collection.png)

#### Writing  Tests

- Postman allows us to write tests in JavaScript in the `Tests` tab.
- These tests can validate various aspects of the response, such as status codes and response bodies.

![Test](./Assets/imagex.png)
#### Running Collections

- Use the Collection Runner to run a series of requests in a collection, which is useful for automated testing.

#### Conclusion

This guide provides steps to get started with Postman. For more advanced features and detailed documentation, visit the [Postman Learning Center](https://learning.postman.com/).

<h2 id='api-test-scenarios'>Test Scenarios</h2>

## TC001 - Testing endpoint: `Endpoint: /api/books`

1. Send a request with valid credentials 
   -  we expect  200 OK response.
2. Send a request with invalid or no API key using this endpoint:
   - expect a 401 Unauthorized .
3. Send a request with a malformed URL for example <http://127.0.0.1:3001> in place of <http://127.0.0.1:3000> (changed  port number)
   - expect a 404 Not Found or similar error response
4. Send a request to the endpoint and check the json response
    - is it a valid response but with an empty `JSON` response?
    - Does the Json Response contain data?

#### Postman Tests for TC001
```
pm.test("TC001: List Books - Status code is 200", function () {
    pm.response.to.have.status(200);
});
pm.test("TC001: Edge Case - Invalid API Key", function () {
    var unauthorizedStatus = pm.response.code === 401 || pm.response.code === 403;
    pm.expect(unauthorizedStatus).to.be.true;
});
pm.test("TC001: Edge Case - Malformed URL", function () {
    pm.response.to.have.status(404);
});

pm.test("TC001: List Books - Response is a JSON array", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData).to.be.an('array');
});
pm.test("TC001: Edge Case - Handle Empty Array", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData.length).to.be.at.least(0);
});


```

## TC002: Testing Endpoint supplied with attribute e.g published_year :  `/api/books?attribute=published_year&value=2007`

  1. Send a request with specific query parameters e.g.` ?attribute=published_year&value=2007`
    - we expect  200 OK response.
  
  2. Use non-existent attribute values (e.g., a future year) and expect a proper handling,
   - Expectation: empty array

  3. Verify the API's response when the attribute filter matches no books
   - Expectation: empty array
  
#### Postman Tests for TC002

```
pm.test("TC002: List Books by Attribute - Status code is 200", function () {
    pm.response.to.have.status(200);
});

pm.test("TC002: Edge Case - Non-existent Attribute Values", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData).to.be.an('array').that.is.empty;
});

pm.test("TC002: Edge Case - Special Characters in Query", function () {
    pm.response.to.have.status(400); // Assuming 400 for bad request
});
pm.test("TC002: List Books by Attribute - Response is a JSON array", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData).to.be.an('array');
});

```

## TC003: Test Endpoint to Display single Book :  `/api/books/{isbn}`

 1. send a GET request for a single book:
   -  Confirm a 200 OK status for valid ISBN
  2. Use an invalid or non-existent ISBN and expect a 404 Error
  3. Test with a malformed ISBN (e.g., incorrect format) and check the response
  4. end a request to the endpoint and check the json response
   
#### Postman Tests for TC003

```
pm.test("TC003: Display Single Book - Status code is 200", function () {
    pm.response.to.have.status(200);
});
pm.test("TC003: Invalid ISBN", function () {
    pm.response.to.have.status(404);
});
pm.test("TC003: Display Single Book - Response is a JSON object", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData).to.be.an('object');
});

```

## TC004: Test Endpoint Add Book to Cart' Endpoint :  `/api/{{userID}}/cart/add`

1. check for a 201 Created status after adding a book
    - Expected Results: 201 status code
2. Confirm the presence of ISBN ,authors,categories,num_pages,published_year,subtitle,title in the response.
3. Try adding a book with invalid or extreme quantities

#### Postman Tests for TC004
```
pm.test("TC004: Add Book to Cart - Status code is 201", function () {
    pm.response.to.have.status(201);
});
pm.test("TC004: Add Non-existent Book", function () {
    pm.response.to.have.status(404);
});

pm.test("TC008: Add Book to Cart - Contains ISBN ,authors,categories,num_pages,published_year,subtitle,title", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData).to.have.property('ISBN');
    pm.expect(jsonData).to.have.property('authors');
    pm.expect(jsonData).to.have.property('categories')
    pm.expect(jsonData).to.have.property('num_pages')
    pm.expect(jsonData).to.have.property('published_year')
    pm.expect(jsonData).to.have.property('subtitle')
    pm.expect(jsonData).to.have.property('title')
});

```

- - -

<h1 id='tdd-title'>4. Test Driven Development (TDD) Lab Guide</h1>

<h2 id='tdd-what-is'>What is TTD?</h2>

Test Driven Development (TDD) is a testing methodology that requires test cases to be written before any actual development of the code begins. This ensures that any code written adheres to and passes the test cases, which in turn produces solid, high-quality code with minimal bugs. TDD promotes frequent feedback as well, through the development of small sections of test cases and code together, which helps by immediately outlining which areas of the code need to be fixed instead of waiting for the entire code to be completed before the testing process begins.

TDD development is broken up into three categories, each which follows one main rule:
- **Red Phase:** Write a failing unit test for the functionality to be implemented.
- **Green Phase:** Write just enough production code to make the failing test pass.
- **Refactor Phase:** Improve upon the code written in the green phase to reduce redundancy.

### What is pytest?
Pytest is a commonly used testing framework in Python, and is widely popular due to its comprehensive and user-friendly features. Pytest is very useful for creating simple and efficient tests that are easy to read, and streamlines the testing process through automatic detection of all test files and functions within a given project. Though based on Behavior-Driven Development (BDD) principles, pytest is very flexible and can be applied to other testing methodologies as well, and additionally supports unit, functional and integration testing levels.

This lab will guide you through the process of using pytest to write and execute tests on a Flask-based bookstore web application.


<h2 id='tdd-setup'>Getting Started with Python, Pytest, and Required Packages</h2>

- #### Install Python:
  - Ensure Python (version 3.7 or higher) is installed on your system. If needed, download Python from [python.org](https://www.python.org/downloads/).
  - You can ensure Python is installed and check its version by opening a command line and running: `python --version`
    
<h2 id='tdd-environment'>Setting Up Your Testing Environment</h2>

- #### Setting Up the Python Virtual Environment
  - Navigate to the `WebApp` folder and open a command line. Initiate your Python virtual environment by running: `python -m venv env`
- #### Activate Python Virtual Environment
  - Activate the virtual environment:
      - On Windows: `env\Scripts\activate`
      - On Unix or MacOS: `source venv/bin/activate` 
- #### Install Required Packages:
  - Open a command line interface inside of the ‘WebApp’ folder.
  - Run the requirements.txt file to install all required packages:
    - `pip install -r requirements.txt`
- #### Run the Flask Application:
  - Navigate to your ‘WebApp’ folder in the command line and run:
    - `flask --debug --app main run`
  - If you receive the error ‘flask is not a recognized command’, alternatively run:
    - `python -m flask --debug --app main run`
  - The application should now be running at `http://127.0.0.1:5000/` and will respond to changes you make in the code when you refresh the page.
  - The flask application will need to be running for the lab to interact with it.

<h2 id='tdd-resources'>Learning Resources</h2>

- #### Documentation:
  - [Python Documentation:](https://docs.python.org/3/) The official Python guide.
  - [Pytest Documentation:](https://docs.pytest.org/en/7.1.x/contents.html) Details how to use and run pytest.
- #### Online Tutorials and Courses:
  - [Unit Testing and Test Driven Development in Python:](https://www.linkedin.com/learning-login/share?account=56744281&forceAccount=false&redirect=https%3A%2F%2Fwww.linkedin.com%2Flearning%2Funit-testing-and-test-driven-development-in-python%3Ftrk%3Dshare_ent_url%26shareId%3DFpSOpa0%252FQMOlU%252BPfWmg0AQ%253D%253D) A course from LinkedIn Learning covering unit testing and TDD with Python.
  - [Test-Driven Development (TDD) - Quick Guide:](https://brainhub.eu/library/test-driven-development-tdd) More information on TDD, including the TDD cycle, advantages & disadvantages, and common practices.
- #### Community Forums and Support:
  - [Stack Overflow:](https://stackoverflow.com/questions/tagged/pytest) Community forum for discussing pytest-related topics.

<h2 id='tdd-writing-tests'>Writing Pytest Tests</h2>

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
          # Function information goes here```
  - ##### Parametrizing
    - Parametrizing allows the test function to run multiple times with different provided sets of data, which eliminates the need to write multiple tests to check for various situations.
    - Parametrizing tests in pytest is formatted as:
    - ```
      @pytest.mark.parametrize("string",[(value1)(value2)])
      def function(string):
        # Function information goes here```
    - Where `string` is the name of the argument the function will take, and `value1` and `value2` are a list of tuples, with each representing a different test case and containing a set of values for the argument. There can be multiple arguments and multiple tuples.
  - ##### pytest.raises
    - pytest.raises checks that certain exceptions get raised when appropriate. The test passes if the exception is raised, otherwise the test fails.
    - pytest.raises is formatted as:
    - ```
      def function():
        with pytest.raises(Error)
          # Function that will raise an error goes here```

<h2 id='tdd-examples'>Test Examples</h2>

- #### Test 1 - Adding a New Book
  - This test validates that a new book can be successfully added.
  - ```
    @pytest.mark.parametrize("newTitle, newAuthor, newGenre, pages, releaseYear", 
                         [("Fake Title", "Fake Author", "Fiction", "100", "2023")])
    def test_add_new_book(driver, newTitle, newAuthor, newGenre, pages, releaseYear):
        # Test to see if a new book input can be successfully added
        try:
            # Navigate to the page with the form
            driver.get("http://127.0.0.1:5000/")  

          # Click the 'Add New Book' button to reveal the form
          new_book_toggle = driver.find_element(By.ID, "newBookToggle")
          new_book_toggle.click()
  
          # Wait for the form to be visible
          WebDriverWait(driver, 10).until(
             expected_conditions.visibility_of_element_located((By.ID, "newBookForm"))
          )
  
          # Now find and fill out the form
          title_input = driver.find_element(By.NAME, "title")
          author_input = driver.find_element(By.NAME, "author")
          genre_input = driver.find_element(By.NAME, "genres")
          pages_input = driver.find_element(By.NAME, "pages")
          year_input = driver.find_element(By.NAME, "releaseYear")
  
          title_input.send_keys(newTitle)
          author_input.send_keys(newAuthor)
          genre_input.send_keys(newGenre)
          pages_input.send_keys(pages)
          year_input.send_keys(releaseYear)
  
          # Find and click the submit button
          submit_button = driver.find_element(By.ID, "submitNewBook")
          submit_button.click()

          # Check to see if the book title is present in the page
          # 2 seconds of wait added to allow for the page to refresh
          driver.implicitly_wait(2)
          assert newTitle in driver.page_source
    
          print("Test executed successfully.")
  
        except Exception as e:
          # Handle any exceptions that occur during the test
          pytest.fail(f"An error occurred during the test: {e}")
- #### Test 2 - Error Handling
  - This test validates if an exception is raised when a user attempts to add a new book with empty inputs.
  - ```
    @pytest.mark.parametrize("newTitle, newAuthor, newGenre, pages, releaseYear", 
                         [("", "", "", "", "")])
    def test_add_new_book_raises_exception(driver, newTitle, newAuthor, newGenre, pages, releaseYear):
        # Test to see if an invalid new book input correctly reports an error
        try:
            # Navigate to the page with the form
            driver.get("http://127.0.0.1:5000/")  

            # Click the 'Add New Book' button to reveal the form
            new_book_toggle = driver.find_element(By.ID, "newBookToggle")
            new_book_toggle.click()
    
            # Wait for the form to be visible
            WebDriverWait(driver, 10).until(
               expected_conditions.visibility_of_element_located((By.ID, "newBookForm"))
            )
    
            # Now find and fill out the form
            title_input = driver.find_element(By.NAME, "title")
            author_input = driver.find_element(By.NAME, "author")
            genre_input = driver.find_element(By.NAME, "genres")
            pages_input = driver.find_element(By.NAME, "pages")
            year_input = driver.find_element(By.NAME, "releaseYear")
            
            title_input.send_keys(newTitle)
            author_input.send_keys(newAuthor)
            genre_input.send_keys(newGenre)
            pages_input.send_keys(pages)
            year_input.send_keys(releaseYear)
    
            # Find and click the submit button
            submit_button = driver.find_element(By.ID, "submitNewBook")
            submit_button.click()
    
            # Assert error box displays
            assert ("block" in driver.find_element(By.ID, "errorBox").get_attribute("style"))
            print("Test executed successfully.")
    
        except Exception as e:
            # Handle any exceptions that occur during the test
            pytest.fail(f"An error occurred during the test: {e}")

## Incomplete Test Scenarios
- #### Test 3 (Incomplete) - Getting CSV Data
  - Write a test that verifies that the data from the CSV file can be successfully loaded.
  - Instruction: Follow the three phases/rules of TDD when writing the test & include screenshots of each phase.
- #### Test 4 (Incomplete) - Writing CSV Data
  - Write a test that verifies that the CSV file can successfully write data.
  - Instruction: Follow the three phases/rules of TDD when writing the test & include screenshots of each phase.


<h2 id='tdd-results'>Expected Test Results</h2>

- #### Test 1
  - In the "Adding a New Book" test, the new book title should be present in the page content after submission.
- #### Test 2
  - For the "Error Handling" test, an exception should be raised when attempting to submit a new book with empty inputs.
- #### Test 3
  - Expected results will depend on the specific implementation but should generally include successful loading of the CSV file data.
- #### Test 4
  - Expected results will depend on the specific implementation but should generally include successful writing of data to the CSV file.


<h2 id='tdd-running-tests'>Running Tests</h2>

- Execute pytest tests with the following command: `pytest test_main.py`
- If pytest is installed correctly, a passing test will issue something similar to following output format:
  - ```
    ======================== test session starts ===================================================
    …
    collected 4 items

    test_main.py
    DevTools listening on ws://127.0.0.1:60121/devtools/browser/463a3f77-4edf-4925-a642-0d38c646b465
    ....                                   	                                                  [100%]
    ======================== 4 passed in 0.01s =====================================================

<h2 id='tdd-conclusion'>Conclusion</h2>

- This lab should provide a good insight into the workings of pytest, how to automate testing, and the beneficial impact that something like automated web-testing can provide in a development environment. Through a mix of guided examples and interactive exercises, you will gain practical experience in testing web applications. This hands-on approach is designed to enhance your skills in both pytest and general web testing methodologies such as Test Driven Development.


- - - 


<h1 id="playwright-title">5.  Playwright Lab</h1>

Playwright is a powerful framework for automating browsers, allowing developers to simulate user interactions with web applications. It supports multiple browsers, making it ideal for cross-browser testing. Playwright is primarily used for end-to-end testing, which tests the flow of an application from start to finish. It ensures that the integrated components of an application function as expected. This lab will guide you through the process of using Playwright to write and execute tests on a Flask-based bookstore web application.

<h2 id='playwright-getting-started'>Getting Started with Playwright</h2>

#### Install Python:
Ensure Python (version 3.7 or higher) is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

#### Install Playwright
Open a command line interface and install Playwright using pip:
`pip install` playwright
After installation, run the following command to install the necessary browsers:
`playwright install`

#### Set Up Your Testing Environment:
Create a new folder on your computer for this project.
Download the provided main.py (the Flask web application) and the incomplete playwright_test_suite.py file. Place these in this folder.
Run the Flask Application:
Navigate to your project folder in the command line and run:
`python main.py`
The application should now be running  

<h2 id='playwright-resources'>Learning Resources</h2>

- Official Playwright Documentation:
	- [Playwright Docs](https://playwright.dev/docs/intro)Comprehensive guide and reference to Playwright features and API.
- Online Tutorials and Courses:
	- [Automate Testing with Playwright](https://www.udemy.com/course/automated-software-testing-with-playwright/): A course on Udemy covering basics to advanced concepts.
	- [Playwright Tutorial Series on YouTube](https://www.youtube.com/playlist?list=PL4cUxeGkcC9jx2TTZk3IGWKSbtugYdrlu): A series of video tutorials for visual learners.
- Community Forums and Support:
	- [Playwright GitHub](https://github.com/microsoft/playwright): For contributions, issues, and discussions related to Playwright.
	- [Stack Overflow](https://stackoverflow.com/questions/tagged/playwright): Community Q&A on Playwright-related topics.

<h2 id='playwright-writing-tests'>Writing Playwright Tests</h2>

- Open Your Test File
- In your project folder, open the file named playwright_test_suite.py.
  - This file will contain all your Playwright tests.
  
#### Basic Playwright Test Structure
A basic Playwright test structure (included) looks like this:
```
from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Define your tests here

    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
```

<h2 id='playwright-test-examples'>Test Examples</h2>

1. Test 1 - Loading the Webpage and Checking the Title:
   This test navigates to the main page and checks if the title is as expected.
   ```
	page = context.new_page()
	page.goto("http://127.0.0.1:5000/")
	assert "County Bookstore" in page.title(), "Page title does not match"
   ```
2.  Test 2 - Adding a New Book:
This test simulates adding a new book by interacting with the web elements.
   ```
	page.click("text=Add Book")  # Click on the 'Add Book' button
	page.fill("input[name='title']", "New Book Title")  # Fill the title
	page.fill("input[name='author']", "Author Name")  # Fill the author
	page.click("text=Submit")  # Submit the new book
	assert "New Book Title" in page.content()  # Verification logic
   ```

## Incomplete Test Scenarios (Exercises YOU need to Complete):
3. Test 3 (Incomplete) - Search Functionality:
   Write a test that searches for a book and verifies the search results.
   Instruction: Fill in the search input, click the search button, and assert that the expected result is present in the page content.
4. Test 4 (Incomplete) - Error Handling:
    Write a test for handling an error, like submitting an empty form.
      Instruction: Try submitting the 'Add Book' form without filling in any details and assert that the appropriate error message is displayed.

<h2 id='playwright-results'>Expected Results from Testing</h2>

- Test 1: For the "Loading the Webpage" test, the page title should match "County Bookstore".
- Test 2: In the "Adding a New Book" test, the new book title should be present in the page content after submission.
- Test 3: Expected results will depend on the specific implementation but should generally include successful execution of the search.
- Test 4:  Expected results will depend on the specific implementation but should generally include proper error handling.

<h2 id='playwright-running'>Running Playwright Tests</h2>

- Execute your tests using the command: `python playwright_test_suite.py`
- Observe the results to ensure all tests are functioning as expected.

<h2 id='playwright-conclusion'>Conclusion</h2>
This lab provides a comprehensive introduction to automated web testing using Playwright. Through a mix of guided examples and interactive exercises, you will gain practical experience in testing web applications. This hands-on approach is designed to enhance your skills in both Playwright and general web testing methodologies.
   
   
   
