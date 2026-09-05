from pynotifier import Notification, NotificationClient
from pynotifier.backends import platform
import psutil

battery = psutil.sensors_battery()

if battery is None:
    message = "No battery detected on this system."
else:
    message = f"Battery Percentage: {battery.percent}% remaining"

notification = Notification(title="Battery Status", message=message)

c = NotificationClient()
c.register_backend(platform.Backend())

try:
    c.notify_all(notification=notification)
except Exception as e:
    print("Notification failed:", e)
