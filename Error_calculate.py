import numpy as np
from PIL import Image

def load_map(filename):
    """
    Загрузка карту из файла и конвертация ее в numpy массив

    :param filename: Путь к файлу карты
    :return: numpy массив, представляющий карту
    """
    # Конвертация изображения в оттенки серого
    image = Image.open(filename).convert('L')

    return np.array(image)

def calculate_rmse(map1, map2):
    """
    Функция для расчета ошибки RMSE

    :param map1: numpy массив, представляющий карту, построенную с помощью SLAM
    :param map2: numpy массив, представляющий эталонную карту
    :return: значение ошибки RMSE
    """
    # Вычисление обычной ошибки
    error = map1 - map2

    # Возведение в квадрат и усреднение ошибки
    squared_error = np.square(error)
    mean_squared_error = np.mean(squared_error)

    # Корень из среднеквадратичной ошибки
    rmse = np.sqrt(mean_squared_error)

    return rmse

if __name__ == "__main__":
    # Загрузка карт из файлов
    map1_filename = 'путь/к/slam/карте.png'
    map2_filename = 'путь/к/эталонной/карте.png'
    map1 = load_map(map1_filename)
    map2 = load_map(map2_filename)

    # Расчет ошибки методом RMSE
    rmse = calculate_rmse(map1, map2)
    print(f"Ошибка:", rmse)
