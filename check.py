# decision=0
# def whatNext():
#     choice=input("Enter your choice\n n for next or \d for done")
#     if choice=="n":
#         decision=True
#     if choice=="d":
#         decision=False
#     while(decision):

#         def addTask(task_list):
#             title = input("Task name please:")
#             description = input("What's that about:")
#             dueDate = input("Enter like (YYYY-MM-DD):")
#             priority = input("Priority (e.g. High, Medium, Low):")

#             dictask = {
#                 'title': title,
#                 'description': description,
#                 'dueDate': dueDate,
#                 'priority': priority,
#                 'completed': False  # Added a 'completed' field, initially set to False
#             }

#             task_list.append(dictask)


#         def view(task_list):
#             for index,element in enumerate(task_list):
#                 print(f"Sno:{index}")
#                 print(f"Title: {element['title']}")  # Display the task title
#                 print(f"Due Date: {element['dueDate']}")
#                 print(f"Mention the priority{element['priority']}")
#                 print(f"Status ::{'Yes'if element['completed']else 'No'}")
            

#         def editTask(task_list):
#             view(task_list)  # Display tasks to the user for selection
#             task_index = int(input("Enter the task number you want to edit: "))

#             if 0 <= task_index < len(task_list):
#                 task = task_list[task_index]
#                 print("Current Task Details:")
#                 view([task])  # Display selected task details
#                 field = input("Enter the field you want to edit (title, description, dueDate, priority, completed): ")
#                 new_value = input("Enter the new value: ")

#                 # Update the selected field
#                 if field in task:
#                     task[field] = new_value
#                     print("Task updated successfully!")
#                 else:
#                     print("Invalid field name.")
#             else:
#                 print("Invalid task number.")


#         t1 = []  # Initialize an empty list to store tasks

#         # Now you can use these functions to manage your tasks

#         addTask(t1)
#         view(t1)


#     # editTask(t1)
#     # view(t1)

import pyodbc

# Establish connection with the mssql server


# decision = True  # Initialize decision to True

# def whatNext():
#     global decision  # Use global to modify the outer 'decision' variable
#     choice = input("Enter your choice\n n for task or \n d for done \n")
#     if choice == "n":
#         decision = True
#     if choice == "d":
#         decision = False

def addTask(task_list):
    title = input("Task name please:")
    description = input("What's that about:")
    dueDate = input("Enter like (YYYY-MM-DD):")
    priority = input("Priority (e.g. High, Medium, Low):")

    conn = pyodbc.connect('DRIVER={SQL Server};'
                    'SERVER=DESKTOP-4OBRHG1\MSSQLSERVER01;'
                    'DATABASE=Tasks;'
                    'Trusted_Connection=yes;'
                    )
    cursor = conn.cursor()
    insert_query = """
    INSERT INTO Tasks (title, description, dueDate, priority, completed)
    VALUES (?, ?, ?, ?, ?)
    """

    # Execute the query with task details
    cursor.execute(insert_query, title, description, dueDate, priority, False)
    conn.commit() 
    # for i in cursor:
    #     print(i)

    dictask = {
        'title': title,
        'description': description,
        'dueDate': dueDate,
        'priority': priority,
        'completed': False  # Added a 'completed' field, initially set to False
    }

    task_list.append(dictask)



def view(task_list):
    # for index, element in enumerate(task_list):
        # print(f"Sno:{index}")
        # print(f"Title: {element['title']}")  # Display the task title
        # print(f"Due Date: {element['dueDate']}")
        # print(f"Mention the priority{element['priority']}")
        # print(f"Status ::{'Yes' if element['completed'] else 'No'}")

    conn = pyodbc.connect('DRIVER={SQL Server};'
            'SERVER=DESKTOP-4OBRHG1\MSSQLSERVER01;'
            'DATABASE=Tasks;'
            'Trusted_Connection=yes;'
            )
    cursor = conn.cursor()
    select_query = """
    SELECT * from Tasks
    """

    # Execute the query with task details
    cursor.execute(select_query) # WAS STUCK at this haha and debug later!!!!!!!!! 

    # conn.commit() commenting as it's not required while showing to the user
    rows = cursor.fetchall() # Fetching all of the rows..

    for row in rows:
        print(row)
    cursor.close()
    conn.close()


def editTask(task_list):
    view(task_list)  # Display tasks to the user for selection
    task_index = int(input("Enter the task number you want to edit: "))

    if 0 <= task_index < len(task_list):
        task = task_list[task_index]
        print("Current Task Details:")
        view([task])  # Display selected task details
        field = input("Enter the field you want to edit (title, description, dueDate, priority, completed): ")
        new_value = input("Enter the new value: ")

        # Update the selected field
        if field in task:
            task[field] = new_value
            print("Task updated successfully!")
        else:
            print("Invalid field name.")
    else:
        print("Invalid task number.")


t1 = []  # Initialize an empty list to store tasks

cond=True
while cond:  # Use a loop to repeatedly ask for user input
    a=input("Enter 'y'if you want to see,add tasks or\n 'e'to edit the existing tasks\n")
    if a=="y":
        addTask(t1)
        view(t1)
        choice=input("Enter 'd' to done or press any other key to continue:")
        if choice == "d":
            break
    elif a=="e":
        editTask(t1)
    elif a=="q":
        cond=False

    