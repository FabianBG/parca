from flask import Blueprint, flash, request, redirect, jsonify
from src.flask_server.utils.request import allowed_file, generate_request
from src.flask_server.models.ocr_plate import decode_batch, generate_input, __MODEL_NAME__
import uuid
import os

model_routes = Blueprint('model_routes', __name__)
version = '/v1/'


@model_routes.route(version + 'ocr_plate', methods=['POST'])
def ocr_plate_predict():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        path = os.path.join('./',  __MODEL_NAME__ + str(uuid.uuid1()))
        file.save(path)
        payload = generate_input(path)
        pred = generate_request(__MODEL_NAME__, payload)
        os.remove(path)
        return jsonify(decode_batch(pred['outputs']))
