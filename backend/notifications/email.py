from .channel import NotificationChannel

class EmailNotification(NotificationChannel):
    def notify(self, user, notification):
        print(f"Sending email notification to {user.email} for {notification.category} - {notification.message}")
