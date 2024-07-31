#!/usr/bin/python3
'''
Gather employee data from API
'''

import requests
from sys import argv

base_endpoint = 'https://jsonplaceholder.typicode.com'

def gather_employee_data(user_id):
    """Gathers and prints employee data from the API."""
    todo_url = f'{base_endpoint}/todos?userId={user_id}'
    username_url = f'{base_endpoint}/users/{user_id}'

    try:
        # Make requests
        todo_response = requests.get(todo_url)
        todo_response.raise_for_status()
        todos = todo_response.json()

        username_response = requests.get(username_url)
        username_response.raise_for_status()
        user = username_response.json()

        # Process data
        completed_tasks = [todo['title'] for todo in todos if todo['completed']]
        total_tasks = len(todos)
        employee_name = user.get('name')

        # Output results
        print(f'Employee {employee_name} is done with tasks({len(completed_tasks)}/{total_tasks}):')
        for task in completed_tasks:
            print(f'     {task}')

    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
    except ValueError:
        print("Invalid user ID. Please provide a valid number.")

if __name__ == '__main__':
    if len(argv) == 2:
        try:
            user_id = int(argv[1])
            gather_employee_data(user_id)
        except ValueError:
            print("Invalid user ID. Please provide a valid number.")
    else:
        print("Usage: ./script_name.py <user_id>")
# #!/usr/bin/python3
# '''
# gather employee data from API
# '''

# import re
# import requests
# from sys import argv

# base_endpoint = 'https://jsonplaceholder.typicode.com'

# if __name__ == '__main__':
#     if len(argv) <= 2:
#         userId = argv[1]

#     employee_id = int(userId)
#     todo_url = '{}/todos?userId={}'.format(base_endpoint, employee_id)
#     username_url = '{}/users/{}'.format(base_endpoint, employee_id)

#     # make todo request
#     todo_response = requests.get(todo_url)
#     json_data = todo_response.json()

#     # makae user request
#     username_response = requests.get(username_url)
#     username_json = username_response.json()

#     # User passed as an arg / todo task completed
#     NUMBER_OF_DONE_TASKS = 0
#     TOTAL_NUMBER_OF_TASKS = 0

#     TASK_TITLE = []

#     for item in json_data:
#         count = 0
#         if 'completed' in item and item.get('completed') is True:
#             NUMBER_OF_DONE_TASKS += 1
#             TASK_TITLE.append(item.get('title'))
#         TOTAL_NUMBER_OF_TASKS += 1

#     # extract username
#     EMPLOYEE_NAME = username_json.get('name')

#     print('Employee {} is done with tasks({}/{}):'.format(
#                                             EMPLOYEE_NAME,
#                                             NUMBER_OF_DONE_TASKS,
#                                             TOTAL_NUMBER_OF_TASKS
#                                             ))

#     for element in TASK_TITLE:
#         print('     {}'.format(element))
