# from doctest import debug
import math

from flask import render_template, request
import dao
from saleapp.app import app


@app.route("/")
def index():
    cates = dao.load_categories()

    page = request.args.get('page', 1)
    cate_id = request.args.get('category_id')
    kw = request.args.get('kw')
    prods = dao.load_products(cate_id=cate_id, kw=kw, page=int(page))

    page_size = app.config["PAGE_SIZE"]
    total = dao.count_products()

    return render_template("index.html", categories=cates, products=prods, pages=math.ceil(total / page_size))


@app.route("/register")
def register_view():
    return render_template('layout/register.html')


if __name__ == "__main__":
    with app.app_context():
        app.run(debug=True)
