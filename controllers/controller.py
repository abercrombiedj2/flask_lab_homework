from app import app
from flask import render_template
from models.order_list import orders

@app.route("/index")
def index():
    return render_template("index.html", orders=orders)

@app.route("/order/<index>")
def order(index):
    return render_template("order.html", order=orders[int(index)])