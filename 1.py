#Практическое задание по уроку "Строки и индексация строк"
#вывести только первое предложение.
_to_split = "Сейчас на Земле появился новый вид роботов. Раньше их называли 'железной оравой', но это не очень точное определение."
print("Первое предложение:",_to_split[0:_to_split.find('.')+1])

#вывести слово в обратном порядке.
_palindrom = "string1"
print("Строка '"+_palindrom+"' в обратном порядке:", _palindrom[::-1])

_even_parts = "1234567"
print("Две половины строки '" + _even_parts +"' поменяли местами:",_even_parts[len(_even_parts)//2:len(_even_parts)]+_even_parts[0:len(_even_parts)//2])

_odds_evens = "123456"
print("Сначала четные, потом нечетные символы строки",_odds_evens+": " ,_odds_evens[0::2], _odds_evens[1::2])

#вывести заданную строку в обратном порядке без первого и последнего символа
_backwards = "123456"
print("Строка '"+_backwards+"' в обратном порядке без первого и последнего символа:",_backwards[-2:0:-1])

_split = "123 1234 5463"
print(_split.split(" "))
_j="0"
print(_j.join(reversed(_split)))
print(reversed(_split))