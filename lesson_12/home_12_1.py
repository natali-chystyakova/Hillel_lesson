# ДЗ 14
# Дана строка в байтовом виде: b'r\xc3\xa9sum\xc3\xa9'.
# Декодировать её в строковый вид в кодировке по умолчанию.
# Затем результат преобразовать снова в байтовый, только уже в кодировке ‘Latin1’
# И на конец результат снова декодировать в строку
# (результаты всех преобразований выводить на экран).

string_byt = b'r\xc3\xa9sum\xc3\xa9'
string_str = string_byt.decode()
print(string_str)
string_byt_lat = string_str.encode('Latin1')
print(string_byt_lat)
string_str_lat = string_byt_lat.decode('Latin1')
print(string_str_lat)
