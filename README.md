# CSC256 Team 8 Test Labs ReadMe


    
# Table of content 
- [Introduction](#introduction)
  - [objectives](#Objectives)
  - [Project Team](#Project-Team)
  
- [Selenium Lab](#Selenium-Lab)
    - [Introduction](#selenium-intro)
    - [Requirements](#selenium-Requirements)
    - [Setup & installation](#setup-installation)
    - [Lab ](#Lab) 
    
- [BDD Lab](#BDD-Lab)  
    
- [API Test LAB](#API-est-Lab)  


- [TDD Lab](#TDD-Lab)

- [Playwrite Lab](#Playwrite-Lab)
    - [Playwrite Introduction ](#Playwrite-intro)
    - [Requirements](#Playwrite-Requirements)
    - [Setup & installation](#setup-installation)
    - [Lab ](#Lab) 

# Introduction
 ## objectives
-	Ensure the system meets the functional requirements as detailed in the SRS.
-	Validate the system’s non-functional requirements.
-	Identify and rectify defects prior to release.
-	Ensure the application accurately handles data and operations.
-	Confirm error handling and validation mechanisms.
-	Verify integration between different modules.
-	Ensure usability and efficiency of the command-line interface.

 ## Project Team
    1. Logan Bennett - Code Developer
    2. Samson Truelove - Code Developer
    3. Aiden Morris - Code Developer
    4. Ava Vanduinen - Tester
    5. Sydney Southerland - Tester
    6. Juan Gomez - Tester
    7. Abdul Caesar - Document Writer
    8. Luke Wainwright - Document Writer
    9. Stephen Rotich - Project Lead/document Writer

# Selenium Lab
## Introduction
Selenium is an open-source software suite of browser automation tools for controlling web browsers through programs and performing browser automation. It is functional across browsers and operating systems and can be used in various programming languages.<br>
for more information please visit the selenium lab website <!--[selenium documentation](https://www.selenium.dev/documentation/)--> <a href="https://www.selenium.dev/documentation/">selenium documentation</a>
</p>
<br>
<br>

## Requirements 

  - Installing Python and Selenium WebDriver. 
  - Setting up ChromeDriver for Google Chrome. 
  - Verifying the installation with a simple script 
  
## Setup & installation
please verify that you have python and PIP installed
to verify if python or PIP are  installed ,Open your terminal or command prompt. e.g CMD,powershell,Linux Terminal or Git Bash and type ```python --version```  ```pip --version``` as shown  in the example below using powerShell
![Powershell ](Assets/image.png)

If Python or Pip is not installed ,Follow the instructions below

 ```
 Install Python
1. Download Python from the official Python website.
2. Run the installer.
3. Make sure to check the box that says "Add Python to PATH" during installation.
4. Verify Python & PIP are installed
```

python official site: <https://www.python.org/downloads/>
<br>
<br>

#### 2. Selenium installation

Make sure you've completed step 1 and have PIP installed and verified. Then, you'll be ready to easily install Selenium
Using PIP ,install Selenium package  terminal or command prompt by typing `pip install selenium`

![Alt text](Assets/image-2.png)
<br>
<br>

#### 3. Download WebDriver

Each browser requires a separate driver and needs to be downloadesd separately
for instance :

+ Chrome:<https://sites.google.com/a/chromium.org/chromedriver/>
+ Firefox: <https://github.com/mozilla/geckodriver/releases>
+ Safari: Safari driver come swith the macOS
+ Edge: <https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/>
  
__For windows__

```
Extract the downloaded driver and place it in a location of your choice
Add the path to the driver in your system's PATH variable. This ensures Python can access and use the driver.
```

__For Linux__

```
Move the downloaded driver to /usr/local/bin or any directory in your PATH 
Ensure proper permissions are granted to the driver (use chmod +x ) 
```
#### 4. verify the installation by writing and running the following script
```
 # Python script to verify Selenium installation 
from selenium import webdriver

# Specify the path to chromedriver
driver = webdriver.Chrome('http://127.0.0.1:5000')

#  Open a website 
driver.get('http://www.google.com')

# Close the browser
driver.quit()

```
## selenium Lab guide 

This section entails the Implementation of the  tests for different functionalities of a web application, and it covers the creation and running  of tests 

```
from selenium import webdriver
from selenium.webdriver.common.by import By
```

```

# Initialize the Chrome WebDriver. This allows Selenium to control a Chrome browser instance

driver = webdriver.Chrome()

# Navigate to the Flask web application's URL

driver.get("<http://127.0.0.1:5000/>") 
```
```
def test_loading_webpage():
    # Test to ensure the main page loads correctly.
 ```

```
def test_presence_of_elements():
    # Test to verify the presence of key elements on the webpage. 
```

```
def test_search_functionality():
    # Test the search functionality.
    
    # TODO: Add detailed assertions for the search results.
```

```
def test_table_interaction():
    # Test interactions with the book details table.
    
    # TODO: Add detailed assertions for the table interaction results.
    
```

```
test_loading_webpage()
test_presence_of_elements()
test_search_functionality()
test_table_interaction()
driver.close()
```

## selenium Test Cases 
    
# BDD Lab  
    
# API Test LAB 
    

# TDD Lab

# Playwrite Lab
## Playwright Lab: Testing a Bookstore Web Application
Playwright is a powerful framework for automating browsers, allowing developers to simulate user interactions with web applications. It supports multiple browsers, making it ideal for cross-browser testing. Playwright is primarily used for end-to-end testing, which tests the flow of an application from start to finish. It ensures that the integrated components of an application function as expected. This lab will guide you through the process of using Playwright to write and execute tests on a Flask-based bookstore web application.

## Getting Started with Playwright
#### Install Python:
Ensure Python (version 3.7 or higher) is installed on your system. You can download it from .

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

#### Learning Resources:
- Official Playwright Documentation:
	- Comprehensive guide and reference to Playwright features and API.
- Online Tutorials and Courses:
	- A course on Udemy covering basics to advanced concepts.
	- A series of video tutorials for visual learners.
- Community Forums and Support:
	- For contributions, issues, and discussions related to Playwright.
	- Community Q&A on Playwright-related topics.



## Writing Playwright Tests
1. Open Your Test File
2. In your project folder, open the file named playwright_test_suite.py.
   This file will contain all your Playwright tests.
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


#### Test Examples
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

#### Incomplete Test Scenarios (Exercises YOU need to Complete):
3. Test 3 (Incomplete) - Search Functionality:
   Write a test that searches for a book and verifies the search results.
   Instruction: Fill in the search input, click the search button, and assert that the expected result is present in the page content.
4. Test 4 (Incomplete) - Error Handling:
    Write a test for handling an error, like submitting an empty form.
      Instruction: Try submitting the 'Add Book' form without filling in any details and assert that the appropriate error message is displayed.

#### Expected Results from Testing

- Test 1: For the "Loading the Webpage" test, the page title should match "County Bookstore".
- Test 2: In the "Adding a New Book" test, the new book title should be present in the page content after submission.
- Test 3: Expected results will depend on the specific implementation but should generally include successful execution of the search.
- Test 4:  Expected results will depend on the specific implementation but should generally include proper error handling.

#### Running the Tests
Execute your tests using the command:
	` python playwright_test_suite.py `
         Observe the results to ensure all tests are functioning as expected.

## Conclusion
This lab provides a comprehensive introduction to automated web testing using Playwright. Through a mix of guided examples and interactive exercises, you will gain practical experience in testing web applications. This hands-on approach is designed to enhance your skills in both Playwright and general web testing methodologies.
   
   
   
