Task List Microservice


In order to leverage this microservice, two .csv files must be in the program folder directory; tasks.csv
and prioritized_tasks.csv.
This microservice will always be running in the background. When the tasks.csv is filled with a list of tasks, the
microservice will then begin. It will evaluate the tasks lists based on the criteria described in the
task_list_microservice.py header comments and as given to me by my partner.
Once the tasks have been prioritized in the microservice, they will be written in order from the highest priority to
the lowest priority into the prioritized_tasks.csv file, with the priority score and task name and each line, separated
by a comma. Each task will be listed on a new line.
The tasks.csv file will not be modified in any way by this microservice.

An example is shown as follows below. The microservice receives the following from the tasks.txt file

Laundry,11-01-2023,9,7
Dishes,11-01-2023,6,5
Vacuuming,11-12-2023,10,10

The prioritized_task list will then return the following (if today's date is 2023-11-12:

10.0,Vacuuming
7.3,Laundry
5.7,Dishes


UML Sequence Diagram






