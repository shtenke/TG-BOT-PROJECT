import sqlite3


class CareerAdvisorBot:
    def __init__(self, db_name="career_bot.db"):
        self.db_name = db_name
        self.create_database()

    def create_database(self):
        """Создает таблицу пользователей и предпочтений, если она не существует"""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER UNIQUE,
                    name TEXT,
                    age INTEGER,
                    interests TEXT
                )
            ''')
            conn.commit()

    def add_user(self, user_id, name, age, interests):
        """Добавляет нового пользователя в базу данных"""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT OR REPLACE INTO users (user_id, name, age, interests) 
                VALUES (?, ?, ?, ?)''', (user_id, name, age, interests))
            conn.commit()

    def get_user(self, name):
        """Получает информацию о пользователе"""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE name = ?", (name,))
            return cursor.fetchone()
        
if __name__ == "__main__":
    bot = CareerAdvisorBot()
    bot.get_user('kostya')