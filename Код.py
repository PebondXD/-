import sqlite3

conn = sqlite3.connect('inventory.db')
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS inventory (
                id INTEGER PRIMARY KEY,
                name TEXT,
                description TEXT,
                price REAL,
                quantity INTEGER,
                category TEXT
            )''')
conn.commit()

def add_product():
    name = input("Введите название товара: ")
    description = input("Введите описание товара: ")
    price = float(input("Введите цену товара: "))
    quantity = int(input("Введите количество товара на складе: "))
    category = input("Введите категорию товара: ")

    cur.execute('''INSERT INTO inventory (name, description, price, quantity, category)
                VALUES (?, ?, ?, ?, ?)''', (name, description, price, quantity, category))
    conn.commit()
    print("Товар успешно добавлен в инвентарь!")

def delete_product():
    product_id = int(input("Введите ID товара для удаления: "))

    cur.execute('''DELETE FROM inventory WHERE id = ?''', (product_id,))
    conn.commit()
    print("Товар успешно удален из инвентаря!")

def edit_product():
    product_id = int(input("Введите ID товара для редактирования: "))

    cur.execute('''SELECT * FROM inventory WHERE id = ?''', (product_id,))
    product = cur.fetchone()

    if product:
        print("Текущая информация о товаре:")
        print("ID:", product[0])
        print("Название:", product[1])
        print("Описание:", product[2])
        print("Цена:", product[3])
        print("Количество:", product[4])
        print("Категория:", product[5])

        new_name = input("Введите новое название товара (оставьте пустым, если не хотите менять): ")
        new_description = input("Введите новое описание товара (оставьте пустым, если не хотите менять): ")
        new_price = float(input("Введите новую цену товара (оставьте 0, если не хотите менять): "))
        new_quantity = int(input("Введите новое количество товара на складе (оставьте 0, если не хотите менять): "))
        new_category = input("Введите новую категорию товара (оставьте пустым, если не хотите менять): ")

        if new_name:
            cur.execute('''UPDATE inventory SET name = ? WHERE id = ?''', (new_name, product_id))
        if new_description:
            cur.execute('''UPDATE inventory SET description = ? WHERE id = ?''', (new_description, product_id))
        if new_price != 0:
            cur.execute('''UPDATE inventory SET price = ? WHERE id = ?''', (new_price, product_id))
        if new_quantity != 0:
            cur.execute('''UPDATE inventory SET quantity = ? WHERE id = ?''', (new_quantity, product_id))
        if new_category:
            cur.execute('''UPDATE inventory SET category = ? WHERE id = ?''', (new_category, product_id))

        conn.commit()
        print("Информация о товаре успешно обновлена!")
    else:
        print("Товар с указанным ID не найден.")

def display_inventory():
    cur.execute('''SELECT * FROM inventory''')
    products = cur.fetchall()

    if products:
        print("Инвентарь магазина:")
        for product in products:
            print("ID:", product[0])
            print("Название:", product[1])
            print("Описание:", product[2])
            print("Цена:", product[3])
            print("Количество:", product[4])
            print("Категория:", product[5])
            print("----------")
    else:
        print("Инвентарь пуст.")

def main_menu():
    while True:
        print("\nГлавное меню")
        print("1. Добавить товар")
        print("2. Удалить товар")
        print("3. Редактировать информацию о товаре")
        print("4. Просмотреть весь инвентарь")
        print("5. Выйти из программы")
        choice = input("Выберите действие (1-5): ")

        if choice == '1':
            add_product()
        elif choice == '2':
            delete_product()
        elif choice == '3':
            edit_product()
        elif choice == '4':
            display_inventory()
        elif choice == '5':
            break
        else:
            print("Пожалуйста, выберите корректное действие (1-5).")

if __name__ == "__main__":
    main_menu()

conn.close()