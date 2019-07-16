docker run -t --rm -p 8501:8501 \
    -v "/Users/latam/code/parca/models/:/models/" \
    tensorflow/serving --model_config_file=/models/models.conf