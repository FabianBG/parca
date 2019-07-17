docker run -t --rm -d -p 8501:8501 \
    -v "/Users/mbastidas/code/parca/models/:/models/" \
    tensorflow/serving --model_config_file=/models/models.conf