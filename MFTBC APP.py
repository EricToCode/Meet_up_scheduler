from app_functions import *
user_c = [[], [], [], [], []]
user_j = [[], [], [], [], []]

account = None
while account != 'x':
    account = input("If you already have an account press 1 \n to create account press 2 \nor x to exit \n")
    if account == '1':
        user = input("What's your name?: ")
        task = None
        while task != 'x':
            task = input("Click 1 to edit classes to schedule \n click 2 to compare schedules \nor x to exit \n")
            if task == '1':
                inp = input('press 1 to add a class or x to exit \n')
                while inp != 'x':
                    schedule_user = [[],[],[],[],[]]
                    new_class = input("Enter the start time of the class, end time, day of class\nfor day:\n1 if monday\n2 if tuesday\n...\n5 if friday\n")
                    new_class_list = new_class.split(',')
                    new_class_list[2] = int(new_class_list[2]) - 1
                    schedule_user[new_class_list[2]].append(convert_time(new_class_list[0], new_class_list[1]))
                    inp = input('press 1 to add a class or x to exit \n')
                    
            elif task == '2':
                blocks_user = [[], [], [], [], []]
                for day in schedule_user:
                    for course in day:
                        if course[1] - course[0] == 2:
                            (course[0] - 8.25) / 0.5
                
                

            task = input("Click 1 to edit classes to schedule \n click 2 to compare schedules \nor x to exit \n")
    account = input("If you already have an account press 1 \n to create account press 2 \nor x to exit \n")
print('program terminated')
