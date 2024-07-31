#!/usr/bin/python3
'''
gather employee data from API
'''

from sys import argv
import requests
import json


base_endpoint = 'https://jsonplaceholder.typicode.com'


if __name__ == '__main__':
    if len(argv) <= 2:
        userId = argv[1]

    employee_id = int(userId)
    todo_url = '{}/todos?userId={}'.format(base_endpoint, employee_id)
    username_url = '{}/users/{}'.format(base_endpoint, employee_id)

    # make todo request
    todo_response = requests.get(todo_url)
    json_todo = todo_response.json()

    # makae user request
    username_response = requests.get(username_url)
    username_json = username_response.json()

    # User passed as an arg / todo task completed
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0

    TASK_TITLE = []

    for item in json_todo:
        count = 0
        if 'completed' in item and item.get('completed') is True:
            NUMBER_OF_DONE_TASKS += 1
            TASK_TITLE.append(item.get('title'))
        TOTAL_NUMBER_OF_TASKS += 1

    # extract username
    EMPLOYEE_NAME = username_json.get('name')

    # export data into json format
    obj = {str(employee_id): []}
    new_obj = {}

    for item in json_todo:
        id_str = str(employee_id)
        obj[id_str].append({
            "task": item.get('title'),
            "completed": item.get('completed'),
            "username": EMPLOYEE_NAME
        })

    filename = "{}.json".format(employee_id)
    with open(filename, 'w') as json_file:
        json.dump(obj, json_file)
