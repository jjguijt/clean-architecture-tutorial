import sqlite3
con = sqlite3.connect("orders.db")

cur = con.cursor()

cur.execute("CREATE TABLE \"order\"(id, customer_name)")
cur.execute("CREATE TABLE order_item(order_id, product_id, number)")
cur.execute("CREATE TABLE product(product_id, product_name, unit_cost_cents)")

cur.execute("""
    INSERT INTO \"order\" VALUES
        ("0001", "Flip de Kort"),
        ("0002", "John Miller"),
        ("0003", "Francois Villeneuve")
""")

cur.execute("""
    INSERT INTO order_item VALUES
        ("0001", "0001", 2),
        ("0002", "0003", 1),
        ("0002", "0005", 1),
        ("0003", "0002", 5)
""")

cur.execute("""
    INSERT INTO product VALUES
        ("0001", "Banana", 122),
        ("0002", "Apple", 99),
        ("0003", "Milk", 52),
        ("0004", "Pizza", 580),
        ("0005", "Cauliflower", 399)
""")

con.commit()
con.close()
