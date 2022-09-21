import cv2
from pathlib import Path
import random
import math
import face_recognition
from imutils import paths
import os
import pickle

# Initially Count is = 1
count = 6
temp_id = ''
# detection_method = 'hog'
# encodings_file = 'encodings/encodings.pickle'
# data = pickle.loads(open(encodings_file, "rb").read())


def gen_frames():
    camera = cv2.VideoCapture(0)
    detection_method = 'hog'
    encodings_file = 'encodings/encodings.pickle'
    data = pickle.loads(open(encodings_file, "rb").read())
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    while True:
        success, frame = camera.read()  # read the camera frame
        if not success:
            break
        else:
            original_img = frame.copy()
            gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            faces = faceCascade.detectMultiScale(gray_img,
                                                 scaleFactor=1.2,
                                                 minNeighbors=5,
                                                 minSize=(50, 50))

            # for (x, y, w, h) in faces:
            #     cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # print("[INFO] recognizing faces...")
            boxes = face_recognition.face_locations(rgb,
                                                    model=detection_method)
            encodings = face_recognition.face_encodings(rgb, boxes)
            names = []
            # loop over the facial embeddings
            for encoding in encodings:
                # attempt to match each face in the input image to our known
                # encodings
                matches = face_recognition.compare_faces(data["encodings"],
                                                         encoding)
                name = "Unknown"
                if True in matches:
                    # find the indexes of all matched faces then initialize a
                    # dictionary to count the total number of times each face
                    # was matched
                    matchedIdxs = [i for (i, b) in enumerate(matches) if b]
                    counts = {}
                    # loop over the matched indexes and maintain a count for
                    # each recognized face face
                    for i in matchedIdxs:
                        name = data["names"][i]
                        counts[name] = counts.get(name, 0) + 1
                    # determine the recognized face with the largest number of
                    # votes (note: in the event of an unlikely tie Python will
                    # select first entry in the dictionary)
                    name = max(counts, key=counts.get)

                # update the list of names
                names.append(name)

                if len(names) > 1:
                    print('Multiple people detected')
                elif len(names) > 0:
                    print(f"Detected person is {names[0]}")
                elif len(faces) > 0:
                    print('Identified unknown faces')
                else:
                    print('No face detected')

            # loop over the recognized faces
            for ((top, right, bottom, left), name) in zip(boxes, names):
                # draw the predicted face name on the image
                cv2.rectangle(frame, (left, top),
                              (right, bottom), (0, 255, 0), 2)
                y = top - 15 if top - 15 > 15 else top + 15
                cv2.putText(frame, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX,
                            0.75, (0, 255, 0), 2)

            global count, temp_id
            if len(faces) == 1 and getCount() <= 5:
                temp_id = temp_id if temp_id != '' else getId()
                saveImage(original_img, temp_id)
                count = count + 1

            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result

# Function to save the image


def saveImage(image, id):
    # Create a folder with the name as userName
    Path("temp_dataset/{}".format(id)).mkdir(parents=True, exist_ok=True)
    # Save the images inside the previously created folder
    cv2.imwrite("temp_dataset/{}/{}_{}.jpg".format(id, id, count), image)
    print("[INFO] Image has been saved in folder : {}".format(
        id))


def getId():
    digits = [i for i in range(0, 10)]
    random_str = ""
    for i in range(6):
        # generating a random index
        # if we multiply with 10 it will generate a number between 0 and 10 not including 10
        # multiply the random.random() with length of your base list or str
        index = math.floor(random.random() * 10)
        random_str += str(digits[index])
    return random_str


def getCount():
    global count
    return count


def getTempId():
    global temp_id
    return temp_id


def record_dataset():
    print('Inside record dataset')
    global count, temp_id
    count = 1
    temp_id = ''
    while getCount() < 5:
        z = 0
    return f"{getTempId()}"
