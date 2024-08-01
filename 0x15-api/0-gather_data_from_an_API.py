#!/usr/bin/python3



"""
A script that returns information
about TODO list progress for an employee

URL https://jsonplaceholder.typicode.com/

Expected output:
    First line: Employee EMPLOYEE_NAME is done with tasks
    (NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
    Second and N next lines display the title of completed tasks:
    TASK_TITLE (with 1 tabulation and 1 space before the TASK_TITLE)

"""

if __name__ == "__main__":
    from json import loads
    from sys import argv
    from urllib.request import urlopen

    th_url = f'https://jsonplaceholder.typicode.com/users/{argv[1]}'
    with urlopen(th_url) as th_data:
        name = loads(th_data.read())['name']
    with urlopen(f'{th_url}/todos') as todos:
        todo_list = loads(todos.read())
        num_tasks = 0
        completed = 0
        completed_list = []
        for task in todo_list:
            if task['completed']:
                completed += 1
                completed_list.append(task['title'])
            num_tasks += 1
        print(f'Employee {name} is done with tasks({completed}/{num_tasks}):')
        [print(f'\t {title}') for title in completed_list]
