from flask import request, jsonify
import os
import time
from library.model import Image_data
from library.extension import db
from library.library_ma import Image_dataSchema

image_schema = Image_dataSchema()
images_schema = Image_dataSchema(many=True)


def add_image_service():
    if 'image' not in request.files:
        return jsonify({"message": "No file"}), 400

    img_file = request.files['image']
    image_path = 'static/'

    if img_file.filename == '':
        return jsonify({"message": "No selected image or img_hover"}), 400

    if not os.path.exists(image_path):
        os.makedirs(image_path)

    name_image = str(int(time.time())) + '.pdf'
    img_path = os.path.join(image_path, name_image)
    img_file.save(img_path)

    pdf_url = "http://127.0.0.1:5000/static/" + name_image
    name = request.form.get('name')
    type = request.form.get('type')
    school = request.form.get('school')
    try:
        new_image_data = Image_data(
            pdf_url, name, type, school)
        db.session.add(new_image_data)
        db.session.commit()
        return jsonify({"message": "Upload image successful!"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": "Cannot add data", "error": str(e)}), 400


def update_image_service(image_id):
    # Trích xuất dữ liệu từ yêu cầu
    data = request.json

    try:
        # Tìm hình ảnh cần sửa theo image_id
        image_data = Image_data.query.get(image_id)

        if not image_data:
            return jsonify({"message": "Image not found"}), 404

        # Cập nhật thông tin hình ảnh
        if 'rating' in data:
            image_data.rating = data['rating']

        db.session.commit()
        return jsonify({"message": "Image updated successfully"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": "Cannot update image", "error": str(e)}), 400


def delete_image_service(image_id):
    try:
        # Tìm hình ảnh cần xóa theo image_id
        image_data = Image_data.query.get(image_id)

        if not image_data:
            return jsonify({"message": "Image not found"}), 404

        # Xóa hình ảnh và lưu thay đổi vào cơ sở dữ liệu
        db.session.delete(image_data)
        db.session.commit()

        return jsonify({"message": "Image deleted successfully"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": "Cannot delete image", "error": str(e)}), 400


def get_all_image_service():
    images = Image_data.query.all()
    if images:
        return images_schema.jsonify(images)
    else:
        return jsonify({"message": "Not found url!"})


def get_latest_images_service():
    # Lấy 10 bản ghi mới nhất
    images = Image_data.query.order_by(Image_data.id.desc()).limit(10).all()

    # Serialize các bản ghi thành định dạng JSON và trả về
    if images:
        return images_schema.jsonify(images)
    else:
        return jsonify({"message": "Not found url!"})
