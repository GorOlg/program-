  
def show_menu(stop_all):
    if stop_all=="yes":
        return 7
    else:
        print("\nВыберите необходимое действие:\n"
            "1. Отобразить весь справочник\n"
            "2. Найти абонента\n"
            "3. Добавить абонента в справочник\n"
            "4. Сохранить справочник в текстовом формате\n"
            "5. Закончить работу")
    choice = int(input("Нажми: "))
    return choice

# чтение 1
def read_txt(filename):
    phone_book=[]
    fields=['Фамилия', 'Имя', 'Телефон']
    with open(filename,'r',encoding='utf-8') as phb:
        for line in phb:
            record = dict(zip(fields, line.split(','))) 
            phone_book.append(record)
    return phone_book

def read_show(filename):
    with open(filename,'r',encoding='utf-8') as data:
        names=data.readlines()
    print(*names)


# Найти абонента 2
def find(phone_book,search_value,key_d):
    list_search=[]
    for i in range(len(phone_book)):
        if phone_book[i][key_d].lower()==search_value.lower():
            list_search.append(phone_book[i])
    if len(list_search)>0:
        return list_search
    return key_d,search_value, "отствует в справочнике"    
# меню для поиска 
def show_menu_0():
    print("\n1.По фамилии\n"
        "2.По имени\n"
        "3.По телефону\n")
    choice_menu_0=int(input())
    return choice_menu_0

# Добавить в сохраенное 3
def add_user(Last_name, name,number):
    with open('temp.txt','w',encoding='utf-8') as data:
        data.write(Last_name +' '+ name +' '+ number +'\n')
    new_data= read_txt('temp.txt')
    return new_data                
# Запись сохраненного
def write_txt(filename, phone_book):
    with open(filename,'w',encoding='utf-8') as phout:
        for i in range(len(phone_book)):
            s=''
            for v in phone_book[i].values():
                s+=v+','
            phout.write(f'{s[:-1]}\n')
        return 'Справочник сохранен!'

# цикл с программой
def work_with_phonebook():
    stop_all='No'
    choice=show_menu(stop_all)
    filename= "phonebook.txt"
    phone_book=read_txt("phonebook.txt")
    # fields=['Фамилия','имя','телефон']
    while (choice!=7):

        if choice==1: # отобразить 
            read_show(filename)
            input("Жми: ")
        elif choice==2: # Поиск
            choice_menu_0= show_menu_0()
            if choice_menu_0==1:
                search_value=input("Введите Фамилию: ")
                key_d='Фамилия'
                print(*(find(phone_book,search_value,key_d)),sep='\n')
            if choice_menu_0==2:
                search_value=input("Введите Имя: ")
                key_d='Имя'
                print(*(find(phone_book,search_value,key_d)),sep='\n')
            if choice_menu_0==1:
                search_value=input("Введите Номер: ")
                key_d='Номер'
                print(*(find(phone_book,search_value,key_d)),sep='\n')
        elif choice==3: # Дбавить абонента
            last_name= input("Last name: ")
            name = input("First name: ")
            number= input("number phone: ")
            new_data= add_user(last_name,name,number)
            print("Добавлен!")
            write_txt(filename,phone_book + new_data)
        elif choice==4:
            print(write_txt('phonebook.txt',phone_book))
        elif choice==5:
            # user_data=input('new data ')
            # add_user(phone_book,user_data)
            # write_txt('phonebook.txt',phone_book)
            stop_menu_6=0
            while stop_menu_6 !=1:
                choice_3= input("Сохранить изменения? (Да\Нет): ").lower()
                if choice_3=='да':
                    print(write_txt('phonebook.txt',phone_book))
                    stop_menu_6 = 1 
                    stop_all= 'yes'
                    print("готово")
                elif choice_3== 'нет':
                    stop_menu_6=1
                    stop_all="yes"
                    print('готово')
                else:
                    print('Введите "да" или "нет"?')


    choice=show_menu(stop_all)

work_with_phonebook()