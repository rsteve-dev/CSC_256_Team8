# Wake County Online Bookstore

## Low-Level Design (LLD) 

#### version 1.0

 <br>

<table>
  <tr>
    <th>Version</th>
    <th>Authors</th>
    <th>Description</th>
    <th>Date Completed</th>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
</table>
<br>
<br>
<br>

## 1.0 Front End (UI)
Pages **- _subject to review by corders_**

+ Home Page: Featured books, Top sellers, Recommendations.
+ Book Details Page: Book information, reviews, add to cart button.
+ Search Results Page: Display books based on search queries.
+ Cart Page: List of added books, total price calculation, and checkout button.
+ User Profile: Purchase history, wish list, personal details.

## 2.0 Back End 

+ ###### Back End services
   Server side Logic will be implemented using Python -Flask
   The following endpoints will be implemented  ** _subject to review_ **
   <ol type ="I">
     <li>GET /books</li>
      <li>GET /books/:id</li>
      <li>GET /cart/:id</li>
      <li>POST /users/login</li>
      <li>POST /users/signup</li>
      <li>POST /purchase</li>
      
   </ol>

## 3.0 Database
Database collections,schemas and relationships

#### i. Users

+ userId: _Unique Identifier for a user_
+ username: _String (unique, indexed)_
+ passwordHash: _String (hashed password using bcrypt or similar)_
+ email: _String (unique, indexed)_
+ firstName: _String_
+ lastName: _String_
+ address: _containing street, city, state, postalCode,country_
+ purchasedBooks: _Array of books -IDs that the user has purchased_
+ wishlist: _Array of book IDs that the user has added to their wishlist_

#### ii. Books:

  + bookId: _Unique Identifier_
+ title: _String (indexed for search)_
+ author: _String (indexed for search)_
+ genre: _String (can be indexed if frequent genre-based queries are expected)_
+ price: _Float_
+ description: _Text_
+ publishDate: _Date_
+ inventoryCount: _Integer_
`coverImageUrl: _String (URL to the book's cover image)_`
+ rating: _Embedded document containing fields like averageRating (Float) and numberOfRatings (Integer)_

#### iii. Orders

+ orderId: _Unique Identifier for an order_ 
+ userId: _ID referencing the User who made the order_
+ bookId: ID referencing the Book purchased.
+ purchaseDate: _Date_
+ shippingStatus: _String (e.g., "Processing", "Shipped", "Delivered")_
+ totalAmount: _Float (to handle cases where book prices change in the future)_
+ quantity: _Integer (how many copies of the book were purchased)_

#### iv. Reviews
 ` _subject to review by corders & team _`

+ reviewId: _Unique Identifier for a review (e.g., ObjectID)_
+ userId: _ID referencing the User who wrote the review_
+ bookId: _ID referencing the reviewed Book_
+ reviewText: _Text_
+ rating: _Integer_
+ reviewDate: _Date_

###### User Management Module

 ###### Attributes,Functionality & Methods:
+ Collect user information (name, email, age, and book genre interest).
+ Validate and store user data in the database.
<!-->
| **Attributes** | user_id, email, password, name, address, cart, order_history                 |
|----------------|------------------------------------------------------------------------------|
| **Methods** | sign_up(), login(), logout(
 ## 4.0 suggested Modules,functionalities 
> #### User module 
> 
> ##### Functionality:
> - Authenticate users during login.
> - Validate user email.
> 
> #### Profile Management
> 
> ###### Functionality:
> - Allow users to update personal information and password.

## Book Management Module
> 
> #### Book Browsing and Searching
> 
> ###### Functionality:
> - Display books by categories (fiction, non-fiction, genres, etc.).
> - Provide a search feature for users to find specific books.
> 
> #### Book Details and Reviews
> 
> ###### Functionality:
> - Show detailed information about a book (author, description, price).
> - Allow users to submit reviews and ratings for books.
> 
> #### Shopping Cart
> 
> ###### Functionality:
> - Enable users to add books to the shopping cart.
> - Display the total price and allow modification of cart contents.
> 
> #### Order Processing
> 
> ###### Functionality:
> - Allow users to proceed to checkout and complete the purchase.
> - Generate an order confirmation with a unique order ID.

## Admin Panel Module
> 
> #### Content Management (Books)
> 
> ###### Functionality:
> - Allow admins to add, edit, or remove books from the catalog.
> 
> #### User and Order Management
> 
> ###### Functionality:
> - Enable admins to manage user accounts.
> - Allow admins to view order details.

