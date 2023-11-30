# CSC256 Team 8 Test Labs ReadMe


    
# Table of content 
- [Introduction](#introduction)
  - [objectives](#Objectives)
  - [Project Team](#Project-Team)
  
i. [Selenium Lab](#Selenium-Lab)
    - [Introduction](#selenium-intro)
    - [Requirements](#selenium-Requirements)
    - [Setup & installation](#setup-installation)
    - [Lab ](#Lab) 
    
ii. [BDD Lab](#BDD-Lab)  
    
iii.[API Test LAB](#API-est-Lab)  
    

iv. [TDD Lab](#TDD-Lab)

v. [Playwrite Lab](#Playwrite-Lab)

# Introduction
- ## objectives
- ## Project Team
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
   
   
   
