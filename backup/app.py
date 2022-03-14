import os
from http import HTTPStatus
from flask import Flask, request, redirect, url_for, Response
from werkzeug.utils import secure_filename

# This app receive a file from a device that has `curl` command
#
# How to use:
# On PC: flask app.py --host 0.0.0.0
# On device: curl -v -F file=@backup.bin http://192.168.0.25:5000

UPLOAD_FOLDER = './backup'
ALLOWED_EXTENSIONS = {'bin', 'gz', 'bin.gz'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            return Response('No selected file.',HTTPStatus.NO_CONTENT)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            return Response('No selected file.',HTTPStatus.NO_CONTENT)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return Response('File received.',HTTPStatus.OK)