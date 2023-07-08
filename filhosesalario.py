sum_of_salary = 0
count_of_people = 0

for count in range (0, 5):
    salary = float(input('Digite o salario '))
    num_of_children = int(input('Digite o numero de filhos '))
    
    if salary <= 1500:
        count_of_people += 1  # count_of_people = count_of_people +1
    
    if num_of_children > 3:
        sum_of_salary += salary   # sum_of_salary = sum_of_salary + salary


print('Recebem ate 1.500,00 ', count_of_people)
print('Soma dos salarios com mais de 3 filhos ', sum_of_salary)