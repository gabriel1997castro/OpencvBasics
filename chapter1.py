import cv2
print("Package imported")

# -------------- Show images
# img = cv2.imread('resources/test_img.png')
#
# cv2.imshow("Output", img)
# cv2.waitKey(0)

# -------------- Videos
# cap = cv2.VideoCapture('resources/test_video.mp4')
#
# while True:
#     success, img = cap.read()
#     cv2.imshow("Video", img)
#     if cv2.waitKey(2) & 0xFF == ord('q'):
#         break

# ------------ WEBCAM
VIDEO_WIDTH = 3
VIDEO_HEIGHT = 4
VIDEO_BRIGHTNESS = 10

cap = cv2.VideoCapture(0)
cap.set(VIDEO_WIDTH, 640)
cap.set(VIDEO_HEIGHT, 480)
cap.set(VIDEO_BRIGHTNESS, 100)

while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break