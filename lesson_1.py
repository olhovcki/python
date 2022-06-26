# Задание 6

mi_revenue = int(input('Введите значение выручки - '))
mi_costs = int(input('Введите значение издержек - '))

if mi_revenue > mi_costs:
    mi_profit = mi_revenue - mi_costs
    mi_profitability_revenue = mi_profit / mi_revenue * 100
    print('Ваша фирма является прибыльной!','\nРентабельность составит -','%.2f'%mi_profitability_revenue,'%')
    num_employees = int(input('Сколько у Вас сотрудников? - '))
    mi_profit_employees = mi_profit / num_employees
    print('Прибыль на одного сотрудника составит -','%.2f'%mi_profit_employees, 'тубриков')
else:
    print('Ваша фирма является убыточной!')
