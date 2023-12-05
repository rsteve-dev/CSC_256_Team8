# Wake County Bookstore API Test Lab 

##  API Documentation

Welcome to the Wake County Bookstore. This API allows developers to access and interact with our online bookstore's features, including browsing books, managing a shopping cart, placing orders, and viewing order history.

## Base URL

The base URL for all API endpoints is: `http://127.0.0.1:3000`

## Authentication

Authentication is required to access specific API endpoints. We use API keys for authentication. To obtain an API key, please get in touch with our support team.

### Request Headers

 `Authorization: Bearer YOUR_API_KEY  supplied securely via sftp or other encrypted methodologies`  

## Endpoints

 Get the yaml representation using the openAPI 3.0 specification format here.***[wc-booksore.yaml](./wc-booksore.yaml)***

1. #### List Books

 **Endpoint:** `/api/books` \
 **HTTP Method:** GET \
 **Description:** Get a list of books available in the bookstore. \
 **Parameters:**

- `search` : A search query to filter books by title, author, or genre. \
- `category`: Filter books by category or genre. \
 **Response:**
  - **Status Code:** 200 OK
  - **Body:** JSON array containing book objects. Example response:

```json
  [
    {
        "ISBN": "979-2591-85790-10-5",
        "authors": "Maria Garcia",
        "categories": "History",
        "num_pages": "962",
        "published_year": "2009",
        "subtitle": "The Mysteries",
        "title": "The Wind River"
    },
    {
        "ISBN": "971-4451-85690-10-5",
        "authors": "Charles Osborne;Agatha Christie",
        "categories": "Detective and mystery stories",
        "num_pages": "241",
        "published_year": "2000",
        "subtitle": "A Novel",
        "title": "Spider's Web"
    },
  ]
```

- **Status Code:** 500 OK

2. #### List Books by attribute e.g. published_year

 **Endpoint:** `/api/books?attribute=published_year&value=2007` \
 **HTTP Method:** GET \
 **Description:** Get a list of books available in the bookstore. \
 **Parameters:**

- `search` : A search query to filter books by title, author, or genre. \
- `category`: Filter books by category or genre. \
 **Response:**
  - **Status Code:** 200 OK
  - **Body:** JSON array containing book objects. Example response:

```json
  [
    {
        "ISBN": "979-2591-85790-10-5",
        "authors": "Maria Garcia",
        "categories": "History",
        "num_pages": "962",
        "published_year": "2009",
        "subtitle": "The Mysteries",
        "title": "The Wind River"
    },
    {
        "ISBN": "971-4451-85690-10-5",
        "authors": "Charles Osborne;Agatha Christie",
        "categories": "Detective and mystery stories",
        "num_pages": "241",
        "published_year": "2000",
        "subtitle": "A Novel",
        "title": "Spider's Web"
    },
  ]
```

- **Status Code:** 500 OK

3. #### Display single Book {by unique id e.g. isbn}

 **Endpoint:** `/api/books/{isbn}` \
 **HTTP Method:** GET \
 **Description:** Get detailed information about a specific book. \
 **Parameters:** \
   `book_id` : The unique identifier of the book. \
 **Response:**

- **Status Code:** 200 OK
- **Body:** JSON array containing book objects. Example response:

  ```json
  {
  "id": "1",
  "title": "The Great Gatsby",
  "author": "F. Scott Fitzgerald",
  "price": 10.99,
  "description": "A classic novel...",
  "category": "Fiction"
  }
 ```

4. #### Add Book to Cart

 **Endpoint:** `/api/{{userID}}/cart/add`  \
 **HTTP Method:** POST \
 **Description:** Add a book to the user's shopping cart. \
 **Response:**

- **Status Code:** 201 Created
- **Body:** Confirmation message.
- **Body:** JSON object containing book_id and quantity.
  
```json
  {
  "book_id": "1",
  "quantity": 2
  }

```

5. #### View Cart

