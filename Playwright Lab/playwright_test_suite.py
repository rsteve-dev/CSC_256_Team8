
from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    
    # Test 001: Loading the webpage and checking the title
    page = context.new_page()
    page.goto("http://127.0.0.1:5000/")
    # Verify the webpage was loaded and has the correct title
    assert "County Bookstore" in page.title(), "Page title does not match"
    print("Test 001: Loading the webpage and checking the title - Passed")



    # Test 002: Adding a new book
    page.click("text=Add New Book")  # Click on the 'Add Book' button
    page.fill("input[name='title']", "New Book Title")  # Fill the title
    page.fill("input[name='author']", "Author Name")  # Fill the author
    page.fill("input[name='genres']", "Fiction")  # Fill the genre
    page.fill("input[name='pages']", "100")  # Fill the pages
    page.fill("input[name='releaseYear']", "2023")  # Fill the release year
    page.click("text=Submit")  # Submit the new book

    # Verify if a new book was added successfully
    assert "New Book Title" in page.content(), "New book was not added"
    print("Test 002: Adding a new book - Passed")



    # Incomplete Test 003: Search Functionality
    # Uncomment and complete the code below:
    #page.fill("input[id='searchInput']", )
    # Verify the expected result is present & VISIBLE in the page content
    #assert "Search Result" in "", "Search did not return expected results"
    #print("Test 003: Search Functionality - Passed")



    # Incomplete Test 004: Error Handling
    # Uncomment and complete the code below:
    #page.click("text=Add New Book") # Click on the 'Add Book' button
    #page.click("text=Submit")  # Submit the form without filling any details
    # Verify if an error message was raised
    #assert "Error Message" in page.content(), "Error handling not working as expected"
    #print("Test 004: Error Handling - Passed")
    

    
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
