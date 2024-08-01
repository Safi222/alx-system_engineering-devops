#!/usr/bin/python3
"""
A python  script that returns information
about TODO list progress for an employee
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
        completed_titles = []
        for task in todo_list:
            if task['completed']:
                completed += 1
                completed_titles.append(task['title'])
            num_tasks += 1
        print(f'Employee {name} is done with tasks({completed}/{num_tasks}):')
        [print(f'\t {title}') for title in completed_titles]
