from random import randint
series = ['Black mirror','Wandinha','Round 6','The Walking Dead','Game of Thrones','Breakink Bad']

rates = []
random_num_list = []
count = 0

while count < 6:
    random_num = randint(0, 5)
    if random_num not in random_num_list:
        rate = int(input(f'Quantas estrelas para a serie {series[random_num]}:'))
        count = count + 1
        rates.insert(random_num, rate)
        random_num_list.append(random_num)
    
print(series)
print(rates)