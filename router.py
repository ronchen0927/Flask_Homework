from app import app
from app.views.page import views
from flask import request
from flask_uploads import UploadSet, IMAGES, configure_uploads


photo = UploadSet(name='photo', extensions=IMAGES)
configure_uploads(app, photo)


@app.route('/', methods=['GET'])  # Index page
def index():
    return views.index()


@app.route('/upload', methods=['GET', 'POST'])  # Upload page
def upload(photo_url=None):
    if request.method == 'POST' and 'photo' in request.files:
        photo_name = photo.save(request.files['photo'])
        print(photo_name)
        photo_url = photo.url(photo_name)
        print(photo_url)

    return views.upload(photo_url)
