#!/usr/bin/python3
"""
Script to retrieve and display TODO list progress for a given employee
using a REST API.

Requirements:
- Use urllib or requests module
- Accept an integer as a parameter (employee ID)
- Display progress information in the specified format
"""

if __name__ == "__main__":

    import json
    from sys import argv
    import csv
    import requests
    import urllib.request

    # get the commandline arg
    argv_user_id = int(argv[1])

    # build a url to get the userID witht the argv_user_id
    u = f"https://jsonplaceholder.typicode.com/todos/{argv_user_id}"
    url_employee_id = u

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
                if data_todo[cont]['userId'] == argv_user_id and \
                        data_todo[cont]['completed']\
                        is True:
                    NUMBER_OF_DONE_TASKS += 1

            # print("Employee {} is done with tasks({}/{}):".format(
            #   EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))

            # print(TOTAL_NUMBER_OF_TASKS)
            for cont in range(len(data_todo)):
                if data_todo[cont]['userId'] == argv_user_id\
                                            and data_todo[cont]['completed']\
                                            is True:
                    NUMBER_OF_DONE_TASKS += 1
                    TASK_TITLE = data_todo[cont]['title']
                    # print("\t ", TASK_TITLE)

    # update the script to save to csv file

    # create user url and api
    user_id_arg = argv[1]
    api_url = "https://jsonplaceholder.typicode.com/"
    user_url = "{}users/{}".format(api_url, user_id_arg)
    user_response = requests.get(user_url)
    user_data = user_response.json()
    username = user_data['username']

    # create todos url and response from requests
    todo_url = "{}todos?userId={}".format(api_url, argv_user_id)
    todo_response = requests.get(todo_url)
    todo_data = todo_response.json()

    # create a file using the user id
    file_name = "{}.csv".format(user_id_arg)

    # declare an empty list
    my_list = []

    # loop through data gotten from todo and dynamically create strings
    for todo in todo_data:
        my_list.append([argv_user_id, username, todo['completed'],
                        todo['title']])

        # open a file on csv = write mode
        with open(file_name, "w", newline='') as play:
            data = csv.writer(play, delimiter=',', quotechar='"',
                              quoting=csv.QUOTE_ALL)

            # write the list inside the csv file
            data.writerows(my_list)
