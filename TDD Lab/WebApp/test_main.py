import pytest
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.close()

@pytest.fixture
def temp_csv_file(tmp_path):
    filename = tmp_path / "mydir/myfile"
    filename.parent.mkdir()
    filename.touch()
    headers = ["title", "author", "genre", "pages", "releaseYear"]
    with open(filename,'w') as csvfile:
        writer = csv.DictWriter(csvfile,fieldnames=headers)
        writer.writeheader()
        writer.writerow({"title" : "Fake Title", "author" : "Fake Author", 
                         "genre" : "Fiction", "pages" : "100", "releaseYear" : "2023"})
    return filename
        


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
    

@pytest.mark.parametrize("expected_data", 
                         [[{"title" : "Fake Title", "author" : "Fake Author", 
                         "genre" : "Fiction", "pages" : "100", "releaseYear" : "2023"}]])
def test_get_csv_data(temp_csv_file, expected_data):
    # Test to validate the CSV data can be sucessfully retrieved
    # Follow the three phases/rules of TDD when writing the test & include screenshots of each phase. 
    try:
        #Add your test functionality here
        pass

    except Exception as e:
        # Handle any exceptions that occur during the test
        pytest.fail(f"An error occurred during the test: {e}")



def test_write_csv_data(temp_csv_file):
    # Test to validate the CSV data can be sucessfully written
    # Follow the three phases/rules of TDD when writing the test & include screenshots of each phase.
    try:
        #Add your test functionality here
        pass

    except Exception as e:
        # Handle any exceptions that occur during the test
        pytest.fail(f"An error occurred during the test: {e}")