# 1-Напишите программу, удаляющую из текста все слова, 
# содержащие заданную строку.

# Пример:
# Пугать ты галок пугай => заданная строка "галок" =>
# Пугать ты пугай
# Пугать ты галок пугай => заданная строка "пуг" =>
# Пугать ты галок

my_text = 'Пугать ты галок пугай'

def del_some_words(my_text):
    my_text = list(filter(lambda x: 'галок' not in x, my_text.split()))
    return " ".join(my_text)

my_text = del_some_words(my_text)
print(my_text)