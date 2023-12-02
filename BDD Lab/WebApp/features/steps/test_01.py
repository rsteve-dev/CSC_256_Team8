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