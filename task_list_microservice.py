# This is a microservice that will prioritize a list of tasks based on the following:
# A task will be sent with a title, due date, urgency score 1-10 and importance score 1-10.
# The algorithm for computing the priority score is as follows:
# due date will need to receive a score from 1-10 based on how far away from the current day it is.
# Same day = 10
# Next day = 9
# 2 days = 8
# 3 days - 7 days = 7
# 8 days - 14 days = 6
# 15 days - 21 days = 5
# 22 days - 28 days = 4
# 29 days -  60 days = 3
# 61 days -  180 days = 2
# 180 days < = 1
# Priority score = [ due_date_score (1-10) + Urgency score (1-10) + Importance score (1-10) ] * .333
# rounded to the nearest 10th

import datetime
import time
from datetime import date
from datetime import datetime, timedelta

while True:

    # open the tasks.txt file and copy the task list into a string
    with open('tasks.txt', 'r', encoding="utf-8") as tasks:
        task_list_string = tasks.read()
    tasks.close()

    # strip task character string of return line \n characters and convert each comma separated string into an item
    # in a list variable
    task_list = task_list_string.replace("\n", ",")
    task_list = list(task_list.split(","))

    # calculate today's date
    # determine number of items in the task list to sort
    today = date.today()
    num_tasks = int(len(task_list) / 4)
    priority_scores = []

    # this for loop goes through each individual task and calculates its priority score
    # the priority score and name of the task are added to the priority_scores list variable as a tuple (score,task)
    for num in range(num_tasks):
        item_num = 4 * num
        priority_score = 0
        priority_score += int(task_list[item_num + 2])
        priority_score += int(task_list[item_num + 3])
        date = datetime.strptime(task_list[item_num + 1], '%m-%d-%Y').date()
        days_due = today - date
        days_due = days_due.days
        if days_due == 0:
            priority_score += 10
        elif days_due == 1:
            priority_score += 9
        elif days_due == 2:
            priority_score += 8
        elif 2 < days_due <= 7:
            priority_score += 7
        elif 8 <= days_due <= 14:
            priority_score += 6
        elif 15 <= days_due <= 21:
            priority_score += 5
        elif 22 <= days_due <= 28:
            priority_score += 4
        elif 29 <= days_due <= 60:
            priority_score += 3
        elif 61 <= days_due <= 180:
            priority_score += 2
        else:
            priority_score += 1
        priority_score = priority_score / 3
        priority_score = round(priority_score, 1)
        priority_scores.append((priority_score, task_list[item_num]))

    # the priority score tuples in the priority_scores list are sorted in order from highest to lower
    priority_scores.sort(reverse=True)

    # priority output is created and a string a characters to print into the output .txt file is generated
    priority_output = ""
    for num in range(num_tasks):
        task_to_add = priority_scores[num]
        priority_output = priority_output + str(task_to_add[0]) + "," + str(task_to_add[1]) + "\n"

    # this section writes in the prioritized tasks into the prioritized_tasks.txt file, one task and priority score
    # per line
    with open('prioritized_tasks.txt', 'w', encoding="utf-8") as prioritized_tasks:
        prioritized_tasks.write(priority_output)
    prioritized_tasks.close()
