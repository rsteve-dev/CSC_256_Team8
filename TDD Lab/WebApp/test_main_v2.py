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
        print("Test executed successfully.")

    except Exception as e:
        # Handle any exceptions that occur during the test
        pytest.fail(f"An error occurred during the test: {e}")
        pytest.fail(f"An error occurred during the test: {e}")
        