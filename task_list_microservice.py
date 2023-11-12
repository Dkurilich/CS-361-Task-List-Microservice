# This is a microservice that will prioritize a list of tasks based on the following:
# A task will be sent with a title, due date, urgency score 1-10 and importance score 1-10.
# The algorithm for computing the priority score is as follows:
# due date will need to receive a score from 1-10 based on how far away from the current day it is.
# Same day = 10
# Next day = 9
# 2 days = 8
# 1 week - 4 weeks = 7-4 respectively
# 4 weeks - 2 months = 3
# 2 months - 6 months = 2
# anything greater than 6 months = 1


