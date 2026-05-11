from flask import Flask, render_template, request, redirect, url_for, Response
import cv2
import os
import face_recognition

app = Flask(__name__)

DATABASE_PATH = 'database/'
os.makedirs(DATABASE_PATH, exist_ok=True)

known_encodings = []
known_names = []


def load_users():
    known_encodings.clear()
    known_names.clear()

    for file in os.listdir(DATABASE_PATH):
        if file.endswith(".png"):
            image_path = os.path.join(DATABASE_PATH, file)
            image = face_recognition.load_image_file(image_path)

            encodings = face_recognition.face_encodings(image)

            if len(encodings) > 0:
                known_encodings.append(encodings[0])
                known_names.append(file.split('.')[0])

load_users()


camera = None
running = False



def generate_frames():
    global camera, running

    while running:

        success, frame = camera.read()
        if not success:
            break

        # Resize for speed
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = small_frame[:, :, ::-1]

        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        door_status = "Access Denied - Unknown Person"

        for face_encoding in face_encodings:

            matches = face_recognition.compare_faces(known_encodings, face_encoding)

            name = "Unknown"

            if True in matches:
                first_match_index = matches.index(True)
                name = known_names[first_match_index]
                door_status = "Access Granted"

            for (top, right, bottom, left) in face_locations:

                top *= 4
                right *= 4
                bottom *= 4
                left *= 4

                color = (0,255,0) if name != "Unknown" else (0,120,255)

                cv2.rectangle(frame,(left,top),(right,bottom),color,2)

                cv2.rectangle(frame,(left,bottom-35),(right,bottom),color,cv2.FILLED)

                cv2.putText(frame,name,(left+6,bottom-6),
                            cv2.FONT_HERSHEY_DUPLEX,1,(200,155,105),1)

        cv2.putText(frame,
                    door_status,
                    (50,50),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0,255,0) if door_status=="Access Granted" else (0,120,255),
                    2)

        ret, buffer = cv2.imencode('.jpg', frame)

        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')




@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/process')
def process():
    return render_template('process.html')



@app.route('/create_database', methods=['GET','POST'])
def create_database():

    if request.method == 'POST':

        name = request.form['name']
        phone = request.form['phone']
        image = request.files['image']

        if image:

            filepath = os.path.join(DATABASE_PATH, f"{name}.png")
            image.save(filepath)

            new_image = face_recognition.load_image_file(filepath)

            encodings = face_recognition.face_encodings(new_image)

            if len(encodings) > 0:

                known_encodings.append(encodings[0])
                known_names.append(name)

                load_users()

        return redirect(url_for('process'))

    return render_template('create_database.html')



@app.route('/start_detection')
def start_detection():

    global camera, running

    if not running:
        camera = cv2.VideoCapture(0)
        running = True

    return redirect(url_for('detection'))


@app.route('/detection')
def detection():
    return render_template('detection.html')


@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/stop_detection')
def stop_detection():

    global running, camera

    running = False

    if camera is not None:
        camera.release()
        camera = None

    return redirect(url_for('process'))



if __name__ == '__main__':
    app.run(debug=True)
