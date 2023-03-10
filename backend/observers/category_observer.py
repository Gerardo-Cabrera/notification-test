class CategoryObserver:
    def __init__(self, category):
        self.category = category

    def update(self, user, notification, channel):
        if self.category in user.subscribed and channel in user.channels:
            channel.notify(user, notification)
