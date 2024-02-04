from scipy import integrate
import random


# Визначення функції та межі інтегрування
def f(x):
    return x ** 2

def is_inside(a, b, x, y):
    """Перевіряє, чи знаходиться точка (x, y) всередині області інтегрування"""
    return y <= f(x)

def monte_carlo_simulation(a, b, num_experiments):
    """Виконує серію експериментів методом Монте-Карло."""
    average_area = 0

    for _ in range(num_experiments):
        # Генерація випадкових точок
        points = [(random.uniform(0, a), random.uniform(0, b)) for _ in range(15_000)]
        # Відбір точок, що знаходяться всередині трикутника
        inside_points = [point for point in points if is_inside(a, b, point[0], point[1])]

        # Розрахунок площі за методом Монте-Карло
        M = len(inside_points)
        N = len(points)
        area = (M / N) * (a * b)

        # Додавання до середньої площі
        average_area += area

    # Обчислення середньої площі
    average_area /= num_experiments
    return average_area

def main():
    # Розміри прямокутника
    a = 2  # ширина прямокутника
    b = 4  # висота прямокутника

    result = integrate.quad(f, 0, a)
    S = result[0]  # Теоретична площа

    # Кількість експериментів
    num_experiments = 100

    # Виконання симуляції
    average_area = monte_carlo_simulation(a, b, num_experiments)

    print(f"Обчислення визначеного інтеграла функцію quad з підмодуля integrate: {S}")
    print(f"Обчислення значення інтеграла функції за допомогою методу Монте-Карло (за {num_experiments} експериментів): {average_area}")

if __name__ == '__main__':
    main()