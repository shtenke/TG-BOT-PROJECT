import sqlite3


class CareerAdvisorBot:
    def __init__(self, db_name="career_bot.db"):
        self.db_name = db_name
        self.create_database()
        self.create_database_prof()

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

    def create_database_prof(self):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS careers (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    interest TEXT NOT NULL,
                    professions TEXT NOT NULL
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

    def get_user(self, user_id):
        """Получает информацию о пользователе"""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
            return cursor.fetchone()
    
    def populate_career_db(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        career_dict = {
            "программирование": "Разработчик ПО, Data Scientist, Инженер AI, Системный администратор, Разработчик игр, Мобильный разработчик, Тестировщик, DevOps-инженер, Frontend-разработчик, Backend-разработчик",
            "бизнес": "Предприниматель, Маркетолог, Финансовый аналитик, Бизнес-аналитик, Менеджер по продажам, HR-специалист, Руководитель проектов, Инвестиционный консультант, Экономист, Бренд-менеджер",
            "дизайн": "Графический дизайнер, UX/UI дизайнер, Иллюстратор, Модный дизайнер, Веб-дизайнер, 3D-дизайнер, Моушн-дизайнер, Архитектурный визуализатор, Арт-директор, Дизайнер интерьеров",
            "инженерия": "Инженер-конструктор, Электронщик, Архитектор, Механик, Инженер-механик, Авиаинженер, Нанотехнолог, Робототехник, Инженер-химик, Энергетик",
            "медицина": "Врач, Фармацевт, Медицинский исследователь, Хирург, Терапевт, Медсестра, Диетолог, Психиатр, Ветеринар, Лаборант",
            "гуманитарные науки": "Журналист, Писатель, Лингвист, Переводчик, Филолог, Историк, Культуролог, Социолог, Редактор, Сценарист",
            "образование": "Учитель, Преподаватель вуза, Педагог-психолог, Методист, Репетитор, Специалист по онлайн-обучению, Тренер по софт-скиллам",
            "искусство": "Художник, Скульптор, Арт-терапевт, Арт-директор, Продюсер, Флорист, Куратор выставок",
            "музыка": "Музыкант, Композитор, Актёр, Режиссёр, Диджей, Звукорежиссёр, Вокалист, Музыкальный педагог",
            "спорт": "Спортсмен, Тренер, Инструктор по йоге, Инструктор по фитнесу, Судья соревнований, Спортивный аналитик, Спортивный менеджер",
            "здоровье": "Физиотерапевт, Массажист, Диетолог, Консультант по ЗОЖ, Нутрициолог, Специалист по ЛФК",
            "право": "Юрист, Адвокат, Нотариус, Судья, Правовед, Юрисконсульт",
            "безопасность": "Следователь, Криминалист, Полицейский, Эксперт по безопасности, Специалист по охране труда, Сотрудник МЧС",
            "наука": "Физик, Химик, Биолог, Математик, Эколог, Астроном, Геолог, Исследователь, Лаборант, Научный сотрудник",
            "исследования": "Научный аналитик, Исследователь ИИ, Специалист по прикладным исследованиям",
            "туризм": "Туроператор, Гид, Менеджер по туризму, Экскурсовод, Туристический агент",
            "гостиничное дело": "Администратор отеля, Ресепшионист, Менеджер по бронированию, Менеджер по обслуживанию гостей",
            "логистика": "Логист, Диспетчер, Менеджер по цепям поставок, Планировщик маршрутов, Координатор доставки",
            "транспорт": "Водитель, Машинист, Моряк, Пилот, Автослесарь, Инженер по транспорту",
            "строительство": "Строитель, Каменщик, Электрик, Сантехник, Прораб, Инженер-строитель, Бетонщик, Плотник",
            "ремонт": "Слесарь, Отделочник, Мастер по ремонту, Техник по обслуживанию, Установщик окон",
            "сельское хозяйство": "Агроном, Зоотехник, Фермер, Ветеринар, Лесник, Специалист по агробизнесу",
            "it-менеджмент": "Менеджер IT-проектов, Продакт-менеджер, Технический директор (CTO), Аналитик данных, Agile-коуч"
        }

        for interest, professions in career_dict.items():
            cursor.execute('INSERT INTO careers (interest, professions) VALUES (?, ?)', (interest.lower(), professions))

        conn.commit()
        conn.close()
    
    def get_career_advice(self, interests):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT professions FROM careers WHERE interest = ?", (interests,))
            result = cursor.fetchone()
            return result[0] if result else "❌ По твоим интересам ничего не найдено."
        

if __name__ == "__main__":
    bot = CareerAdvisorBot()
    


