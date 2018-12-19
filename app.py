import json
from flask import Flask
from flask import render_template
from flask import request


app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index')


@app.route('/items', methods=['GET', 'POST'])
def items():
    with open('db.txt', 'r') as f:
        items = json.load(f)
        if request.method == 'POST':
            item = request.form['item']
            quantity = request.form['quantity']
            if "delete_button" in request.form.keys() and request.form["delete_button"] == "Delete":
                del items[item]
            with open('db.txt', 'w') as f2:
                json.dump(items, f2)
        return render_template('items.html', items=items)

