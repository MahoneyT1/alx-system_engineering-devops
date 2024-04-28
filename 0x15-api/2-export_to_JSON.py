#!/usr/bin/python3
"""
Script to retrieve and display TODO list progress for a given employee
using a REST API.

Requirements:
- Use urllib or requests module
- Accept an integer as a parameter (employee ID)
- Display progress information in the specified format
"""

import urllib.request
from sys import argv
import json
import requests
# get the commandline arg
argv_user_id = int(argv[1])

# build a url to get the userID witht the argv_user_id

url_employee_id = f"https://jsonplaceholder.typicode.com/todos/{argv_user_id}"

# set counter for tasks
count_all_task_for_argv = 0
NUMBER_OF_DONE_TASKS = 0
TASK_TITLE = ""

# extract user id

with urllib.request.urlopen(url_employee_id) as response:
    data_todo = json.loads(response.read().decode())

    # extract user name
    user_id = data_todo['id']

    # build a url with id gotten
    url_user_name = f"https://jsonplaceholder.typicode.com/users/{user_id}"

    with urllib.request.urlopen(url_user_name) as res:
        data_usernames = json.loads(res.read().decode())

        # store the argv user name to in var
        EMPLOYEE_NAME = data_usernames['name']

    # Task counter session
    url_count_tasks = f"https://jsonplaceholder.typicode.com/todos"

    with urllib.request.urlopen(url_count_tasks) as response:
        data_todo = json.loads(response.read().decode())

        # loop through data_todo and increment task
        for cont in range(len(data_todo)):
            if data_todo[cont]['userId'] == argv_user_id:
                count_all_task_for_argv += 1

        TOTAL_NUMBER_OF_TASKS = count_all_task_for_argv

        for cont in range(len(data_todo)):
            if data_todo[cont]['userId'] == argv_user_id\
              and data_todo[cont]['completed'] is True:
                NUMBER_OF_DONE_TASKS += 1

        for cont in range(len(data_todo)):
            if data_todo[cont]['userId'] == argv_user_id\
              and data_todo[cont]['completed'] is True:
                NUMBER_OF_DONE_TASKS += 1
            TASK_TITLE = data_todo[cont]['title']

# creat into json

api_url = "https://jsonplaceholder.typicode.com/"
user_url = "{}users/{}".format(api_url, argv_user_id)

todo_url = "{}todos?userId={}".format(api_url, argv_user_id)

user_response = requests.get(user_url)
user_data = user_response.json()
username = user_data['username']

todo_response = requests.get(todo_url)
todo_data = todo_response.json()

my_list = []
new_obj = {}

for todo in todo_data:
    new_obj = {
        "task": todo['title'],
        "completed": todo['completed'],
        "username": username
    }
    my_list.append(new_obj)

# create a dictionary with user id and the newly created list
new_dict = {str(argv_user_id): my_list}

filename = "{}.json".format(argv_user_id)
with open(filename, "w") as p:
    json.dump(new_dict, p)
