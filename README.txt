Communication Contract
In order to leverage this microservice, two .csv files must be in the program folder directory; tasks.csv
and prioritized_tasks.csv.
This microservice will always be running in the background. When the tasks.csv is filled with a list of tasks, the
microservice will then begin. It will evaluate the tasks lists based on the criteria described in the
task_list_microservice.py header comments and as given to me by my partner.
Once the tasks have been prioritized in the microservice, they will be written in order from the highest priority to
the lowest priority into the prioritized_tasks.csv file. Each task will be listed on a new line.
The tasks.csv folder will be cleared once the prioritized_tasks.csv file is written.


