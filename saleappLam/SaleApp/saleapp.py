import json
from flask import render_template
from SaleApp import app
from SaleApp import dao

@app.route('/')
def index():
    cate = dao.load_categories()
    p = dao.load_products()
    return render_template('index.html', categories = cate, products = p)


if __name__ == '__main__':
    app.run(debug=True)
