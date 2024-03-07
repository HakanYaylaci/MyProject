import time
from plyer import notification

def send_notification(title,message):
    notification.notify(
        title=title,
        message=message,
        timeout=10
    )

if __name__ =="__main__"   :
    title="Masaüstü Bildirim Uygulaması"
    message="Bu bir bildirim uygulamasıdır."

    send_notification(title,message)
