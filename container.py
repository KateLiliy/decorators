class MyPascalList(object):
    def __init__(self, *args):
        self.index = 0
        if args:
            self.data = list(args) #для сразу заполненного списка
        else:
            self.data = [] #для пустого списка

    def append(self, value):
        self.data.append(value)

    def __iter__(self): #для итерации в цикле for
        return self

    def __next__(self): #для итерации в цикле for
        if self.index == len(self.data):
            raise StopIteration #raise для остановки итератора (можно поднять исключение)
        self.index += 1
        return self.data[self.index - 1]

    def __setitem__(self, key, value):#назначение элемента по индексу
        if (key - 1) >= 0:
            self.data[key - 1] = value
        elif key == 0:
            raise IndexError #ошибка, если обратились к нулю
        else:
            self.data[key] = value

    def __getitem__(self, key):#доступ по индексу (или ключу)
        if (key - 1) >= 0:
            return self.data[key - 1]
        elif key == 0:
            raise IndexError
        else:
            return self.data[key]

    def __repr__(self):#для получения строкового представления объекта (для print)
        return str(self.data)

    def __len__(self):
        return len(self.data)

    def __contains__(self, item):#проверка на принадлежность элемента
        return item in self.data




my_list1 = MyPascalList(1, 2, 3, 4, 5, 6) # список с элементами
my_list2 = MyPascalList()

my_list1[1] = 0
my_list1[6] = 100

try:
    my_list1[0] = 0  # Обнуляет последний элемент (!!!)
except IndexError:
    print('Нельзя обращаться к 0, у нас тут массив с 1')

 #для проверки   
my_list1.append(2)
my_list2.append(1)
my_list2.append(2)
my_list2.append(3)
my_list2.append(4)


print(my_list1)
[print(elem, sep=' ', end=' ') for elem in my_list1]
print()
print(my_list2)
[print(elem, sep=' ', end=' ') for elem in my_list2]
print()
print(len(my_list1))
print(100 in my_list1)
print(1121 in my_list1)
