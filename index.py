def day_code(ip_day):
    if(ip_day=="MON"): return "M"
    elif(ip_day=="TUE"): return "T"
    elif(ip_day=="WED"): return "W"
    elif(ip_day=="THU"): return "H"
    elif(ip_day=="FRI"): return "F"
    elif(ip_day=="SAT"): return "Sa"
    elif(ip_day=="SUN"): return "Su"
    else: Exception("Please enter a valid day !")

if __name__=="__main__":
    input_data  = {
        "CS303": [("TUE", "10:30-11:30"), ("WED", "09:30-14:30"), ("THU", "09:30-10:30")],
        "CS301": [("MON", "15:00-16:00"), ("WED", "13:00-16:00"), ("FRI", "16:00-17:00")],
        "CS311": [("WED", "10:30-13:30")],
        "PH401": [("TUE", "14:00-15:00"), ("WED", "14:00-15:00"), ("FRI", "19:00-20:00")]
    }

    courses = input("Please enter course codes of your courses : ").split()

    chosen_courses = {i:input_data[i] for i in input_data.keys() if i in courses}

    with open("timetable.yaml", "wt") as out_file:
        for key, value in chosen_courses.items():
            for day_time in value:
                out_file.write("- name: "+key+"\n")

                # use the below line for when a course has same time for all the diven days
                # out_file.write("  days: "+"".join([day_code(i[0]) for i in value])+"\n")

                out_file.write("  days: "+day_code(day_time[0])+"\n")
                out_file.write("  time: "+day_time[1]+"\n\n")