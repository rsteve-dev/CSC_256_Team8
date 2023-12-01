# Lab Testing Progress

## API Test Lab
### Test Cases (based on the api_Test_Lab.md file)
- **TC001:** List Books: `/api/books`
	- Result:
	- Status:
- **TC002:** List Books by Attribute: `/api/books?attribute=published_year&value=2007`
	- Result:
	- Status:
- **TC003:** Display Single Book: `/api/books/{isbn}`
	- Result:
	- Status:
- **TC004:** Get Categories: `/categories`
	- Result:
	- Status:
 - **TC005:** Error Handling: All Endpoints
	- Result:
 	- Status:
 
### Lab Testing
- **TC001:** TBD
	- Result:
	- Status:
- **TC002:** TBD
	- Result:
	- Status
- **TC003:** TBD (Student Input)
	- Result:
	- Tester Code Used:
	- Status:
- **TC004:** TBD (Student Input)
	- Result:
	- Tester Code Used:
 	- Status:

- - -

## BDD Lab
### Lab Testing
- **TC001:** TBD
	- Result:
	- Status:
- **TC002:** TBD
	- Result:
	- Status:
- **TC003:** TBD
	- Result:
	- Status:
- **TC004:** TBD (Student Input)
	- Result:
	- Tester Code Used:
	- Status:
- **TC005:** TBD (Student Input)
	- Result:
	- Tester Code Used:
 	- Status:

- - -

## Playwright Lab
### Lab Testing
- **TC001: Loading the Webpage and Checking the Title**
	- Result: For the "Loading the Webpage" test, the page title should match "County Bookstore".
	- Status: Attempted - currently waiting for [Issue #21](https://github.com/rsteve-dev/CSC_256_Team8/issues/21) to be resolved.
- **TC002: Adding a New Book**
	- Result: In the "Adding a New Book" test, the new book title should be present in the page content after submission.
	- Status: Attempted - currently waiting for [Issue #21](https://github.com/rsteve-dev/CSC_256_Team8/issues/21) to be resolved.
- **TC003: Search Functionality (Student Input)**
	- Result: Expected results will depend on the specific implementation but should generally include successful execution of the search.
	- Tester Code Used:
	- Status: Attempted - currently waiting for [Issue #21](https://github.com/rsteve-dev/CSC_256_Team8/issues/21) to be resolved.
- **TC004: Error Handling (Student Input)**
	- Result: Expected results will depend on the specific implementation but should generally include proper error handling.
	- Tester Code Used:
	- Status: Attempted - currently waiting for [Issue #21](https://github.com/rsteve-dev/CSC_256_Team8/issues/21) to be resolved.

- - -

## Selenium Lab
### Lab Testing
- **TC001: Validate that the new book “Pages” and “Release Year” fields only accept integers**
	- Result: For the “Non-int input” test, the page and release year boxes in the ‘New Book’ section won’t be able to accept a non-numeric input.
	- Status: Complete & Passed
- **TC002: Adding a New Book**
	- Result: In the "Adding a New Book" test, the new book title should be present in the page content after submission.
	- Status: Complete & Passed
- **TC003: Search Functionality (Student Input)**
	- Result: Expected results will depend on the specific implementation but should generally include successful execution of the search.
	- Tester Code Used:
		```
  		# Select the Search box
  		search_title = "Gilead"

  		# Click the Search bar to enter the desired title if not selected already
        if("none" in driver.find_element(By.ID, "searchInput").get_attribute("style")):
            driver.find_element(By.ID, "searchInput").click()
        
        # Send input
        driver.find_element(By.ID, "searchInput").send_keys(search_title)

        # Check to see if the book title is present in the page
        # 2 seconds of wait added to allow for the page to refresh
        driver.implicitly_wait(2)
        assert search_title in driver.page_source
	- Status: Complete & Passed
- **TC004: Error Handling (Student Input)**
	- Result: Expected results will depend on the specific implementation but should either assert the presence of a displayed error or other handling.
	- Tester Code Used:
		```
  		# Show the new book box
        new_book_button = driver.find_element(By.ID, "newBookToggle")

        # Click the Add New Book button to display the book section if not displayed already
        if("none" in driver.find_element(By.ID, "addNewBook").get_attribute("style")):
            new_book_button.click()

        # Wait half a second for the box to appear
        driver.implicitly_wait(0.5)

        # Attempt to add empty inputs
        empty_title = ""
        driver.find_element(By.ID, "newTitle").send_keys(empty_title) 
        driver.find_element(By.ID, "newAuthor").send_keys("")
        driver.find_element(By.ID, "newGenres").send_keys("")
        driver.find_element(By.ID, "pages").send_keys("")
        driver.find_element(By.ID, "releaseYear").send_keys("")

        # Submit new book
        driver.find_element(By.ID, "submitNewBook").click()
	- Status: Complete & Passed

![Screenshot showing a Terminal output indicating that the tests ran and passed.](Assets/Selenium_Lab_Testing_Complete.png)

- - -

## TDD Lab
### Lab Testing
- **TC001:** TBD
	- Result:
	- Status:
- **TC002:** TBD
	- Result:
	- Status:
- **TC003: Getting CSV Data (Student Input)**
	- Result:
	- Tester Code Used:
	- Status:
- **TC004: Writing CSV Data (Student Input)**
	- Result:
	- Tester Code Used:
	- Status:
