#!/usr/bin/python3
"""a Python script that, using this REST API, for a
given employee ID, returns information about his/her
TODO list progress.
"""

import requests
from sys import argv


# extract employee_id from commandline
employee_id = int(argv[1])
base_endpoint = 'https://jsonplaceholder.typicode.com'

if employee_id:
    todo_url = '{}/todos?userId={}'.format(base_endpoint, employee_id)
    username_url = '{}/users/{}'.format(base_endpoint, employee_id)

    # make todo request
    todo_response = requests.get(todo_url)
    json_data = todo_response.json()
    
    # makae user request
    username_response = requests.get(username_url)
    username_json = username_response.json()

    # User passed as an arg / todo task completed
    completed_task = 0
    not_completed_task = 0
    

    for item in json_data:
        count = 0
        if 'completed' in item and item.get('completed') is True:
            completed_task += 1
        not_completed_task += 1

    # extract username
    username = 

    print(completed_task, '/', not_completed_task)
