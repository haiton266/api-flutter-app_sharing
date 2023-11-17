from library.extension import db
from library.library_ma import FeedbackSchema
from library.model import Feedback_data
from flask import request, jsonify, json

total_schema = FeedbackSchema()
feedbacks_schema = FeedbackSchema(many=True)


def add_feedback_data_service():
    data = request.json
    if (('content' in data) and ('username' in data) and ('id_pdf' in data)):
        content = data['content']
        username = data['username']
        id_pdf = data['id_pdf']
        try:
            new_feedback_data = Feedback_data(
                content, username, id_pdf)
            db.session.add(new_feedback_data)
            db.session.commit()
            return jsonify({"message": "Add success!"}), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({"message": "Cannot add data", "error": str(e)}), 400
    else:
        return jsonify({"message": "Request error"}), 400


def get_all_feedback_data_service():
    totals_data = Feedback_data.query.all()
    if totals_data:
        return feedbacks_schema.jsonify(totals_data)
    else:
        return jsonify({"message": "Not found sensors_data!"})


def get_pdf_feedback_data_service(id_pdf):
    totals_data = Feedback_data.query.filter_by(id_pdf=id_pdf)
    if totals_data:
        return feedbacks_schema.jsonify(totals_data)
    else:
        return jsonify({"message": "Not found sensors_data!"})


def update_feedback_data_by_id_service(id):
    price = Feedback_data.query.get(id)
    if price:
        data = request.json
        if (data and ("content" in data) and ('username' in data) and ('id_pdf' in data)):
            try:
                price.content = data['content']
                price.username = data['username']
                price.id_pdf = data['id_pdf']
                db.session.commit()
                return jsonify({"message": "Feedback updated successfully"})
            except Exception as e:
                db.session.rollback()
                return jsonify({"message": "Cannot update Feedback!", "error": str(e)}), 400
    else:
        return jsonify({"message": "Not found Feedback!"}), 404


def delete_feedback_data_by_id_service(id):
    price = Feedback_data.query.get(id)
    if price:
        try:
            db.session.delete(price)
            db.session.commit()
            return jsonify({"message": "Feedback deleted successfully"})
        except Exception as e:
            db.session.rollback()
            return jsonify({"message": "Cannot delete feedback!", "error": str(e)}), 400
    else:
        return jsonify({"message": "Not found feedback!"}), 404
