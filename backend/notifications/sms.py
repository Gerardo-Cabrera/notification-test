from .channel import NotificationChannel

class SmsNotification(NotificationChannel):
    def notify(self, user, notification):
        print(f"Sending SMS notification to {user.phone_number} for {notification.category} - {notification.message}")
