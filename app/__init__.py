from flask import Flask
app = Flask(__name__)

UPLOAD_FOLDER = 'app/static/photo/'

app.config['SECRET_KEY'] = 'development'
app.config['UPLOADED_PHOTO_DEST'] = UPLOAD_FOLDER
app.config['UPLOADED_PHOTO_URL'] = 'static/photo/'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
