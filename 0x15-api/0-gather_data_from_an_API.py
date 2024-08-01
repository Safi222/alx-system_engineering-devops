#!/user/bin/python3
"""
#A Python script that, using this REST API
#url https://jsonplaceholder.typicode.com/
#expected output:
First line: Employee EMPLOYEE_NAME is done with tasks
(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
Second and N next lines display the title of completed tasks:
TASK_TITLE (with 1 tabulation and 1 space before the TASK_TITLE)

"""
if __name__ == "__main__":
    from json import loads
    from sys import argv
    from urllib.request import urlopen

    url = f'https://jsonplaceholder.typicode.com/users/{argv[1]}'
    with urlopen(url) as th_data:
        emplo_name = loads(th_data.read())['name']
    with urlopen(f'{url}/todos') as todos:
        todo_list = loads(todos.read())
        num_tasks = 0
        completed = 0
        completed_list = []
        for task in todo_list:
            if task['completed']:
                completed += 1
                completed_list.append(task['title'])
            num_tasks += 1
        
        print(f'Employee {emplo_name} is done with tasks({completed}/{num_tasks}):')
        [print(f'\t {title}') for title in completed_list]
