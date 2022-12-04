import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import decimal

musics = ["Classical", "Jazz", "Rap", "Pop", "Rock", "EDM", "Country", "Alternative", "Indie", "Cultural", "Lo-Fi", "Fortnite"]
gradeLevel = ["Senior", "Junior", "Sophomore", "Freshman"]
classes = {
    "Senior" : {},
    "Junior" : {},
    "Sophomore" : {},
    "Freshman" : {}
}

musicCount = {}
def main():
    for el_class in classes:
        for music in musics:
            musicCount[music] = 0
            classes[el_class][music] = {
                "count" : 0,
                "GPA_AVG" : 0,
                "ACT_AVG": 0
                }

    cols = [1, 2, 3, 4]
    excel_file = pd.read_excel("Music and Grades in CBhS (Responses).xlsx", usecols = cols)

    #stored all column headers/names in an array and stored in variable
    column_names = excel_file.columns.ravel()

    column_arrays = {}
    for column in column_names:
        column_arrays[column] = excel_file[column].tolist()
    
    #stored each column data in a variable for easier use later
    grade = column_arrays["What grade are you in?"]
    average_grade = column_arrays['What is your average grade in each class?']
    music = column_arrays['What type of music do you listen to while studying? (pick at most two)']
    act = column_arrays["If you have taken the ACT, please pick which value corresponds with your score."]

    #print(grade)
    #print(average_grade)
    #print(music)

    for x in range(0, len(grade)):
        
        if ',' in music[x]:
            copy = music[x][:].split(", ")
            classes[grade[x]][copy[0]][classes[grade[x]][copy[0]]["count"]] = {
                "AvgGrade" : average_grade[x],
                "ACT" : act[x],
                "_AvgGrade": get_avg_grade(average_grade[x]),
                "_AvgACT": get_avg_act(act[x])
            }
            classes[grade[x]][copy[1]][classes[grade[x]][copy[1]]["count"]] = {
                "AvgGrade" : average_grade[x],
                "ACT" : act[x],
                "_AvgGrade": get_avg_grade(average_grade[x]),
                "_AvgACT": get_avg_act(act[x])
            }
            classes[grade[x]][copy[0]]["count"] += 1
            classes[grade[x]][copy[1]]["count"] += 1
            musicCount[copy[0]] += 1
            musicCount[copy[1]] += 1

        else:
            classes[grade[x]][music[x]][classes[grade[x]][music[x]]["count"]] = {
                "AvgGrade" : average_grade[x],
                "ACT" : act[x],
                "_AvgGrade": get_avg_grade(average_grade[x]),
                "_AvgACT": get_avg_act(act[x])
            }
            classes[grade[x]][music[x]]["count"] += 1
            musicCount[music[x]] += 1



        # sets at a specific grade level (index which x is) of a specific music and the key will be the count number of the specific music 
        
        # increments count of total amount the music had been chosen in the specific class and overall


    print_all_class_info()
    plot_graphs()

    #displays the total count for each music genre
    #print_count()
    


def print_all_class_info():
    for level in gradeLevel:
        print(f"------------This is the information for the {level}s------------")
        # to get the raw data
        for music in musics:
            gpa_sum = 0
            act_sum = 0
            ACTcount = classes[level][music]["count"]
            print("                                                         " + music + ":")
            for i in range(0, classes[level][music]["count"]):
                gpa_sum += classes[level][music][i]['_AvgGrade'] 
                if classes[level][music][i]['_AvgACT'] == 0:
                    ACTcount -= 1
                    continue   
                act_sum += classes[level][music][i]['_AvgACT']
            
            if classes[level][music]["count"] == 0: 
                continue
            classes[level][music]["GPA_AVG"] = gpa_sum / classes[level][music]["count"]
            if ACTcount == 0:
                ACTcount = 1
            classes[level][music]["ACT_AVG"] = act_sum / ACTcount
            print(f'Average GPA: {round(classes[level][music]["GPA_AVG"], 2)}')
            print(f'Average ACT: {round(classes[level][music]["ACT_AVG"], 2)}')
        #print(classes[level])
        
                


#displays music information in each class
def print_class_info():
    for level in gradeLevel:
        print(f"------------This is the information for the {level}s------------")
        # to get the raw data
        print(classes[level])
        for music in musics:
            print("                                                         " + music + ":")
            for i in range(0, classes[level][music]["count"]):
                print(f"Student {i + 1}:\nAverage Grade: {classes[level][music][i]['AvgGrade']}")
                print(f"Recorded ACT: {classes[level][music][i]['ACT']}")
        
        print("\n")

def plot_graphs():
    for level in gradeLevel:
        print(f"------------This is the information for the {level}s------------")
        # to get the raw data
        #print(classes[level])

        gpa_info = {}
        act_info = {}

        x_gpa = []
        y_gpa = []

        x_act = []
        y_act = []

        for music in musics:
            for i in classes[level][music]:
                if "GPA" in str(i):
                    #print(i, type(classes[level][music][i]))
                    x = classes[level][music][i]
                    gpa_info[music] =  round(x, 2)
                if "ACT" in str(i):
                    #print(i, type(classes[level][music][i]))
                    
                    x = classes[level][music][i]
                    act_info[music] = round(x, 2)

        info = sorted(gpa_info.items(), key=lambda kv:
            (kv[1], kv[0]))
        
        for i in info:
            x_gpa.append(i[0])
            y_gpa.append(i[1])

        info = sorted(act_info.items(), key=lambda kv:
            (kv[1], kv[0]))
        
        for i in info:
            x_act.append(i[0])
            y_act.append(i[1])

        #print(x_act, y_act)
        #plt.bar(np.array(x_gpa), np.array(y_gpa))
        #plt.show()

        fig, ax = plt.subplots()
        
        
        #ax.set_ylabel('GPA')
        #ax.set_xlabel("Music")
        #ax.set_title(f"{level} Class")

        #plt.bar(np.array(x_gpa), np.array(y_gpa))
        #plt.ylim(top=100)
        #plt.show()



        ax.set_ylabel('ACT Scores')
        ax.set_xlabel("Music")
        ax.set_title(f"{level} Class")

        plt.bar(np.array(x_act), np.array(y_act))
        plt.ylim(top=36)
        plt.show()


def get_avg_grade(grade):
    if "90" in grade:
        return 95
    elif "80" in grade:
        return 85
    elif "70" in grade:
        return 75
    else:
        return 65

def get_avg_act(act):
    if "33" in act:
        return 34.5
    elif "30" in act:
        return 31
    elif "26" in act:
        return 27.5
    elif "23" in act:
        return 24
    elif "19" in act:
        return 20.5
    elif "15" in act:
        return 16.5
    elif "11" in act:
        return 12.5
    elif "1" in act:
        return 3.5
    else:
        return 0

def print_count():
    print("This shows the total amount of music in total")
    for music in musics:
        print(f"{music}: {musicCount[music]}")


if __name__=="__main__":
    main()