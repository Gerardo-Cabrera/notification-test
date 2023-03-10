class Subject:
    def __init__(self):
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self, user, notification, channel):
        for observer in self.observers:
            if observer.category == notification.category:
                observer.update(user, notification, channel)
