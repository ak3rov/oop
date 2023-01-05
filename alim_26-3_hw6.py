contacts = [
    {'name': 'Geektech', 'phone': '0507052018'},
    {'name': 'Служба спасения', 'phone': '911'},
    {'name': 'Пожарная служба', 'phone': '101'},
]

def create():
    name = input('Введите имя: ')
    phone = input('Введите номер: ')
    contacts.append({"name": name, "phone": phone})
    return contacts

def edit():
    i = 0
    while i < 2:
        name = input("(Geektech) (Служба спасения) (Пожарная служба) \n Введите имя контакта :\n ")
        if name != "Geektech":
            print('Имя не правильно!')
            continue
        new_name = input('Введите новое имя:')
        new_phone = input('Введите новый номер:')
        for contact in contacts:
            if name == contact["name"]:
                contact["name"] = new_name
                contact["phone"] = new_phone
            return contact

def delete():
    while True:
        name = input('(Geektech) (Служба спасения) (Пожарная служба) \n Введите имя: \n ')
        for contact in contacts:
            if name != contact["name"]:
                continue
        for contact in contacts:
            if name == contact["name"]:
                a = contacts.index(contact)
                del contacts[a]
        return contacts

while True:
    for i in contacts:
        print(f"{i}")
    commands = input("create = 1, edit = 2, delete =  3 \n Введите номер команды \n ")
    if commands == "1":
        create()
    elif commands == "2":
        edit()
    elif commands == "3":
        delete()
    elif commands != "1" or "2" or "3":
        print('Такой команды нет!')
        continue
