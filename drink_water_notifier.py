from plyer import notification

if __name__=="__main__":
    notification.notify(
        title= "Please Drink Water",
        message= "Water is very important for Life. Its time to drink a glass of water. Go and drink water right now",
        app_icon="D:\Python\Apps\RelaxEyesNotification\glass.ico",
        timeout= 10
    )