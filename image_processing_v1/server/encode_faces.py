import cv2
from pathlib import Path
import face_recognition
from imutils import paths
import pickle
import os

dataset_path = 'dataset'
detection_method = 'hog'
encodings_file = 'encodings/encodings.pickle'


def train_dataset():
    print("[INFO] quantifying faces...")
    imagePaths = list(paths.list_images('dataset'))
    knownEncodings = []
    knownNames = []
    # loop over the image paths
    for (i, imagePath) in enumerate(imagePaths):
        # extract the person name from the image path
        print("[INFO] processing image {}/{}".format(i + 1,
                                                     len(imagePaths)))
        name = imagePath.split(os.path.sep)[-2]
        # load the input image and convert it from BGR (OpenCV ordering)
        # to dlib ordering (RGB)
        image = cv2.imread(imagePath)
        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        # detect the (x, y)-coordinates of the bounding boxes
        # corresponding to each face in the input image
        boxes = face_recognition.face_locations(rgb,
                                                model=detection_method)
        # compute the facial embedding for the face
        encodings = face_recognition.face_encodings(rgb, boxes)
        # loop over the encodings
        for encoding in encodings:
            # add each encoding + name to our set of known names and
            # encodings
            knownEncodings.append(encoding)
            knownNames.append(name)
    # dump the facial encodings + names to disk
    print("[INFO] serializing encodings...")
    data = {"encodings": knownEncodings, "names": knownNames}
    f = open(encodings_file, "wb")
    f.write(pickle.dumps(data))
    f.close()
    return 'dataset is encoded'
