#!/usr/bin/python3
'''
gather employee data from API
'''

from sys import argv
import csv
import requests

base_endpoint = 'https://jsonplaceholder.typicode.com'

if __name__ == '__main__':
    if len(argv) <= 2:
        userId = argv[1]

    employee_id = int(userId)
    todo_url = '{}/todos?userId={}'.format(base_endpoint, employee_id)
    username_url = '{}/users/{}'.format(base_endpoint, employee_id)

    # make todo request
    todo_response = requests.get(todo_url)
    todo_task = todo_response.json()

    # makae user request
    username_response = requests.get(username_url)
    username_json = username_response.json()

    # User passed as an arg / todo task completed
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0

    TASK_TITLE = []

    for item in todo_task:
        count = 0
        if 'completed' in item and item.get('completed') is True:
            NUMBER_OF_DONE_TASKS += 1
            TASK_TITLE.append(item.get('title'))
        TOTAL_NUMBER_OF_TASKS += 1

    # extract username
    EMPLOYEE_NAME = username_json.get('name')

    for element in TASK_TITLE:
        print(" \t", element)

    # export data in the CSV format
    file_name = '{}.csv'.format(employee_id)

    header = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS",
              "TASK_TITLE"
              ]
    new_row = []

    for task in todo_task:
        new_row.append([employee_id, EMPLOYEE_NAME,
                        task.get('completed'), task.get('title')])

    with open(file_name, 'w') as employee_file:
        csv_writer = csv.writer(employee_file, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_ALL)
        for task in new_row:
            csv_writer.writerow(task)
