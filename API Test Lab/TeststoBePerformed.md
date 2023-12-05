## TC001 - Testing endpoint: `Endpoint: /api/books`

1. Send a request with valid credentials 
   -  we expect  200 OK response.
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

  1. Send a request with specific query parameters e.g.` ?attribute=published_year&value=2007`
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

pm.test("TC002: Edge Case - Non-existent Attribute Values", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData).to.be.an('array').that.is.empty;
});

pm.test("TC002: Edge Case - Special Characters in Query", function () {
    pm.response.to.have.status(400); // Assuming 400 for bad request
});
pm.test("TC002: List Books by Attribute - Response is a JSON array", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData).to.be.an('array');
});

```

## TC003: Test Endpoint to Display single Book :  `/api/books/{isbn}`

 1. send a GET request for a single book:
   -  Confirm a 200 OK status for valid ISBN
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

