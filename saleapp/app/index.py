# from doctest import debug
import math

from flask import render_template, request, redirect, session, jsonify
import dao, utils
from app import app, login
from flask_login import login_user, logout_user
from app.models import UserRole


@app.route("/")
def index():

    page = request.args.get('page', 1)
    cate_id = request.args.get('category_id')
    kw = request.args.get('kw')
    prods = dao.load_products(cate_id=cate_id, kw=kw, page=int(page))

    page_size = app.config["PAGE_SIZE"]
    total = dao.count_products()

    return render_template("index.html", products=prods, pages=math.ceil(total / page_size))


@app.route("/register", methods=['get', 'post'])
def register_view():
    err_msg = ''
    if request.method.__eq__('POST'):
        password = request.form.get('password')
        confirm = request.form.get('confirm')

        if not password.__eq__(confirm):
            err_msg = 'Mật khẩu không khớp!!!'
        else:
            data = request.form.copy()

            del data['confirm']
            avatar = request.files.get('avatar')
            dao.add_user(avatar=avatar, **data)
            return redirect('/login')

    return render_template('layout/register.html', err_msg=err_msg)


@app.route("/api/carts", methods=['post'])
def add_to_cart():
    # {
    #     "1":{
    #         "id": 1,
    #         "name": "iphone",
    #         "price": 123,
    #         "quantity": 2
    #     }, "2":{
    #     "id": 2,
    #     "name": "iphone",
    #     "price": 123,
    #     "quantity": 2
    # }
    # }
    cart = session.get('cart')
    if not cart:
        cart = {}

    print(request.json)
    id = str(request.json.get('id'))
    name = request.json.get('name')
    price = request.json.get('price')

    if id in cart:
        cart[id]['quantity'] = cart[id]['quantity'] + 1
    else:
        cart[id] = {
            "id": id,
            "name": name,
            "price": price,
            "quantity": 1
        }

    session['cart'] = cart

    print(cart)

    return jsonify(utils.cart_stats(cart))

@app.route("/login", methods=['get', 'post'])
def login_view():
    if request.method.__eq__('POST'):
        username = request.form.get('username')
        password = request.form.get('password')
        user = dao.auth_user(username=username, password=password)
        if user:
            login_user(user=user)
            return redirect('/')

    return render_template('layout/login.html')


@app.route("/login-admin", methods=['post'])
def login_admin_view():
    username = request.form.get('username')
    password = request.form.get('password')

    user = dao.auth_user(username=username, password=password, role=UserRole.ADMIN)
    if user:
        login_user(user=user)
    return redirect('/admin')


@app.route("/logout")
def logout_process():
    logout_user()
    return redirect('/login')

@app.route('/cart')
def cart_view():
    return render_template('layout/cart.html')

@login.user_loader
def load_user(user_id):
    return dao.get_user_by_id(user_id)

@app.context_processor
def common_response_data():
    return {
        'categories': dao.load_categories(),
        'cart_stats': utils.cart_stats(session.get('cart'))
    }

if __name__ == "__main__":
    with app.app_context():
        from app import admin

        app.run(debug=True)
