To set up the server:

```
python -m pip install -r requirements.txt
```

To start the server:

```
flask --app clean_architecture/server/server run
```


## Tutorial app
There's a small application that connects to an API to read Order data. The application creates a small report on this, listing all orders with the name of the customer, products ordered and the total price.
The team responsible for the application is changing the API from version 1 to version 2. Try to apply Hexagonal Architecture when migrating from version 1 to version 2!


## Version 1 of the API

Get orders: `GET /api/v1/get_orders`: Returns a list of orders, where every order is itself a list: [id, customer name]

Example result: `[["0001", "Pete Harvey"]]`


Read order: `GET /api/v1/read_order/<id>`: Returns a list of items in an order, where every item is itself a list: [order_id, product_id, number of products]

Example result: `[["0002", "3814", 15]]`


Get product: `GET /api/v1/get_product/<id>`: Returns a single product as a list: [product_id, name, price in cents]

Example result: `["3814", "Banana", 280]`


## Version 2 of the API

Get orders: `GET /api/v2/orders`: Orders are an object `{"id": id, "customer": customer name}`

Example result: `[{"id": "0001", "customer": "Pete Harvey"}]`


Get order items: `GET /api/v2/order/<id>`: Order items are an object `{"order_id": order ID, "product_id": product ID, "nr": number of products}`

Example result: `[{"order_id": "0002", "product_id": "3814", "nr": 15}]`


Get product: `GET /api/v2/product/<id>`: Products are an object `{"id": product ID, "name": product name, "price_euros": the price in Euros}`

Example result: `{"id": "3814", "name": "Banana", "price_euros": 2.80}`


