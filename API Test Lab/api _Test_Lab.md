# Wake County Bookstore API Test Lab 

## 1. Setting Up the Environment

###### `Virtual Machines or Containers`

- Utilize VMs or containers (like Docker) for isolated testing environments.
- Create `Dockerfile` and `docker-compose.yml` for easy setup and replication.

### Localhost Setup

- Ensure API is running on `localhost` (<http://127.0.0.1:3000>).
- Verify accessibility from test machines or containers.

## 2. Tools for Testing

###### API Testing Tools
***please check the provided postman installation guide for the preseeding tasks ***

- **Postman** : For manual API interactions and testing 
  

## 3.  API Test Cases

- API doumentation provided in this directory contains a detailed description of each endpoints
  - Develop test cases for each API endpoint and add any edsge cases that might be missing .
  - Create automated scripts for these test cases.
  - Cover authentication, request parameters, response validation, and error handling.

###### List Books (`/api/books`)

- **Happy Path Test:** GET request without parameters to verify response with a list of books.
- **Filter by Category:** GET request with a valid `category` parameter to verify filtered response.
- **Search Query:** GET request with `search` parameter to verify relevant books are returned.
- **Invalid Parameters:** GET request with invalid parameters to test error handling.
- **Server Error Simulation:** Simulate a server error and verify a 500 status code response.

###### List Books by Attribute (`/api/books?attribute=published_year&value=2007`)

- **Filter by Published Year:** GET request with valid `published_year` and `value`.
- **Invalid Year:** GET request with an invalid year to test error handling.
- **Non-Existent Attribute:** GET request with a non-existent attribute to test error handling.

###### Display Single Book (`/api/books/{isbn}`)

- **Valid ISBN:** GET request with a valid ISBN to verify correct details.
- **Invalid ISBN:** GET request with an invalid ISBN to test error handling.

###### Add Book to Cart (`/api/{{userID}}/cart/add`)

- **Add Book:** POST a valid `book_id` and `quantity` and verify the response.
- **Invalid Book ID:** POST with an invalid `book_id` to test error handling.
- **Invalid Quantity:** POST with an invalid `quantity` to test error handling.

###### View Cart (`/api/{{userID}}/cart`)

- **Valid User ID:** GET request with a valid `userID` to verify correct cart contents.
- **Invalid User ID:** GET request with an invalid `userID` to test error handling.

###### Remove Book from Cart (`/api/{{userID}}/cart/remove/{book_id}`)

- **Valid Removal:** DELETE a valid `book_id` from user's cart and verify update.
- **Invalid Book ID:** DELETE with an invalid `book_id` to test error handling.

###### Get Categories (`/categories`)

- **Retrieve Categories:** GET request to verify all categories are listed correctly.

###### Place an Order (`/orders/place`)

- **Place Valid Order:** POST a valid order and verify the response.
- **Invalid Payment Info:** POST with invalid payment details to test error handling.
- **Empty Cart:** Try placing an order with an empty cart to test error handling.

###### View Order History (`/orders`)

- **Valid User ID:** GET request with a valid `userID` to verify correct order history.
- **Invalid User ID:** GET request with an invalid `userID` to test error handling.

###### Error Handling (All Endpoints)

- **Invalid Method:** Use an invalid HTTP method to test error handling.
- **Timeout Simulation:** Simulate a request timeout and verify response.
- **Authorization:** Access endpoints requiring authorization with and without valid API keys.
