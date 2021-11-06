# Order API
### API for ordering food

This project contains multiple API endpoints:
* /order-lists/ - Gives backs all the orders made
* /order-details/{id} - Gives back specific order
* /new-order/ - Gives back the latest order made
* /create-order/ - To create a new order
* /update-order/{id} - To update a specific order
* /delete-order/{id} - To delete a specific order
* /cust-contacted/ - To check if the user has recieved the email

API Heroku Deployment link - <a href="https://test-order-api.herokuapp.com/" target="_blank">here </a>

Zapier link - <a href="https://zapier.com/shared/5fe385985fbfa3434afa7f5ddcf7a1ec0f683413">Here</a>

For the zapier flow, I'm using /new-order/ endpoint to retrieve the latest order made and then using the data(email) from the get request, I'm sending a mail of 
Order Confirmation to the customer.(Using Email with Zapier, because Gmail repeatedly send mail to the same mail address, even when mail address were different from the GET request).

And after sending mail, using a POST request, I'm updating /cust-contacted/ endpoint giving relevant data and marking "contacted" key as True.
Temporarily, I'm triggering zapier from a GET request in /create-order/ endpoint.



