#!/usr/bin/python3
"""a Python script that, using this REST API, for a
given employee ID, returns information about his/her
TODO list progress.
"""

import requests
import sys.argv


# extract employee_id from commandline
employee_id = int(argv[1])


if employee_id:
    # employee_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(employee_id)
    todo_url = 'https://jsonplaceholder.typicode.com/todos/{}'.format(employee_id)
    
    # make a request
    response = requests.get(todo_url)

    # jsonify response body
    json_data = response.json()
    completed_task = None

    print(json_data) 

