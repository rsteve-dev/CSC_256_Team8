




#### TC001 - Book Search Functionality

![Alt text](Assets/image-6.png)
<br> This is a database query and no changes should be made in the database
<table>
    <tr>
        <td>Objective</td>
        <td>Validate book search functionality.</td>
    </tr>
    <tr>
        <td>Prerequisite</td>
        <td>User is on the bookstore's homepage and The database has books listed</td>
    </tr>
    <tr>
        <td>Steps</td>
        <td>
            1. Navigate to the search bar.<br>
            2. Enter a known book title, e.g., "Harry Potter." <br>
            3. Click <i> Search </i> or press <i>Enter </i>.
        </td>
    </tr>
    <tr>
        <td>Expected Result</td>
        <td>Relevant book titles (all "Harry Potter" series books) display in the results</td> <br>
    </tr>

</table>

#### TC002 - Add Book to Cart from Search

![Alt text](Assets/image-7.png)
<table>
    <tr>
        <td>Objective</td>
        <td>Validate the process of adding a book to the cart from search results</td>
    </tr>
    <tr>
        <td>Prerequisite</td>
        <td>User has searched for a book and results are displayed</td>
    </tr>
    <tr>
        <td>Steps</td>
        <td>
            1. From the list of displayed books, locate "Harry Potter and the Philosopher's Stone."<br>
            2. Click on "Add to Cart." <br>
        </td>
    </tr>
    <tr>
        <td>Expected Result</td>
        <td>Confirmation pop-up: "Harry Potter and the Philosopher's Stone added to cart.<br>
        Cart icon updates with a number or indication of content <br>
        </td>  
    </tr>

</table>

####  TC003 - View Cart Items
![Alt text](Assets/ViewCartItems.png)
<table>
    <tr>
        <td>Objective</td>
        <td>Validate that a user can view all items added to their cart, including the book title, author, price, and quantity. Additionally, validate that the total price is displayed and is the correct sum of all items in the cart</td>
    </tr>
    <tr>
        <td>Prerequisite</td>
        <td>User has added at least one book to the cart.</td>
    </tr>
    <tr>
        <td>Steps</td>
        <td>
            1. log into the online bookstore.<br>
            2. browse and adds several books to the cart.<br>
            3.  navigates to the cart page <br>
        </td>
    </tr>
    <tr>
        <td>Expected Result</td>
        <td>The cart page fetches the cart items from the user's session or database.<br>
            The page displays all the cart items with book title, author, price, and quantity.<br>
            The total price for all items in the cart is displayed at the bottom <br>
        </td>  
    </tr>

</table>

`-----------------> add more test cases `
