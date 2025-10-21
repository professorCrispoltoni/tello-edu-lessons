from djitellopy import Tello
import cv2

tello = Tello()
tello.connect()
tello.streamon()
frame_reader = tello.get_frame_read()

while True:
    img = frame_reader.frame
    cv2.imshow("drone", img)
    if cv2.waitKey(1) & 0xff == 27:  # ESC per uscire
        break

cv2.destroyAllWindows()
tello.streamoff()
