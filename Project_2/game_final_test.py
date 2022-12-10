import numpy as np

def random_predict(number:int=1) -> int:
         
    count = 0
    bottom_limit = 1
    top_limit = 101
    
    while True:
        
        count += 1
        
        predict_number = np.random.randint( bottom_limit, top_limit) # предполагаемое число
        if predict_number > number:
            top_limit = predict_number
        elif predict_number < number:
            bottom_limit = predict_number
        else:
            break # выход из цикла, если угадали
    
    return(count)

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток
    dispersion = round(np.var(count_ls),2)
    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    print(f"Дисперсия: {dispersion}")
    return(score)

# RUN
if __name__ == '__main__':
    score_game(random_predict)