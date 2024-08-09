def information_card(data):
    for key, volues in data.items():
            print(f"{key}: {volues}")

data_card = [
{ # данные Максим
    'Name': 'Максим',
    'Age': '46',
    'New Age': '46',
    'Is Student': 'Fals'
},
 { # данные Софья
    'Name': 'Софья',
    'Age': '16',
    'New Age': '16',
    'Is Student': 'True'
},
 { # данные Саша
    'Name': 'Саша',
    'Age': '26',
    'New Age': '26',
    'Is Student': 'True'
}]

data_card.append({ # добавляем Петю
    'Name': 'Петя',
    'Age': '30',
    'New Age': '30',
    'Is Student': 'True'
})

for i in range(0, len(data_card)):
        information_card(data_card[i])

