import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.close()

@pytest.mark.parametrize("newTitle, newAuthor, newGenre, pages, releaseYear", 
                         [("Fake Title", "Fake Author", "Fiction", "100", "2023")])
def test_add_new_book(driver, newTitle, newAuthor, newGenre, pages, releaseYear):
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
        title_ = driver.find_element(By.NAME, "title")
        author_ = driver.find_element(By.NAME, "author")
        genre_ = driver.find_element(By.NAME, "genres")
        pages_ = driver.find_element(By.NAME, "pages")
        year_ = driver.find_element(By.NAME, "releaseYear")

        title_.send_keys(newTitle)
        author_.send_keys(newAuthor)
        genre_.send_keys(newGenre)
        pages_.send_keys(pages)
        year_.send_keys(releaseYear)

        # Find and click the submit button
        submit_button = driver.find_element(By.ID, "submitNewBook")
        submit_button.click()
        print("Test executed successfully.")

    except Exception as e:
        # Handle any exceptions that occur during the test
        pytest.fail(f"An error occurred during the test: {e}")
        pytest.fail(f"An error occurred during the test: {e}")
        