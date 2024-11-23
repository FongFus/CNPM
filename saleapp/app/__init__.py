from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote
import cloudinary
from flask_login import LoginManager

app = Flask(__name__)

app.secret_key = 'HGHJAHA^&^&*AJAVAHJ*^&^&*%&*^GAFGFAG'
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:%s@localhost/saledb?charset=utf8mb4" % quote(
    "Admin@123")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["PAGE_SIZE"] = 4

db = SQLAlchemy(app)

cloudinary.config(cloud_name='dncgine9e',
                  api_key='257557947612624',
                  api_secret='88EDQ7-Ltwzn1oaI4tT_UIb_bWI')

login = LoginManager(app)
