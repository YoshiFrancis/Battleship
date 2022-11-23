import pandas as pd

musics = ["Classical", "Jazz", "Rap", "Pop", "Rock", "EDM", "Country", "Alternative", "Indie", "Cultural", "Lo-Fi", "Fortnite"]
gradeLevel = ["Senior", "Junior", "Sophmore", "Freshman"]
classes = {
    "Senior" : {},
    "Junior" : {},
    "Sophmore" : {},
    "Freshman" : {}
}

musicCount = {}
def main():
    for el_class in classes:
        for music in musics:
            musicCount[music] = 0
            classes[el_class][music] = {"count" : 0}

    cols = [0, 1, 2]
    excel_file = pd.read_excel("PythonAndExcelTesting.xlsx", usecols = cols)

    #stored all column headers/names in an array and stored in variable
    column_names = excel_file.columns.ravel()

    column_arrays = {}
    for column in column_names:
        column_arrays[column] = excel_file[column].tolist()
    
    #stored each column data in a variable for easier use later
    grade = column_arrays["What grade are you in?"]
    average_grade = column_arrays['What is your average grade in each class?']
    music = column_arrays['What type of music do you listen to while studying? (pick at most two)']

    #print(grade)
    #print(average_grade)
    #print(music)

    for x in range(0, len(grade)):
        # sets at a specific grade level (index which x is) of a specific music and the key will be the count number of the specific music 
        classes[grade[x]][music[x]][classes[grade[x]][music[x]]["count"]] = {
                "AvgGrade" : average_grade[x]
            }
        # increments count of total amount the music had been chosen in the specific class and overall
        classes[grade[x]][music[x]]["count"] += 1
        musicCount[music[x]] += 1

    #displays music information in each class
    for level in gradeLevel:
        print(f"This is the information for the {level}s")
        # to get the raw data
        #print(classes[level])
        for music in musics:
            print(music + ":")
            for i in range(0, classes[level][music]["count"]):
                print(f"Student {i + 1}:\nAverage Grade: {classes[level][music][i]['AvgGrade']}")
        
        print("\n")

    #displays the total count for each music genre
    print("This shows the total amount of music in total")
    for music in musics:
        print(f"{music}: {musicCount[music]}")


if __name__=="__main__":
    main()