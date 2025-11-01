import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title="ALERT !!!",
            message="Take a break! It has been an hour!",
            timeout=10  # Notification stays for 10 seconds
        )
        time.sleep(3600)  # Wait for 1 hour (3600 seconds)
