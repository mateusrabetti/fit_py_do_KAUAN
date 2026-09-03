import sqlite3
from database.db import get_db_connection

class UserModel:
    @staticmethod
    def find_by_username(username):
        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE username = ?', )
        conn.close()
        return user
    
    @staticmethod
    def create_user(username, password):