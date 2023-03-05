from win10toast import ToastNotifier
import time
import os
toast = ToastNotifier()
toast.show_toast(
    "Notification",
    "Notification body",
    duration = 1,
    icon_path = "icon file path here",
    threaded = True,
)
time.sleep(1)
os._exit(1)
