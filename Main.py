from flask import send_file
from flask import Flask
from flask_uploads import UploadSet, configure_uploads, IMAGES

app = Flask(__name__)
photos = UploadSet('photos', IMAGES)

app.config['UPLOADED_PHOTOS_DEST'] = 'img/'
configure_uploads(app, photos)

@app.route('/pressure_gauge')
def get_ressure_gauge():
    print("OK")
    return send_file('img/Einstein.jpg', mimetype='image/jpg')
    # return 'Saved as '
    # if request.method == 'GET':
    # if request.args == Utils.RESSURE_GAUGE_FIRST:
    # todo check if file is empty
    # todo save photo


if __name__ == '__main__':
    app.run(host='0.0.0.0	', port=5000, debug=True)
