Feature: Behave Tests Lab

    Scenario: Test 1: Validate that only partial input for a new book shows an error
        Given We have the bookstore and the new book box open 
        When We type a title in for a new book and nothing else
        Then It will not make a book and instead make an error

    Scenario: Test 2: Sorting by the pages column shows the smallest page count book
        Given We have the bookstore open
        When We click the page count header
        Then The book with the smallest page count will be at the top of the list

    #Scenario: Test 3: Ensure the search bar only searches the list of titles

    #Scenario: Test 4: Add a new book and verify its present in the list