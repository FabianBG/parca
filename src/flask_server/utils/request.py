import json
import requests
from src.config import config

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def generate_request(model_name, payload):
    r = requests.post(config['TENSORFLOW_SERVE_URL'] + model_name, json=payload)
    return json.loads(r.content.decode('utf8').replace("'", '"'))
    