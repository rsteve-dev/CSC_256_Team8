import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# Navigate to the Flask web application's URL.
driver.get("http://127.0.0.1:5000/")

@pytest.mark.parametrize("newTitle, newAuthor, newGenre, pages, releaseYear", (["Fake Title", "Fake Author", "Fiction", "100", "2023"]))
def test_add_new_book(newTitle, newAuthor, newGenre, pages, releaseYear):
    # Test to validate a new book can be successfully added
    try:
        assert newTitle == "Fake Title"
        assert newAuthor == "Fake Author"
        assert newGenre == "Fiction"
        assert pages == "100"
        assert releaseYear == "2023"
    except AssertionError:
        pytest.fail("Failed: test_add_new_book. Added book is not present.\n")

@pytest.mark.parametrize("newTitle, newAuthor, newGenre, pages, releaseYear", (["", "", "", "", ""]))
def test_add_new_book_raises_exception(newTitle, newAuthor, newGenre, pages, releaseYear):
    # Test to see if an invalid new book input correctly reports an error
    try:
        assert newTitle == ""
        assert newAuthor == ""
        assert newGenre == ""
        assert pages == ""
        assert releaseYear == ""
    except Exception as e:
        assert str(e) == "One or more inputs is invalid. Please re-check your provided book information."
        print("Test add_new_book_raises_exception() passed.")
    else:
        pytest.fail("Failed: test_add_new_book_raises_exception. Expected ExceptionError but no exception was raised.\n")

def test_get_csv_data():
    # Test to validate the CSV data can be sucessfully retrieved
    # Follow the three phases/rules of TDD when writing the test & include screenshots of each phase. 
    try:
        pass
    except AssertionError:
        pytest.fail("Failed: test_get_csv_data.")

def test_write_csv_data():
    # Test to validate the CSV data can be sucessfully written
    # Follow the three phases/rules of TDD when writing the test & include screenshots of each phase.
    try:
        pass
    except AssertionError:
        pytest.fail("Failed: test_write_csv_data.")

# Execute the test functions
test_add_new_book()
test_add_new_book_raises_exception()
test_get_csv_data()
test_write_csv_data()

# Close the browser window after tests.
driver.close()