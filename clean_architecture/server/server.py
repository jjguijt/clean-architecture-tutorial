import json
import sqlite3
from contextlib import contextmanager

from flask import Flask

@contextmanager
def db_connection():
    con = sqlite3.connect("orders.db")
    cur = con.cursor()

    try:
        yield cur
    finally:
        con.close()


app = Flask(__name__)



@app.route("/api/v1/get_orders")
def get_orders_v1():
    """
    Returns a list of orders
    Every order is itself a list [id, customer name]
    """
    with db_connection() as cur:
        result = cur.execute("SELECT * FROM \"order\";")
        rows = result.fetchall()
        return json.dumps(rows)


@app.route("/api/v1/read_order/<id>")
def read_order_v1(id):
    """
    Returns a list of items in an order
    Every item is itself a list [order_id, product_id, number of products]
    """
    with db_connection() as cur:
        # Imagine we handle SQL injection here
        result = cur.execute(f"SELECT * FROM \"order_item\" WHERE order_id = \"{id}\";")
        rows = result.fetchall()
        return json.dumps(rows)


@app.route("/api/v1/get_product/<id>")
def get_product_v1(id):
    """
    Returns details of a product
    Every product is a list [product_id, name, price in cents]
    """
    with db_connection() as cur:
        # Imagine we handle SQL injection here
        result = cur.execute(f"SELECT * FROM \"product\" WHERE product_id = \"{id}\";")

        row = result.fetchone()
        return json.dumps(row)


@app.route("/api/v2/orders")
def get_orders_v2():
    """
    Returns a list of orders
    Every order is an object {"id": id, "customer": customer name}
    """
    with db_connection() as cur:
        result = cur.execute("SELECT * FROM \"order\";")

        formatted_result = []
        for row in result.fetchall():
            formatted_result.append({"id": row[0], "customer": row[1]})
        return json.dumps(formatted_result)


@app.route("/api/v2/order/<id>")
def read_order_v2(id):
    """
    Returns a list of items in an order
    Every item is itself a list {"order_id": order ID, "product_id": product ID, "nr": number of products}
    """
    with db_connection() as cur:
        # Imagine we handle SQL injection here
        result = cur.execute(f"SELECT * FROM \"order_item\" WHERE order_id = \"{id}\";")

        formatted_result = []
        for row in result.fetchall():
            formatted_result.append({"order_id": row[0], "product_id": row[1], "nr": row[2]})
        return json.dumps(formatted_result)


@app.route("/api/v2/product/<id>")
def get_product_v2(id):
    """
    Returns details of a product
    Every product is a list {"id": product ID, "name": product name, "price_euros": the price in Euros}
    """
    with db_connection() as cur:
        # Imagine we handle SQL injection here
        result = cur.execute(f"SELECT * FROM \"product\" WHERE product_id = \"{id}\";")

        row = result.fetchone()
        formatted_result = {"product_id": row[0], "product_name": row[1], "price_euros": row[2] * 0.01}
        return json.dumps(formatted_result)
