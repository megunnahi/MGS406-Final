from flask import Flask, render_template, request
import mysql.connector as sql
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def home_page():
    return render_template('home.htm')

@app.route('/newinfo/')
def new_order():
    return render_template('new_order.htm')

@app.route('/order/', methods = ['POST', 'GET'])
def order_page():
    msg = ''
    if request.method == 'POST':
        try:
            custID = request.form['CustID']
            custName = request.form['CustName']
            custGender = request.form['CustGender']
            custPhone = request.form['CustPhone']
            custOrder = request.form['CustOrder']
            arrival = request.form['arrivalDate']

            print("")
            print(f"Received ID: {custID}")
            print(f"Recevied Name: {custName}")
            print(f"Received Gender: {custGender}")
            print(f"Received Phone: {custPhone}")
            print(f"Received Order: {custOrder}")
            print(f"Received Date: {arrival}")

            with sql.connect(host = "localhost", user = "James", password = "bob14228", database = "clothing_store") as conn:
                print("Connected to MySQL")
                cur = conn.cursor()
                cur.execute("INSERT INTO customer (CustID, CustName, CustGender, CustPhone, CustOrder, arrivalDate) VALUES('{0}', '{1}', '{2}', '{3}', '{4}', '{5}');".format(custID, custName, custGender, custPhone, custOrder, arrival))

                print("SQL Statement has been executed")
                conn.commit()
                print("Committed")
                msg = "Customer order has been added"
                conn.close()
                print("Connection has been closed")

        except:
            conn.rollback()
            msg = "Error in recording customer order"
            conn.close()
        finally:
            return render_template("order.htm", msg = msg)

@app.route('/records/')
def records_page():
    conn = sql.connect(host = "localhost", user = "James", password = "bob14228", database = "clothing_store")
    cur = conn.cursor()
    cur.execute("SELECT * FROM customer;")

    rows = cur.fetchall()
    print(rows)
    return render_template('records.htm', rows = rows)

if __name__ == "__main__":
    app.run(debug == True)
