import cv2
import controller as cnt
from cvzone.HandTrackingModule import HandDetector

detector = HandDetector(detectionCon=0.8, maxHands=1)
video = cv2.VideoCapture(0)

while True:
    ret, frame = video.read()
    frame = cv2.flip(frame, 1)
    hands, img = detector.findHands(frame)

    if hands:
        lmList = hands[0]
        fingerUp = detector.fingersUp(lmList)

        print(fingerUp)
        cnt.led(fingerUp)  # Controls each LED according to each finger

        # Optional: Display finger status
        labels = ["Thumb", "Index", "Middle", "Ring", "Pinky"]
        for i, (up, label) in enumerate(zip(fingerUp, labels)):
            color = (0, 255, 0) if up else (0, 0, 255)
            cv2.putText(frame, f"{label}: {'Up' if up else 'Down'}",
                        (20, 100 + i * 40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

    cv2.imshow("frame", frame)
    k = cv2.waitKey(1)
    if k == ord("k"):
        break

video.release()
cv2.destroyAllWindows()
