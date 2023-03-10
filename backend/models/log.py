import logging
import sqlite3


class Log:
    def __init__(self, log_file='notifications.log', db_file='notifications.db'):
        self.logger = logging.getLogger(__name__)
        self.log_file = log_file
        self.db_file = db_file
        self.db_conn = sqlite3.connect(db_file)
        self.db_cursor = self.db_conn.cursor()
        
        self.db_cursor.execute('''
            CREATE TABLE IF NOT EXISTS logs (
                id INTEGER PRIMARY KEY,
                user_id INTEGER,
                user_name TEXT,
                category TEXT,
                channel TEXT,
                message TEXT,
                timestamp TEXT
            )
        ''')
        self.db_conn.commit()

    def add_log(self, user_id, user_name, category, channel, message, timestamp):
        try:
            if not user_id or not user_name or not category or not channel or not message:
                self.logger.error('Invalid input data: {}, {}, {}, {}, {}'.format(user_id, user_name, category, channel, message))
                return

            with open(self.log_file, 'a') as f:
                f.write('{}\t{}\t{}\t{}\t{}\t{}\n'.format(user_id, user_name, category, channel, message, timestamp))

            self.db_cursor.execute('''
                INSERT INTO logs (user_id, user_name, category, channel, message, timestamp)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (user_id, user_name, category, channel, message, timestamp))
            self.db_conn.commit()

            self.logger.info('Added log: {}, {}, {}, {}, {}, {}'.format(user_id, user_name, category, channel, message, timestamp))
        except Exception as e:
            print(f'Error adding log: {e}')

    def get_logs(self):
        self.db_cursor.execute('SELECT * FROM logs ORDER BY timestamp DESC')
        rows = self.db_cursor.fetchall()

        logs = []

        for row in rows:
            logs.append({
                'id': row[0],
                'user_id': row[1],
                'user_name': row[2],
                'category': row[3],
                'channel': row[4],
                'message': row[5],
                'timestamp': row[6]
            })

        return logs
