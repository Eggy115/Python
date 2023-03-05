import screen_brightness_control as sbc
while(True):
    a = input("Enter Brightness: ")
    try:
        sbc.set_brightness(a)
        print(f"Brightness set to {a}")
    except:
        print(f"Brightness could not be set to {a}")
