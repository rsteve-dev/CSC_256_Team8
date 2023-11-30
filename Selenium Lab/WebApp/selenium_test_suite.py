from selenium import webdriver
from selenium.webdriver.common.by import By
from random import randint

# Initialize the Chrome WebDriver. This allows Selenium to control a Chrome browser instance.
driver = webdriver.Chrome()

# Navigate to the Flask web application's URL.
driver.get("http://127.0.0.1:5000/")



def test_001_nonint_input():
    # Test to ensure the “Pages” and “Release Year” Fields only accepts integers
    print("Starting test: test_001_nonint_input")
    try:

        # Show the new book box
        new_book_button = driver.find_element(By.ID, "newBookToggle")

        # Click the Add New Book button to display the book section if not displayed already
        if("none" in driver.find_element(By.ID, "addNewBook").get_attribute("style")):
            new_book_button.click()

        # Wait half a second for the box to appear
        driver.implicitly_wait(0.5)

        # Attempt to put a character in int-only inputs
        driver.find_element(By.ID, "pages").send_keys("a")
        driver.find_element(By.ID, "releaseYear").send_keys("a")

        # Get the current contents of the input
        pages_input_content = driver.find_element(By.ID, "pages").get_attribute("value")
        release_year_input_content = driver.find_element(By.ID, "releaseYear").get_attribute("value")

        # Assert results
        assert pages_input_content == ""
        assert release_year_input_content == ""

        print("Passed: test_001_nonint_input\n")
        
    except Exception as e:
        print("Failed: test_001_nonint_input. Error: " + str(e) + '\n')



def test_002_add_book():
    # Test to ensure adding a new book works
    print("Starting test: test_002_add_book")

    try:
        # Show the new book box
        new_book_button = driver.find_element(By.ID, "newBookToggle")
        
        # Click the Add New Book button to display the book section if not displayed already
        if("none" in driver.find_element(By.ID, "addNewBook").get_attribute("style")):
            new_book_button.click()

        # Wait half a second for the box to appear
        driver.implicitly_wait(0.5)

        # Send inputs
        new_title = "Test Title " + str(randint(0, 100)) # Random number after title to prevent duplicate entries
        driver.find_element(By.ID, "newTitle").send_keys(new_title) 
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

        print("Passed: test_002_add_book\n")

    except AssertionError:
        print("Failed: test_002_add_book. Added book is not present\n")



def test_003_search_book():
    # Test to search for a specific book and assert the book is present in the results
    print("Starting test: test_003_search_book")

    try:
        #Add your test functionality here

        print("Passed: test_003_search_book\n")

    except AssertionError:
        print("Failed: test_003_search_book\n")



def test_004_invalid_input():
    # Test to see if an invalid new book input correctly reports an error
    print("Starting test: test_004_invalid_input")

    try:
        #Add your test functionality here

        print("Passed: test_004_invalid_input\n")

    except AssertionError:
        print("Failed: test_004_invalid_input\n")
        

# Execute the test functions.
test_001_nonint_input()
test_002_add_book()
test_003_search_book()
test_004_invalid_input()

# Close the browser window after tests.
driver.close()