**Endpoint:** `/api/{{userID}}/cart` \
**HTTP Method:** GET \
**Description:** Get the user's shopping cart contents. \
**Response:**

- **Status Code:** 200 OK
- **Body:** JSON array of cart items.

  ```json
    [
        {
          "ISBN": "979-2591-85790-10-5",
          "authors": "Maria Garcia",
          "categories": "History",
          "num_pages": "962",
          "published_year": "2009",
          "subtitle": "The Mysteries",
          "title": "The Wind River"
        }
    ]
  ```

6. #### Remove Book from Cart

**Endpoint:** /cart/remove/{book_id} \
**HTTP Method:** DELETE \
**Description:** Remove a book from the user's shopping cart. \
**Parameters:**
`book_id`: The unique identifier of the book. \
**Response:**

- **Status Code:** 204 No Content
  
7. #### Get Categories

**Endpoint:** /categories \
**HTTP Method:** GET \
**Description:** Get a list of available book categories or genres. \
**Response:**

- **Status Code:** 200 OK
- **Body:** JSON array of category objects. Example response:

```json
[
  "Fiction",
  "Non-Fiction",
  "Mystery",
  "Science Fiction"
]
```


# Postman Installation and User Guide

## Introduction

Postman is a popular tool for API development and testing. It allows developers and Testers to build, test, and document APIs easily. This guide will help  with the installation process and provide  an overview of how to use Postman.

## Installation

### Step 1: Downloading Postman

