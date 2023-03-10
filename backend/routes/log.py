from flask import Blueprint, jsonify
from models.log import Log

log_blueprint = Blueprint('log', __name__)

@log_blueprint.route('/log', methods=['GET'])
def get_logs():
    log = Log()
    logs = log.get_logs()
    return jsonify(logs)
