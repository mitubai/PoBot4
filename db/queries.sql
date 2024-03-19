-- Создание таблицы для блюд
CREATE TABLE IF NOT EXISTS dishes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    description TEXT,
    price INTEGER,
    picture TEXT
)

-- Заполнение таблицы
INSERT INTO dishes (name, description, price, picture)  
    VALUES ('Ассорти СЕТ', 'Колбаски: говяжья и куриная, полукопченная, капуста квашеная, картофель фри, сочные куриные крылышки, чесночные гренки, сырный соус, горчица,кетчуп. АССОРТИ СЕТ Уй этинен жана тоок этинен, жарым- жартылай ышталган колбасалар, туздалып ачытылган капуста, карт?шк? фри, ширел?? тоок канаттары, сарымсактуу куурулган нандар, сыр чыгы, горчица, кетчуп.', 1498, 'assorti1.png'),
    ('Атлантика', 'Атлантическая слабосолёная сельдь, отварной картофель, лук, зелень. АТЛАНТИКА Азыраак туздалган Атлантика сельди, сууга бышкан карт?шк?, пияз, ч?п- чарлар. Atlantic slightly salted herring, boiled potatoes, onions, herbs.', 318, 'atlantika.png')

-- Получение всех блюд
SELECT name, price FROM dishes

-- Получение одного блюда
SELECT * FROM dishes WHERE id = 2

-- Получение блюд по цене
SELECT * FROM dishes WHERE price < 500

-- Получение блюд средней цены
SELECT * FROM dishes WHERE price BETWEEN 500 AND 1500

-- Получение блюд по категории
SELECT * FROM dishes WHERE category_id = 3

-- Получение блюд по названию категории
SELECT d.name, d.price, dc.name FROM dishes AS d
    JOIN dish_categories AS dc ON d.category_id = dc.id
    WHERE dc.name = 'Закуски'