1. Visit the Postman website to download the application. [Postman Downloads](https://www.postman.com/downloads/).
2. Choose the version suitable for your operating system (Windows, MacOS, Linux).
3. Click on the download link to start the process.

### Step 2: Installing Postman

- After downloading, open the installer file.
- Follow the on-screen instructions to complete the installation.

## Getting Started with Postman

#### Creating an Account

- Upon opening Postman for the first time, you will be prompted to create an account. This can be done using an email address, Google account, or other sign-in methods.
- Creating an account allows you to sync your collections across devices and access more features.

#### Postman Interface

- Familiarize yourself with the Postman interface. Key areas include:
  - **Request Tab**: Where you create new requests.
  - **Response Section**: View responses to your requests.
  - **Collections**: Organize your requests and tests.

#### Making Your First API Request

1. Click on the `New` button and select `Request`.
2. Enter the details for your request:
   - **URL**: Enter the API endpoint you wish to test.
   - **Method**: Select the HTTP method (GET, POST, PUT, DELETE, etc.).
   - **Headers/Body**: Add as needed depending on your API requirements.
3. Click `Send` to execute the request.
4. The response will appear in the section below.
5.
   ![Alt text](./postman_images/send_request.png)

#### Saving Requests

- Save your requests in collections for easy access and organization.
- Click on the `Save` button after setting up your request and specify the collection to save it in.

#### Using Collections and Environments

- ***grab the collection and Environment files in the github repo inside API test lab folder and import it to your local installed postman***
  
- **Collections**: Group related requests for easier management and execution.

- **Environments**: Use environments to manage sets of variables for different setups (like development, testing, production).
-
- ![Alt text](./postman_images/collection.png)

#### Writing  Tests

- Postman allows us to write tests in JavaScript in the `Tests` tab.
- These tests can validate various aspects of the response, such as status codes and response bodies.

![Test](./postman_images/imagex.png)

### Running Collections

- Use the Collection Runner to run a series of requests in a collection, which is useful for automated testing.

#### Conclusion

This guide provides  steps to get started with Postman. For more advanced features and detailed documentation, visit the [Postman Learning Center](https://learning.postman.com/).



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


###### Error Handling (All Endpoints)

- **Invalid Method:** Use an invalid HTTP method to test error handling.
- **Timeout Simulation:** Simulate a request timeout and verify response.
- **Authorization:** Access endpoints requiring authorization with and without valid API keys.

## TC001 - Testing endpoint: `Endpoint: /api/books`

1. Send a request with valid credentials
   - we expect  200 OK response.
2. Send a request with invalid or no API key using this endpoint:
   - expect a 401 Unauthorized .
3. Send a request with a malformed URL for example <http://127.0.0.1:3001> in place of <http://127.0.0.1:3000> (changed  port number)
   - expect a 404 Not Found or similar error response
4. Send a request to the endpoint and check the json response
    - is it a valid response but with an empty `JSON` response?
    - Does the Json Response contain data?

#### Postman Tests for TC001

```
pm.test("TC001: List Books - Status code is 200", function () {
    pm.response.to.have.status(200);
});
pm.test("TC001: Edge Case - Invalid API Key", function () {
    var unauthorizedStatus = pm.response.code === 401 || pm.response.code === 403;
    pm.expect(unauthorizedStatus).to.be.true;
});
pm.test("TC001: Edge Case - Malformed URL", function () {
    pm.response.to.have.status(404);
});

pm.test("TC001: List Books - Response is a JSON array", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData).to.be.an('array');
});
pm.test("TC001: Edge Case - Handle Empty Array", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData.length).to.be.at.least(0);
});


```

## TC002: Testing Endpoint supplied with attribute e.g published_year :  `/api/books?attribute=published_year&value=2007`

  1. Send a request with specific query parameters e.g.`?attribute=published_year&value=2007`
    - we expect  200 OK response.
  
  2. Use non-existent attribute values (e.g., a future year) and expect a proper handling,

- Expectation: empty array

  3. Verify the API's response when the attribute filter matches no books

- Expectation: empty array
  
#### Postman Tests for TC002

```
pm.test("TC002: List Books by Attribute - Status code is 200", function () {
    pm.response.to.have.status(200);
});

pm.test("TC002: Non-existent Attribute Values", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData).to.be.an('array').that.is.empty;
});

pm.test("TC002: Special Characters in Query", function () {
    pm.response.to.have.status(400); // Assuming 400 for bad request
});
pm.test("TC002: List Books by Attribute - Response is a JSON array", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData).to.be.an('array');
});

```

## TC003: Test Endpoint to Display single Book :  `/api/books/{isbn}`

 1. send a GET request for a single book:

- Confirm a 200 OK status for valid ISBN

  2. Use an invalid or non-existent ISBN and expect a 404 Error
  3. Test with a malformed ISBN (e.g., incorrect format) and check the response
  4. end a request to the endpoint and check the json response

#### Postman Tests for TC003

```
pm.test("TC003: Display Single Book - Status code is 200", function () {
    pm.response.to.have.status(200);
});
pm.test("TC003: Invalid ISBN", function () {
    pm.response.to.have.status(404);
});
pm.test("TC003: Display Single Book - Response is a JSON object", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData).to.be.an('object');
});

```

## TC004: Test Endpoint Add Book to Cart' Endpoint :  `/api/{{userID}}/cart/add`

1. check for a 201 Created status after adding a book
    - Expected Results: 201 status code
2. Confirm the presence of ISBN ,authors,categories,num_pages,published_year,subtitle,title in the response.
3. Try adding a book with invalid or extreme quantities

#### Postman Tests for TC004

```
pm.test("TC004: Add Book to Cart - Status code is 201", function () {
    pm.response.to.have.status(201);
});
pm.test("TC004: Add Non-existent Book", function () {
    pm.response.to.have.status(404);
});

pm.test("TC008: Add Book to Cart - Contains ISBN ,authors,categories,num_pages,published_year,subtitle,title", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData).to.have.property('ISBN');
    pm.expect(jsonData).to.have.property('authors');
    pm.expect(jsonData).to.have.property('categories')
    pm.expect(jsonData).to.have.property('num_pages')
    pm.expect(jsonData).to.have.property('published_year')
    pm.expect(jsonData).to.have.property('subtitle')
    pm.expect(jsonData).to.have.property('title')
});

```
