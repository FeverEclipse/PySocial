# Welcome To My Social Network Project! - Eyup Menevse

import sys

# Defining Necessary Variables
counter = 0
output_file = open("output.txt", "w")

# Creating Necessary Lists and Dictionaries
user_list = {}
command_list = []

# Append Users to User List
with open("{}".format(sys.argv[1])) as i:
    for line in i:
        line = line.rstrip("\n")
        user_list[line.split(":")[0]] = line.split(":")[1].split(" ")

# Check Commands From Text File
with open("{}".format(sys.argv[2])) as commands:
    for line in commands:
        line = line.rstrip("\n")
        command = line.split(" ")[0]
        command_content = line.split(" ", 1)[1]

        # Categorize The Commands and Execute Them
        if command == "ANU":

            # Checking If The Input Meet The Conditions
            if command_content not in user_list:
                # Adding The User
                user_list[command_content] = []
                output_file.write("User '{}' has been added to the social network successfully\n".format(command_content))

            else:
                output_file.write("ERROR: Wrong input type! for 'ANU’! -- This user already exists!!\n")

        elif command == "DEU":

            # Checking If The Input Meet The Conditions
            if command_content in user_list:

                # Deleting The User and Its Relations
                for user in user_list:
                    for friend in user_list[user]:
                        if friend == command_content:
                            user_list[user].remove(friend)
                del user_list[command_content]
                output_file.write("User '{}' and his/her all relations have been deleted successfully\n".format(command_content))
            else:
                output_file.write("ERROR: Wrong input type! for 'DEU'!--There is no user named '{}'!!\n".format(command_content))

        elif command == "ANF":

            # Defining Source and Target Users
            source_friend = line.split(" ")[1]
            target_friend = line.split(" ")[2]

            # Checking If The Inputs Meet The Conditions
            if source_friend in user_list:
                if target_friend in user_list:
                    if target_friend not in user_list[source_friend] and source_friend not in user_list[target_friend]:
                        # Creating a Relation Between The Users
                        user_list[source_friend].append(target_friend)
                        user_list[target_friend].append(source_friend)
                        output_file.write("Relation between '{}' and '{}' has been added successfully\n".format(source_friend, target_friend))
                    else:
                        output_file.write("ERROR: A relation between '{}' and '{}' already exists!!\n".format(source_friend, target_friend))

                else:
                    output_file.write("ERROR: Wrong input type! for 'ANF'! -- No user named '{}' found!!\n".format(target_friend))
            else:
                if target_friend not in user_list:
                    output_file.write("ERROR: Wrong input type! for 'ANF'! -- No user named '{}' and '{}' found!\n".format(source_friend, target_friend))
                else:
                    output_file.write("ERROR: Wrong input type! for 'ANF'! -- No user named '{}' found!!\n".format(source_friend))

        elif command == "DEF":

            # Defining Source and Target Users
            source_friend = line.split(" ")[1]
            target_friend = line.split(" ")[2]

            # Checking If The Inputs Meet The Conditions
            if source_friend in user_list and target_friend in user_list:
                if target_friend in user_list[source_friend]:

                    # Removing The Relation Between The Users
                    user_list[source_friend].remove(target_friend)
                    user_list[target_friend].remove(source_friend)
                    output_file.write("Relation between '{}' and '{}' has been deleted successfully\n".format(source_friend, target_friend))
                else:
                    output_file.write("ERROR: No relation between '{}' and '{}' found!!\n".format(source_friend, target_friend))
            elif source_friend and target_friend not in user_list:
                output_file.write("ERROR: Wrong input type! for 'DEF'! -- No user named '{}' and '{}' found!\n".format(source_friend, target_friend))
            if source_friend in user_list and target_friend not in user_list:
                output_file.write("ERROR: Wrong input type! for 'DEF'! -- No user named '{}' found!\n".format(target_friend))
            if target_friend in user_list and source_friend not in user_list:
                output_file.write("ERROR: Wrong input type! for 'DEF'! -- No user named '{}' found!\n".format(source_friend))

        elif command == "CF":

            # Checking If The Input Meet The Conditions
            if command_content in user_list:

                # Writing The Friend Count Of The Given User
                output_file.write("User '{}' has {} friends\n".format(command_content, len(user_list[command_content])))
            else:
                output_file.write("ERROR: Wrong input type! for 'CF'! -- No user named '{}' found!\n".format(command_content))

        elif command == "FPF":

            # Defining Necessary Variables and Lists
            user_name = line.split(" ")[1]
            distance = int(line.split(" ")[2])
            possible_friend_list = []

            # Checking If The Inputs Meet The Conditions
            if user_name in user_list and distance <= 3:

                # Finding Possible Friends and Outputting Them
                if distance == 1:
                    for user in user_list[user_name]:
                        for distance_1 in user_list[user]:
                            if distance_1 not in possible_friend_list and distance_1 != user_name and distance_1 != '':
                                possible_friend_list.append(distance_1)
                    output_file.write("User '{}' has {} possible friends when maximum distance is {}\n".format(user_name, len(possible_friend_list), distance))
                    sorted_and_edited_list = str(possible_friend_list.sort())
                    sorted_and_edited_list.replace("[","{")
                    sorted_and_edited_list.replace("]","}")
                    output_file.write("These possible friends: {}\n".format(sorted_and_edited_list))

                elif distance == 2:
                    for user in user_list[user_name]:
                        for distance_1 in user_list[user]:
                            if distance_1 not in possible_friend_list and distance_1 != user_name and distance_1 != '':
                                possible_friend_list.append(distance_1)
                            for distance_2 in user_list[distance_1]:
                                if distance_2 not in possible_friend_list and distance_2 != user_name and distance_2 != '':
                                    possible_friend_list.append(distance_2)
                    output_file.write("User '{}' has {} possible friends when maximum distance is {}\n".format(user_name, len(possible_friend_list), distance))
                    output_file.write("These possible friends: {}\n".format(sorted(possible_friend_list)))

                elif distance == 3:
                    for user in user_list[user_name]:
                        for distance_1 in user_list[user]:
                            if distance_1 not in possible_friend_list and distance_1 != user_name and distance_1 != '':
                                possible_friend_list.append(distance_1)
                            for distance_2 in user_list[distance_1]:
                                if distance_2 not in possible_friend_list and distance_2 != user_name and distance_2 !='':
                                    possible_friend_list.append(distance_2)
                                if distance_2 != '':
                                    for distance_3 in user_list[distance_2]:
                                        if distance_3 not in possible_friend_list and distance_3 != user_name and distance_3 != '':
                                            possible_friend_list.append(distance_3)
                    output_file.write("User '{}' has {} possible friends when maximum distance is {}\n".format(user_name, len(possible_friend_list), distance))
                    output_file.write("These possible friends: {}\n".format(sorted(possible_friend_list)))
            if user_name not in user_list:
                output_file.write("ERROR: Wrong input type! for 'FPF'! -- No user named {} found!\n".format(user_name))
            if distance not in range(1,4):
                output_file.write("ERROR: Wrong input type! for 'FPF'! -- Distance is out of range!\n")

        elif command == "SF":

            # Defining Necessary Variables and Lists
            user_name = line.split(" ")[1]
            MD = int(line.split(" ")[2])
            check_list = []
            suggest_friend_list = {}

            counter = 0

            # Checking If The Inputs Meet The Conditions
            if user_name in user_list and MD in range(1,5):

                # Suggesting Friends To User
                for friend in user_list[user_name]:
                    for friend2 in user_list[friend]:
                        if friend2 not in check_list and user_list[user_name]:
                            check_list.append(friend2)

                for check_item in check_list:
                    for friend in user_list[user_name]:
                        if check_item in user_list[friend] and check_item != user_name and check_item != '':
                            counter += 1
                    if counter >= MD:
                        suggest_friend_list[check_item] = counter
                    counter = 0
                sorted_keys = list(suggest_friend_list.keys())
                sorted_keys.sort()
                output_file.write("Suggestion List for '{}' (when MD is {}):\n".format(user_name, MD))

                for item in sorted_keys:
                    output_file.write("'{}'  has '{}' mutual friends with '{}'\n".format(user_name, suggest_friend_list[item], item))
                output_file.write("The suggested friends for '{}':{}\n".format(user_name, list(suggest_friend_list.keys())))

            elif user_name not in user_list:
                output_file.write("Error: Wrong input type! for 'SF'! -- No user named '{}' found!!\n".format(user_name))
            if MD not in range(1,5):
                output_file.write("Error: Mutually Degree cannot be less than 1 or greater than 4\n")
output_file.close()