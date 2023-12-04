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
