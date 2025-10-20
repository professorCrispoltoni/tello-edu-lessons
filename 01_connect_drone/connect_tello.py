from djitellopy import Tello

tello = Tello()
tello.connect()
print(f"🔋 Batteria: {tello.get_battery()}%")
tello.end()
