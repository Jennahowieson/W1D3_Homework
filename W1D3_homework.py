tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]

# Print a list of uncompleted tasks
def uncompleted_tasks(list):
    uncompleted = []

    for task in list:
        if task ["completed"] == False:
            uncompleted.append(task)
    return uncompleted
print (uncompleted_tasks(tasks))


# Print a list of completed tasks
def completed_tasks(list):
    completed = []

    for task in list:
        if task ["completed"] == True:
            completed.append(task)
    return completed
print (completed_tasks(tasks))


# Print a list of all task descriptions
def task_description(list):
    descriptions = []
    for task in list:
        descriptions.append(task["description"])
    return descriptions
print (task_description(tasks))


# Print a list of tasks where time_taken is at least a given time
def task_time(list,time):
    long_tasks= []
    for task in list:
        if task["time_taken"] > time:
            long_tasks.append(task)
    return long_tasks
print (task_time(tasks,25))


# Print any task with a given description
def task_desc(list, job):
    results = []
    for task in list: 
        if task["description"] == job:
            results.append(task)
        return results
print (task_desc(tasks, "Make Dinner"))
    
# Extension
# Given a description update that task to mark it as complete.
# def task_complete(list, desc):
#     for task in list:
#         if status == desc:
#             task["completed"] = True
#     return task["completed"]
# print(task_complete(tasks,"Feed Cat"))

# Add a task to the list