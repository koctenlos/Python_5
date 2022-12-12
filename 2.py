# Условие задачи: На столе лежит 2021(или сколько вы скажете)
# конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28
# (или сколько вы зададите в начале) конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сделайте эту игру.
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

import random
import sys

def create_random():
    return random.randint(1, 28)

def gamer_choice():
    gamer = int(input("Напишите количество конфет от 1 до 28: "))
    if gamer >= 1 and gamer <= 28:
        return gamer
    else:
        print("Указано неверное значение")
        sys.exit()
    




def round():
    ostatok = 2021
    gamer = gamer_choice()
    bot = create_random()
    i = 1
    while ostatok >0:
        if i%2 == 0:
            ostatok = count_ostatok(ostatok, gamer_choice())
            i = i+1
        else:
            ostatok = count_ostatok(ostatok, create_random())
            i = i+1
        if ostatok>0:
            print(f'Раунд {i-1}, Остаток =  {ostatok} ')
        else:
            if i%2 == 0:
                print("Человек  победил")
            else:
                print("Компьютер победил")



def count_ostatok(ost, a):
    if ost > 0:
        return (ost - a)


round()