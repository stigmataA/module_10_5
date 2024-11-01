from datetime import datetime
import multiprocessing


def read_info(name): # функция
    all_data = [] # создание локального списка
    with open(name, encoding="utf-8") as file: # открытие файла
        while True: #
            line = file.readline() # чтение строки из файла
            all_data.append(line) # добавление строки в список all_data
            if not line:
                break # завершение цикла когда строка окажется пустой


if __name__ == "__main__":
    filenames = [f'./file {number}.txt' for number in range(1, 5)]

    start_1 = datetime.now() # время начало выполнения

    for filename in filenames: #
        read_info(filename)

    end_1 = datetime.now() # время завершения выполнения
    print(f"{end_1 - start_1} (линейный)") # расчет общего времени выполнения при линейном подходе

    with multiprocessing.Pool(processes=8) as pool: # создание пула рабочих процессов
        start_2 = datetime.now() # время начало выполнения
        pool.map(read_info, filenames) # метод параллельного выполнения функции read_info для каждого файла
    end_2 = datetime.now() # время завершения выполнения
    print(f"{end_2 - start_2} (многопроцессный)") # расчет общего времени выполнения при многопроцессном подходе
