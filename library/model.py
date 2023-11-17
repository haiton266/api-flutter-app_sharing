from library.extension import db
from flask_jwt_extended import get_jwt_identity
import json


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(20), nullable=False)
    address = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(50), nullable=False)

    def __init__(self, email, username, password, address, phone):
        self.email = email
        self.username = username
        self.password = password
        self.address = address
        self.phone = phone
# thêm address,phone


class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), nullable=False)
    adminname = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(20), nullable=False)

    def __init__(self, email, adminname, password):
        self.email = email
        self.adminname = adminname
        self.password = password


class Total_price(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    men_price = db.Column(db.Integer, nullable=False)
    women_price = db.Column(db.Integer, nullable=False)
    men_product = db.Column(db.Integer, nullable=False)
    women_product = db.Column(db.Integer, nullable=False)
    label = db.Column(db.String(50), nullable=False)

    def __init__(self, men_price, women_price, men_product, women_product, label):
        self.men_price = men_price
        self.women_price = women_price
        self.men_product = men_product
        self.women_product = women_product
        self.label = label


class Feedback_data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(500), nullable=False)
    username = db.Column(db.String(50), nullable=False)
    id_pdf = db.Column(db.Integer, nullable=False)

    def __init__(self, content, username, id_pdf):
        self.content = content
        self.username = username
        self.id_pdf = id_pdf


class Customer_data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    phone_ct = db.Column(db.String(50), nullable=False)
    email_ct = db.Column(db.String(50), nullable=False)
    user_ct = db.Column(db.String(50), nullable=False)
    mess_ct = db.Column(db.String(500), nullable=False)
    address_ct = db.Column(db.String(50), nullable=False)
    # bỏ pass_ct

    def __init__(self, phone_ct, email_ct, user_ct, mess_ct, address_ct):
        self.phone_ct = phone_ct
        self.email_ct = email_ct
        self.user_ct = user_ct
        self.mess_ct = mess_ct
        self.address_ct = address_ct


class Image_data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pdf_url = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    type = db.Column(db.String(255), nullable=False)
    school = db.Column(db.String(255), nullable=False)

    def __init__(self, pdf_url, school, name, type):
        self.pdf_url = pdf_url
        self.school = school
        self.name = name
        self.type = type
