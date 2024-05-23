import numpy as np
from PIL import Image

def load_map(filename):
    image = Image.open(filename).convert('L')

    return np.array(image)

def calculate_rmse(map1, map2):
    error = map1 - map2
    squared_error = np.square(error)
    mean_squared_error = np.mean(squared_error)
    rmse = np.sqrt(mean_squared_error)

    return rmse

if __name__ == "__main__":
    map1_filename = 'путь/к/slam/карте.png'
    map2_filename = 'путь/к/эталонной/карте.png'
    map1 = load_map(map1_filename)
    map2 = load_map(map2_filename)

    rmse = calculate_rmse(map1, map2)
    print(rmse)
