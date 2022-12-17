from collections import deque
from collections import defaultdict

tasks = [(36871, 'office', False), (40690, 'office', False), (35364, 'voltage', False), (41667, 'voltage', True), (33850, 'office', False)]

def task_manager(tasks):
    
    tasks_dict = defaultdict(deque)
    
    for a in tasks:
        tasks_dict[a[1]] = deque()
    
    for b in tasks:
        if b[2]:
            tasks_dict[b[1]].appendleft(b[0])
        else:
            tasks_dict[b[1]].append(b[0])

    return tasks_dict

print (task_manager(tasks))

