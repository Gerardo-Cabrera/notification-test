from flask import Blueprint, request, jsonify
from models.log import Log
from models.notification import Notification
from notifications.email import EmailNotification
from notifications.push import PushNotification
from notifications.sms import SmsNotification
from observers.category_observer import CategoryObserver
from observers.subject import Subject
from models.user import User
from datetime import datetime

notification_blueprint = Blueprint('notification', __name__)

@notification_blueprint.route('/notification', methods=['POST'])
def send_notification():
    data = request.get_json()
    print("data: ", data)
    category = data.get('category')
    message = data.get('message')

    if not category or not message:
        return jsonify({'message': 'Missing category or message'}), 400

    # Mock user data
    users = [
        User(user_id='1', name='Gerardo', email='gerardo@example.com', phone_number='6673596744', subscribed=['Sports', 'Finance'], channels=['E-Mail', 'SMS']),
        User(user_id='2', name='Johanna', email='johanna@example.com', phone_number='6673596745', subscribed=['Movies'], channels=['Push Notification']),
        User(user_id='3', name='Joel', email='joel@example.com', phone_number='6673596746', subscribed=['Sports', 'Movies', 'Finance'], channels=['SMS', 'E-Mail', 'Push Notification'])
    ]

    notification = Notification(category, message)

    subject = Subject()
    for user in users:
        if category in user.subscribed:
            subject.attach(CategoryObserver(category))

    for user in users:
        if category in user.subscribed:
            print(user.name)
            for channel in user.channels:
                if channel == 'E-Mail':
                    EmailNotification().notify(user, notification)
                elif channel == 'SMS':
                    SmsNotification().notify(user, notification)
                elif channel == 'Push Notification':
                    PushNotification().notify(user, notification)

                Log().add_log(user.user_id, user.name, category, channel, message, str(datetime.now()))

    return jsonify({'message': 'Notification sent successfully'}, 200)
