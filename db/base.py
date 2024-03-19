import sqlite3
from pathlib import Path
from pprint import pprint


class Database:
    def __init__(self) -> None:
        db_path = Path(__file__).parent.parent / "database.sqlite"
        self.db = sqlite3.connect(db_path)
        self.cursor = self.db.cursor()

    def drop_tables(self):
        self.cursor.execute("DROP TABLE IF EXISTS dishes")
        self.db.commit()

    def create_tables(self):
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS dish_categories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT
            )
            """
        )
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS dishes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                description TEXT,
                price INTEGER,
                picture TEXT,
                category_id INTEGER,
                FOREIGN KEY(category_id) REFERENCES dish_categories(id)
            )
            """
        )
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS survey (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                age INTEGER,
                phone_number TEXT
            )
            """
        )
        self.db.commit()

    def populate_tables(self):
        self.cursor.execute(
            """
            INSERT INTO dish_categories (name)
                VALUES  ('Пицца 30 см'),
                        ('Пицца 40 см'),
                        ('Закуски'), 
                        ('Салаты'), 
                        ('Супы')
            """
        )
        self.cursor.execute(
            """
            INSERT INTO dishes (name, description, price, picture, category_id)  
                VALUES ('Ассорти СЕТ', 'Колбаски: говяжья и куриная, полукопченная, капуста квашеная, картофель фри, сочные куриные крылышки, чесночные гренки, сырный соус, горчица,кетчуп. АССОРТИ СЕТ Уй этинен жана тоок этинен, жарым- жартылай ышталган колбасалар, туздалып ачытылган капуста, карт?шк? фри, ширел?? тоок канаттары, сарымсактуу куурулган нандар, сыр чыгы, горчица, кетчуп.', 1498, 'assorti1.png', 3),
                ('Атлантика', 'Атлантическая слабосолёная сельдь, отварной картофель, лук, зелень. АТЛАНТИКА Азыраак туздалган Атлантика сельди, сууга бышкан карт?шк?, пияз, ч?п- чарлар. Atlantic slightly salted herring, boiled potatoes, onions, herbs.', 318, 'atlantika.png', 3)
            """
        )
        self.db.commit()

    def get_all_dishes(self):
        self.cursor.execute("SELECT * FROM dishes")
        return self.cursor.fetchall()

    def get_one_dish(self, id: int):
        self.cursor.execute(
            "SELECT * FROM dishes WHERE id = :dishId", {"dishId": id}
        )
        return self.cursor.fetchone()

    def get_cheap_dishes(self):
        self.cursor.execute("SELECT * FROM dishes WHERE price < 500")
        return self.cursor.fetchall()

    def get_dishes_by_category(self, category_id: int):
        self.cursor.execute(
            "SELECT * FROM dishes WHERE category_id = :categoryId",
            {"categoryId": category_id},
        )
        return self.cursor.fetchall()

    def get_dishes_by_cat_name(self, cat_name: str):
        self.cursor.execute(
            """
            SELECT d.* , dc.name FROM dishes AS d
            JOIN dish_categories AS dc ON d.category_id = dc.id
            WHERE dc.name = :catName
            """,
            {"catName": cat_name},
        )
        return self.cursor.fetchall()

    def insert_survey(self, data: dict):
        self.cursor.execute(
            """
            INSERT INTO survey (name, age, phone_number)
                VALUES (:name, :age, :phone_number)
            """,
            data,
        )
        self.db.commit()


if __name__ == "__main__":
    db = Database()
    db.drop_tables()
    db.create_tables()
    db.populate_tables()
    # pprint(db.get_all_dishes())
    # for dish in db.get_all_dishes():
    #     print("Название: ", dish[1]," Описание: ", dish[2])
    # pprint(db.get_one_dish(2))
    # pprint(db.get_cheap_dishes())
    # pprint(db.get_dishes_by_category(3))
    pprint(db.get_dishes_by_cat_name("Закуски"))






# СУБД SQLite
# СУБД - система управления базами данных
        # Sqlite, Postgres, MySql,       

# python301/database.sqlite