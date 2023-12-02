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