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


class Feedback_data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(500), nullable=False)
    username = db.Column(db.String(50), nullable=False)
    id_pdf = db.Column(db.Integer, nullable=False)

    def __init__(self, content, username, id_pdf):
        self.content = content
        self.username = username
        self.id_pdf = id_pdf


class Image_data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pdf_url = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    type = db.Column(db.String(255), nullable=False)
    school = db.Column(db.String(255), nullable=False)
    username = db.Column(db.String(255), nullable=False)

    def __init__(self, pdf_url, name, type, school, username):
        self.pdf_url = pdf_url
        self.school = school
        self.name = name
        self.type = type
        self.username = username
