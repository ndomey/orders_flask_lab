from flask import Blueprint
from flask import render_template
from models.task_list import orders

orders_blueprint = Blueprint("order", __name__)

@orders_blueprint.route("/orders")

def index():
    return render_template('index.jinja', title="Motorcycle order list", orders=orders)