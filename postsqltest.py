import psycopg2

connect_str = "dbname='testpython' user='admin' host='localhost' password='admin'"

with psycopg2.connect(connect_str) as conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER , price REAL )")


    def insert_value(item_name, quantity_value, price_value):
        cur.execute("INSERT INTO store (item, quantity, price) VALUES(%s,%s,%s)", (item_name, quantity_value, price_value))


    def view_value():
        cur.execute("SELECT * FROM store")
        row = cur.fetchall()
        return row


    def delete_value(item):
        cur.execute("DELETE FROM store WHERE item=?", (item,))


    def update_value(item, quantity, price):
        cur.execute("UPDATE store SET quantity=?, price=? WHERE item=?", (quantity, price, item))


    insert_value("Apple 2", 400, 3.5)
    # print(view_value())

    conn.commit()
