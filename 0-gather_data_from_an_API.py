#!/user/bin/python3
"""
A Python script that, using this REST API
URL https://jsonplaceholder.typicode.com/

Expected output :
First line: Employee EMPLOYEE_NAME is done with
tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
Second and N next lines display the title of completed tasks:
TASK_TITLE (with 1 tabulation and 1 space before the TASK_TITLE)

"""
from sys import argv
from json import loads
from urllib.request import urlopen


if __name__ == "__main__":

    url = f'https://jsonplaceholder.typicode.com/users/{argv[1]}'

    with urlopen(url) as th_data:
        emplo_name = loads(th_data.read())['name']
    with urlopen(f'{url}/todos') as todos:
        todo_list = loads(todos.read())
        tasks_num = 0
        completed = 0
        completed_list = []
        for task in todo_list:
            if task['completed']:
                completed += 1
                completed_list.append(task['title'])
            tasks_num += 1

        print(f'Employee {emplo_name} is done with tasks({completed}/{tasks_num})')
        [print(f'\t {title}') for title in completed_list]
