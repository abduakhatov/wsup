from flask import send_file
from flask import Flask, render_template, request
from flask_uploads import UploadSet, configure_uploads, IMAGES
import os
from utils import Utils
import sys
import numpy as np



app = Flask(__name__)
photos = UploadSet('photos', IMAGES)

app.config['UPLOADED_PHOTOS_DEST'] = 'saved/'
configure_uploads(app, photos)


@app.route('/training', methods=['GET', 'POST'])
def train():
     if request.method == 'POST' and 'photo' in request.files:
         # image_id = request.form['image_id']
         filename = photos.save(request.files['photo'])
         face_encodings = face_recognition.face_encodings(face_recognition.load_image_file(request.files['photo']))
         if len(face_encodings) == 0:
             return "Cannot find a face"
         known_face_encodings.append(
             face_recognition.face_encodings(face_recognition.load_image_file(request.files['photo']))[0])
         known_face_names.append(filename[:-4])
         return 'Saved as ' + filename
     return render_template('./flask.html')


@app.route('/pressure_gauge')
def get_ressure_gauge():
    print("OK")
    return send_file('saved/Einstein.jpg', mimetype='image/jpg' )
    #return 'Saved as '
	#if request.method == 'GET':
	#if request.args == Utils.RESSURE_GAUGE_FIRST:
	# todo check if file is empty
	# todo save photo


@app.route('/pressure_gauge')
def pressure_gauge():
	print(request.headers)
	#if request.method == 'POST' and 'photo' in request.files:
	#	#print("asdasd")
        #	return "upload"
	return "OK" 

if __name__ == '__main__':
    app.run(host = '0.0.0.0	', port = 5000, debug=True)

