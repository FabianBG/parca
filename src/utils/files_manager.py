import os
from src.types import ModelFolder
from src.config import config
import shutil
import json
 

def read_models_dirs():
    output = []
    for directory in os.listdir(config['MODEL_FOLDER']):
        if directory.endswith(config['MODEL_SUFIX']):
            model_dir = os.path.join(config['MODEL_FOLDER'], directory)
            model_data = ModelFolder(model_dir)
            for version in os.listdir(model_dir):
                model_data.addVersion(version)
            output.append(model_data)
    return output

def add_model_dir(source_path, model_name):
    model_name = model_name + '.' + config['MODEL_SUFIX']
    model_dir = os.path.join(config['MODEL_FOLDER'], model_name)
    if os.path.isdir(model_dir):
        version_size = len(os.listdir(model_dir))
    else:
        version_size = 0
    copy_dir(source_path, os.path.join(model_dir, str(version_size + 1)))


def generate_model_config(path_folder=None):
    output = []
    proto_file = 'model_config_list: {{confs}}'
    conf = ''
    conf_text = 'config: {name: "{name}", base_path: "{base}", model_platform: "tensorflow"}'
    for model in read_models_dirs():
        conf = conf + conf_text.replace('{name}', model.name)
        if path_folder is None: conf = conf.replace('{base}', model.path)
        else: conf = conf.replace('{base}', os.path.join(path_folder, model.name))
        conf = conf + ','
    with open(os.path.join(config['MODEL_FOLDER'], 'models.conf'), 'w') as config_file:
        config_file.write(proto_file.replace('{confs}', conf))



def copy_dir(src, dest):
    print('From', src, 'to', dest)
    try:
        shutil.copytree(src, dest)
    except shutil.Error as e:
        print('Directory not copied. Error: %s' % e)
    except OSError as e:
        print('Directory not copied. Error: %s' % e)
