from flask import Flask
from models import *

from pony.orm import serialization

app = Flask(__name__)


@app.route("/restaurant/<int:restaurant_id>/item")
@orm.db_session
def get_menu(restaurant_id):
    restaurant = Restaurant.select(lambda r: r.id == restaurant_id).first()

    if not restaurant:
        return '{"error": "There is no such restaurant"}', 400

    menu_items = (item for item in orm.select(mi for mi in MenuItem if mi.restaurant == restaurant))
    return serialization.to_dict(menu_items)
