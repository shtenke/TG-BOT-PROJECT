import sqlite3


class CareerAdvisorBot:
    def __init__(self, db_name="career_bot.db"):
        self.db_name = db_name
        self.create_database()
        self.create_database_prof()
        self.create_database_prof_desc()

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


    def create_database_prof_desc(self):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS careers_desc (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    professions TEXT NOT NULL,
                    description TEXT NOT NULL
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
        }
        career_descriptions = {
            "Разработчик ПО": "Разрабатывает и поддерживает программное обеспечение для различных платформ.",
            "Data Scientist": "Анализирует большие объемы данных для выявления закономерностей и создания моделей.",
            "Инженер AI": "Разрабатывает системы искусственного интеллекта и машинного обучения.",
            "Системный администратор": "Отвечает за настройку, управление и поддержку компьютерных систем и серверов.",
            "Разработчик игр": "Создаёт компьютерные игры, включая их проектирование и программирование.",
            "Мобильный разработчик": "Создаёт приложения для мобильных устройств на платформы iOS и Android.",
            "Тестировщик": "Проводит тестирование программного обеспечения для поиска ошибок и улучшения качества.",
            "DevOps-инженер": "Разрабатывает процессы автоматизации для разработки и эксплуатации приложений.",
            "Frontend-разработчик": "Отвечает за визуальную часть веб-приложений, взаимодействие с пользователем.",
            "Backend-разработчик": "Создаёт серверную часть веб-приложений, работу с базами данных и серверными системами.",
            "Предприниматель": "Создаёт и управляет собственным бизнесом, принимая стратегические решения.",
            "Маркетолог": "Изучает рынок и разрабатывает стратегии продвижения товаров и услуг.",
            "Финансовый аналитик": "Анализирует финансовые данные компании для принятия инвестиционных решений.",
            "Бизнес-аналитик": "Оценивает бизнес-процессы и разрабатывает рекомендации для их оптимизации.",
            "Менеджер по продажам": "Организует и управляет процессом продажи товаров или услуг.",
            "HR-специалист": "Занимается подбором, обучением и развитием персонала компании.",
            "Руководитель проектов": "Организует и управляет проектами, контролирует их реализацию.",
            "Инвестиционный консультант": "Оказывает консультационные услуги по инвестированию в различные активы.",
            "Экономист": "Изучает экономические процессы и разрабатывает рекомендации для улучшения бизнеса.",
            "Бренд-менеджер": "Управляет имиджем и стратегией бренда на рынке.",
            "Графический дизайнер": "Создаёт визуальные элементы для различных типов медиа, таких как логотипы, рекламные материалы.",
            "UX/UI дизайнер": "Проектирует интерфейсы для обеспечения удобства пользователей в цифровых продуктах.",
            "Иллюстратор": "Создаёт рисунки и графику для книг, журналов, рекламных материалов и других медиа.",
            "Модный дизайнер": "Разрабатывает новые коллекции одежды, учитывая тренды и эстетические предпочтения.",
            "Веб-дизайнер": "Проектирует визуальные элементы веб-сайтов и интернет-ресурсов.",
            "3D-дизайнер": "Создаёт трёхмерные модели и анимации для различных проектов, включая игры и кино.",
            "Моушн-дизайнер": "Разрабатывает анимационные элементы для видео, рекламы и других медиа.",
            "Архитектурный визуализатор": "Создаёт фотореалистичные изображения зданий и интерьеров.",
            "Арт-директор": "Руководит процессом создания визуального контента, координирует работу дизайнеров.",
            "Дизайнер интерьеров": "Проектирует оформление и функциональные особенности внутренних пространств."
        }

        for interest, professions in career_dict.items():
            cursor.execute('INSERT INTO careers (interest, professions) VALUES (?, ?)', (interest.lower(), professions))
        for profession, description in career_descriptions.items():
            cursor.execute('INSERT INTO careers_desc (professions,description) VALUES (?, ?)', (profession, description))
        conn.commit()
        conn.close()
    
    def get_career_advice(self, interests):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT professions FROM careers WHERE interest = ?", (interests,))
            result = cursor.fetchone()
            return f'Тебе подходят эти профессии:{result[0]}' if result else "❌ По твоим интересам ничего не найдено."
        
    def get_prof_desc(self,profession):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT description FROM careers_desc WHERE professions = ?", (profession,))
            result = cursor.fetchone()
            return {result[0]} if result else "❌ По твоей профессии ничего не найдено."
        
    def get_professions(self):
         with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            a = []
            for id in range(1,31):
                cursor.execute("SELECT professions FROM careers_desc WHERE id = ?",(id,))
                a.append(cursor.fetchone())
            return a
        

if __name__ == "__main__":
    bot = CareerAdvisorBot()

    


