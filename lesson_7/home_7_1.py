# Дан словарь, создать новый словарь при помощи конструкции
# генератор словаря, поменяв местами ключ и значение.


chess_players = {
    "Carlsen, Magnus": 2865,
    "Firouzja, Alireza": 2804,
    "Ding, Liren": 2799,
    "Caruana, Fabiano": 2792,
    "Nepomniachtchi, Ian": 2773
}


new_chess_players = {value: key for key, value in chess_players.items()}
print(new_chess_players)