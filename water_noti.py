from plyer import notification
import time

if __name__ == "__main__":
    while True:
        notification.notify(
            title="Please Drink Water!!",
            message="Health authorities commonly recommend eight 8-ounce glasses, which equals about 2 liters, "
                    "or half a gallon. This is called the 8×8 rule and is very easy to remember",
            app_icon='glass.ico',
            timeout=10
        )
        time.sleep(60)
    a=input()