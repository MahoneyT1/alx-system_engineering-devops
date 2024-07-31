#!/usr/bin/python3
'''
gather employee data from API
'''

import re
import requests
from sys import argv

base_endpoint = 'https://jsonplaceholder.typicode.com'

if __name__ == '__main__':
    if len(argv) <= 2:
        userId = argv[1]
    
    
    employee_id = int(userId)
    todo_url = '{}/todos?userId={}'.format(base_endpoint, employee_id)
    username_url = '{}/users/{}'.format(base_endpoint, employee_id)

    # make todo request
    todo_response = requests.get(todo_url)
    json_data = todo_response.json()

    # makae user request
    username_response = requests.get(username_url)
    username_json = username_response.json()

    # User passed as an arg / todo task completed
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0

    title = []

    for item in json_data:
        count = 0
        if 'completed' in item and item.get('completed') is True:
            NUMBER_OF_DONE_TASKS += 1
            title.append(item.get('title'))
        TOTAL_NUMBER_OF_TASKS += 1

    # extract username
    EMPLOYEE_NAME = username_json.get('name')

    print("Employee {} is done with tasks({}/{}):".format(
                                            EMPLOYEE_NAME,
                                            NUMBER_OF_DONE_TASKS,
                                            TOTAL_NUMBER_OF_TASKS
                                            ))

    for element in title:
        print("\t", element)
