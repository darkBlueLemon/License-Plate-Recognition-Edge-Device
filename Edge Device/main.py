from requestUtil import RequestUtil
from ultralytics import YOLO
import cv2

request_util = RequestUtil(base_url='http://127.0.0.1:5000')

# load models
license_plate_detector = YOLO('./models/bestNew.pt')

# load video
cap = cv2.VideoCapture(4)

vehicles = [2, 3, 5, 7]

# read frames
frame_nmr = -1
ret = True
print("Started Camera")
while ret:
    frame_nmr += 1
    ret, frame = cap.read()
    if ret:

        # detect license plates
        license_plates = license_plate_detector(frame, verbose=False)[0]
        for license_plate in license_plates.boxes.data.tolist():
            x1, y1, x2, y2, score, class_id = license_plate
            if score < 0.5:
                continue

            license_plate_crop = frame[int(y1):int(y2), int(x1): int(x2), :]

            if license_plate_crop.size == 0:
                # print("Cropped image is empty")
                continue

            # process license plate
            license_plate_crop_gray = cv2.cvtColor(license_plate_crop, cv2.COLOR_BGR2GRAY)

            cv2.imwrite(f"./savedImages/{frame_nmr}.jpg", license_plate_crop_gray)
