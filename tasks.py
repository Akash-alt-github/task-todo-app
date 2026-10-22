import json
import datetime

try:
    with open("doc.json","r+",encoding="utf-8") as task:
        all_tasks = json.load(task)


    # for index, t in enumerate(all_tasks):
    #     print(f"{t['task_name']}, {index}")


    # get_task = int(input("Enter the task number: "))

    # if get_task:
    #     print(all_tasks[get_task]['task_name'])

    get_number = int(input("For Viewing Task Enter 1, Adding Enter 2, Editing Enter 3, Deleting Enter 4 : "))

    if get_number:

        if get_number== 1:
            print("All Tasks: ")
            for index, t in enumerate(all_tasks):

                status = "Done" if t["is_done"] else "Pending"
                print(f"No. {index+1}: {t['task_name']}. - {status}")

        elif get_number== 2:
            new_task = input("Write the new task: ")
            is_done = False
            created_at = datetime.datetime.now().isoformat()
            updated_at = datetime.datetime.now().isoformat()

            new_task_dict = {
            "task_name": new_task,
            "is_done": is_done,
            "created_at": created_at,
            "updated_at": updated_at
            }

            all_tasks.append(new_task_dict)
            print(all_tasks)

            json_string = json.dumps(all_tasks)
            with open("doc.json","w") as task:
                task.write(json_string)

        elif get_number== 3:
            get_task = int(input("Enter the task number you want to edit: "))

            if get_task:
                old_task = all_tasks[get_task-1]['task_name']
                edited_task = input(f"Edit: {old_task} -> ")
                is_done = bool(input("Enter 'Done' if it is done, else ignore and 'enter': "))
                updated_at = datetime.datetime.now().isoformat()

                all_tasks[get_task-1]['task_name'] = edited_task
                all_tasks[get_task-1]['is_done'] = is_done
                all_tasks[get_task-1]['updated_at'] = updated_at

                json_string = json.dumps(all_tasks)
                with open("doc.json","w") as task:
                    task.write(json_string)


        elif get_number== 4:
            get_task = int(input("Enter the task number you want to delete: "))

            if get_task:
                all_tasks.pop(get_task-1)
                print(all_tasks)
                json_string = json.dumps(all_tasks)
                with open("doc.json","w") as task:
                        task.write(json_string)

except:
    print("Invalid Database....")       

    
