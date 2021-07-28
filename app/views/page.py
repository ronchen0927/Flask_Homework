from flask import render_template


class views:
    def index():
        return render_template('pages/index.html')

    def upload(photo_url):
        return render_template('pages/upload.html', photo_url=photo_url)
