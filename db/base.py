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
            CREATE TABLE IF NOT EXISTS dishes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                description TEXT,
                price INTEGER,
                picture TEXT
            )
            """
        )
        self.db.commit()

    def populate_tables(self):
        self.cursor.execute(
            """
            INSERT INTO dishes (name, description, price, picture)  
                VALUES ('Ассорти СЕТ', 'Колбаски: говяжья и куриная, полукопченная, капуста квашеная, картофель фри, сочные куриные крылышки, чесночные гренки, сырный соус, горчица,кетчуп. АССОРТИ СЕТ Уй этинен жана тоок этинен, жарым- жартылай ышталган колбасалар, туздалып ачытылган капуста, карт?шк? фри, ширел?? тоок канаттары, сарымсактуу куурулган нандар, сыр чыгы, горчица, кетчуп.', 1498, 'assorti1.png'),
                ('Атлантика', 'Атлантическая слабосолёная сельдь, отварной картофель, лук, зелень. АТЛАНТИКА Азыраак туздалган Атлантика сельди, сууга бышкан карт?шк?, пияз, ч?п- чарлар. Atlantic slightly salted herring, boiled potatoes, onions, herbs.', 318, 'atlantika.png')
            """
        )
        self.db.commit()

    def get_all_dishes(self):
        self.cursor.execute("SELECT * FROM dishes")
        return self.cursor.fetchall()


if __name__ == "__main__":
    db = Database()
    db.drop_tables()
    db.create_tables()
    db.populate_tables()
    # pprint(db.get_all_dishes())
    for dish in db.get_all_dishes():
        print("Название: ", dish[1]," Описание: ", dish[2])



# СУБД SQLite
# СУБД - система управления базами данных
        # Sqlite, Postgres, MySql,       

# python301/database.sqlite