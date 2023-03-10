from .channel import NotificationChannel

class PushNotification(NotificationChannel):
    def notify(self, user, notification):
        print(f"Sending push notification to {user.user_id} for {notification.category} - {notification.message}")
