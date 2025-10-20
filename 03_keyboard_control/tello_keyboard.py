from djitellopy import Tello
import cv2

tello = Tello()
tello.connect()

print(f"🔋 Batteria: {tello.get_battery()}%")

if tello.get_battery() > 20:
    tello.takeoff()
    try:
        while True:
            key = cv2.waitKey(1) & 0xFF
            if key == 27:  # ESC
                break
            elif key == ord('w'):
                tello.move_forward(30)
            elif key == ord('s'):
                tello.move_back(30)
            elif key == ord('a'):
                tello.move_left(30)
            elif key == ord('d'):
                tello.move_right(30)
            elif key == ord('e'):
                tello.rotate_clockwise(30)
            elif key == ord('q'):
                tello.rotate_counter_clockwise(30)
            elif key == ord('r'):
                tello.move_up(30)
            elif key == ord('f'):
                tello.move_down(30)
            elif key == ord('l'):
                tello.land()
                break
    finally:
        tello.land()
        cv2.destroyAllWindows()
else:
    print("⚠️ Batteria insufficiente")
