class Mechanic:
    def __init__(self, spare_part, car_brand, release_date):
        self.data = {'spare part': spare_part,'car brand': car_brand,'release date':release_date}
    def information(self):
            return self.data

base = {}
while True:
    n = input('База данних механіка:\n 1 - інформація про запчастину\n 2 - добавити інформацію про запчастину \n 3 - Завершити роботу \n ')
    if n == '1':
        name = input('')
        print(base[name])

    elif n == '2':
        name = input('назва запчастини: ')
        spare_part = input('')
        car = input('')
        release_date = input('')
        spare = Mechanic(spare_part,car,release_date)
        base[name] = spare.information()
        print(base)
        
    elif n == '3':
        break
    else:
        raise Exception('Error')
