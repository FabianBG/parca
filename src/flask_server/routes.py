from flask import Blueprint, flash, request, redirect, jsonify
from src.flask_server.utils.request import allowed_file, generate_request
from src.flask_server.models.mnist_fashion import decode_output, generate_input
import uuid
import os
from src.flask_server.utils.images import simple_image_handler

model_routes = Blueprint('model_routes', __name__)

@model_routes.route('/api', methods=['POST'])
def make_file_predict():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    if 'model' not in request.form:
        flash('No model definition')
        return redirect(request.url)
    file = request.files['file']
    print("Executing ::::::", request.form['model'])
    model = request.form['model']
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        path = os.path.join('./',  model + str(uuid.uuid1()))
        file.save(path)
        data = simple_image_handler(path, (96, 96))
        payload = generate_input(path, data)
        pred = generate_request(model, payload)
        os.remove(path)
        pretty_response = decode_output(pred['outputs'][0])
        print("Response ::::::", pred, pretty_response)
        return jsonify(pretty_response)
