class DataBase:
    def __init__(self, passport, education, speciality, post, salary):
        self.data = {'passport': passport,'education': education ,'speciality':speciality,'post':post , 'salary':salary}
    def information(self):
            return self.data

base = {}
while True:
    n = input('База данних:\n 1 - інформація про працівника \n 2 - добавити інформацію про працівника \n 3 - записати інформацію в файл \n 4 - Видалення працівника \n 5 - Завершити роботу \n')
    if n == '1':
        name = input("Ім'я працівника: ")
        print(base[name])

    elif n == '2':
        name = input("Ім'я працівника: ")
        passport = input('Введіть паспортні данні працівника: ')
        edu = input('Освіта працівника: ')
        spec = input('Спеціальність працівника: ')
        post = input('Посада працівника: ')
        salary = input('Заробітна плата: ')
        worker = DataBase(passport, edu, spec, post, salary)
        base[name] = worker.information()

    elif n == '3':
        name = input("Введіть ім'я:  ")
        with open('text.txt','a', encoding='UTF-8') as file:
            file.write(str(base[name]))
    elif n == '4':
        name = input("Введіть ім'я: ")
        del base[name]
    elif n == '5':
        break
    else:
        raise Exception('Невірне значення n')
