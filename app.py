import cv2
from flask import Flask,render_template,Response
app = Flask(__name__)
""""
cascade="haarcascade_frontalface_default.xml"
face_detect=cv2.CascadeClassifier(cascade)
"""
cap=cv2.VideoCapture(0)

def face_visu():
    while True:
        ret,frame=cap.read()
        frame=cv2.flip(frame,1)
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
      # face=face_detect.detectMultiScale(gray,1.1,4)
      
        """
        for (x,y,w,h) in face:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            pr=frame
            roi = gray[y:y+h,x:x+w]
        """
        rete, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/video_feed')
def video_feed():
    return Response(face_visu(), mimetype='multipart/x-mixed-replace; boundary=frame')
if __name__=='__main__':
    app.run(debug=True)