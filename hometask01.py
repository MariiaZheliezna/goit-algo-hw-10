import pulp


def main():
    # Ініціалізація моделі
    model = pulp.LpProblem("Maximize Profit", pulp.LpMaximize)

    # Визначення змінних
    lemonade = pulp.LpVariable('Лимонад', lowBound=0, cat=pulp.LpContinuous)
    fruit_juice = pulp.LpVariable('Фруктовий сік', lowBound=0, cat=pulp.LpContinuous)
    water_1 = pulp.LpVariable('Вода_1', lowBound=0, cat=pulp.LpContinuous)
    water_2 = pulp.LpVariable('Вода_2', lowBound=0, cat=pulp.LpContinuous)
    sugar = pulp.LpVariable('Цукор', lowBound=0, upBound=50, cat=pulp.LpContinuous)
    limon_juice = pulp.LpVariable('Лимонний сік', lowBound=0, upBound=30, cat=pulp.LpContinuous)
    fruit_puree = pulp.LpVariable('Фруктове пюре', lowBound=0, upBound=40, cat=pulp.LpContinuous)

    # Функція цілі (Максимізація прибутку)
    model += lemonade + fruit_juice, "Profit"   

    # Додавання обмежень
    model += 0.5 * water_1 - lemonade >= 0
    model += sugar - lemonade >= 0
    model += limon_juice - lemonade >= 0
    model += water_2 - fruit_juice >= 0
    model += 0.5 * fruit_puree - fruit_juice >= 0
    model += water_1 + water_2 <= 100

    # Розв'язання моделі
    model.solve()

    print(pulp.LpStatus[model.status])

    # Вивід результатів
    print("Кількість 'Лимонаду', яку потрібно виробити, для максимізації загальної кількості продуктів:", lemonade.varValue)
    print("Кількість 'Фруктового соку', яку потрібно виробити, для максимізації загальної кількості продуктів:", fruit_juice.varValue)
    print("Максимально можлива загальна кількість вироблених продуктів 'Лимонад' та 'Фруктовий сік': ", lemonade.varValue + fruit_juice.varValue)

if __name__ == '__main__':
    main()