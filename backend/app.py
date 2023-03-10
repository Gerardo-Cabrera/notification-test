from flask import Flask, render_template
from flask_cors import CORS
from routes import notification_blueprint, log_blueprint

app = Flask(__name__)
CORS(app)

app.register_blueprint(notification_blueprint)
app.register_blueprint(log_blueprint)

@app.route('/')
def index():
    return render_template('index.html')
