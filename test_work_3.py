#Task 4.7

from collections import Counter

north_list = [elem for bill in north for elem in bill]
south_list = [elem for bill in south for elem in bill]
center_list = [elem for bill in center for elem in bill]

c = Counter(center_list)
s = Counter(south_list)
n = Counter(north_list)
print(c - (n + s))
# Counter()
print(n - (s + c))
# Counter({'Cola': 6})
print(s - (c + n))
# Counter()

#Task 4.8

from collections import Counter

north_list = [elem for bill in north for elem in bill]
south_list = [elem for bill in south for elem in bill]
center_list = [elem for bill in center for elem in bill]

c = Counter(center_list)
s = Counter(south_list)
n = Counter(north_list)

print((s + c + n).most_common()[1])
# ('Bread', 240)

#Task 4.9

ratings = [('Old York', 3.3), ('New Age', 4.6), ('Old Gold', 3.3), ('General Foods', 4.8),
          ('Belissimo', 4.5), ('CakeAndCoffee', 4.2), ('CakeOClock', 4.2), ('CakeTime', 4.1),
          ('WokToWork', 4.9), ('WokAndRice', 4.9), ('Old Wine Cellar', 3.3), ('Nice Cakes', 3.9)]
# Отсортируйте список ratings по убыванию рейтинга. Для кафе
# с одинаковым рейтингом отсортируйте кортежи по названию.
ratings.sort(key=lambda x: (-x[1], x[0]))
# Сохраните данные с рейтингом в словарь cafes, где ключами являются
# названия кафе, а значениями - их рейтинг.
from collections import OrderedDict
cafes = OrderedDict(ratings)

#Task 4.10
from collections import deque, defaultdict

def task_manager(tasks):
    servers = defaultdict(deque)
    for task in tasks:
        if task[-1]:
            servers[task[1]].appendleft(task[0])
        else:
            servers[task[1]].append(task[0])
    return servers
