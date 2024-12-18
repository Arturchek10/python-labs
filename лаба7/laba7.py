# 10. Написать класс ChartDrawer, который принимает список списков, содержащих координаты точек и содержит методы
# add_point(x, y) для добавления новой точки в список, remove_point(x, y) для удаления точек с указанными координатами.
# Класс должен правильно использовать инкапсуляцию

class ChartDrawer:
    def __init__(self, points=None):
        "Инициализация класса с набором точек"
        self.__points = points if points is not None else []  # Список списков с координатами точек

    def add_point(self, x, y):
        "Добавляет новую точку в список"
        self.__points.append([x, y])
        print(f"Точка ({x}, {y}) добавлена")

    def remove_point(self, x, y):
        "Удаляет точку с указанными координатами"
        try:
            self.__points.remove([x, y])
            print(f"Точка ({x}, {y}) удалена")
        except ValueError:
            print(f"Точка ({x}, {y}) не найдена")

    def get_points(self):
        "Возвращает копию списка точек "
        return self.__points[:]

    def __str__(self):
        "Возвращает строковое представление объекта"
        return f"ChartDrawer с точками: {self.__points}"


# Пример

if __name__ == "__main__":
    # Создаем объект класса
    chart = ChartDrawer([[0, 0], [1, 1], [2, 2]])
    
    # Вывод начального состояния
    print(chart)
    
    # Добавляем новую точку
    chart.add_point(3, 3)
    print(chart)
    
    # Удаляем точку
    chart.remove_point(1, 1)
    print(chart)
    
    # Пытаемся удалить несуществующую точку
    chart.remove_point(10, 10)
    
    # Получаем список точек
    points = chart.get_points()
    print(f"Копия списка точек: {points}")
    
    # Проверка на инкапсуляцию: изменение копии не влияет на оригинал
    points.append([5, 5])
    print(f"Измененная копия точек: {points}")
    print(f"Оригинальный список точек: {chart.get_points()}")
