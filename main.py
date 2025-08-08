import numpy
import cv2
import imutils
import csv
from datetime import datetime

log_file = open("log.csv", mode="a", newline="")
log_writer = csv.writer(log_file)


gunCascade = cv2.CascadeClassifier("cascade.xml")

if gunCascade.empty():
    print("Cannot find cascade.xml")
    print("Make sure it is in the same folder as the code.")
    exit()

camera = cv2.VideoCapture(0)

firstFrame = None
gunExist = None

while True:
    ret, frame = camera.read()

    if not ret or frame is None:
        print(" Failed to grab frame")
        break

    frame = imutils.resize(frame, width=500)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    gun = gunCascade.detectMultiScale(gray, 1.3, 5, minSize=(100, 100))

    if len(gun) > 0:
        gunExist = True

    for x, y, w, h in gun:
        frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roiGray = gray[y : y + h, x : x + w]
        roiColor = frame[y : y + h, x : x + w]

    if firstFrame is None:
        firstFrame = gray
        continue

    cv2.imshow("Security feed", frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break   

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

if gunExist:
    print(f"[{timestamp}]  Gun detected!")
    log_writer.writerow([timestamp, "Gun Detected"])
else:
    print(f"[{timestamp}]  No gun detected.")
    log_writer.writerow([timestamp, "No Gun"])





camera.release()
cv2.destroyAllWindows()
