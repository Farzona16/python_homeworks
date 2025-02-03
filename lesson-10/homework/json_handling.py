import json
import csv
with open("tasks.json", 'r') as f:
    data = json.load(f)  
    for task in data:
        task_id = task.get("id")
        task_name = task.get("task")
        completed_status = task.get("completed")
        priority = task.get("priority")          
        print(f"ID: {task_id}, Task Name: {task_name}, Completed: {completed_status}, Priority: {priority}")
    data[0]["completed"]=False
with open("tasks.json", 'w') as f:
    json.dump(data,f,indent=4)
def calculate_statistics():
    total_task=len(data)
    print(f"The number of total tasks: {total_task}")
    completed_tasks=0
    not_completed=0
    priority=0
    for task in data:
        if task.get("completed", False):
            completed_tasks+=1
        else:
            not_completed+=1
        priority += task["priority"]
        av_priority=priority/len(data)
    print(f"Completed tasks: {completed_tasks}")
    print(f"Pending tasks: {not_completed} ")
    print(f"Average priority: {av_priority} ")
calculate_statistics()
with open("tasks.csv", 'w',newline='') as f:
    fieldnames=data[0].keys()
    writer=csv.DictWriter(f,fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)