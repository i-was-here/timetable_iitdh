from flask import Flask, request, render_template,send_file
# import pdfschedule
import os
from courses_list import cse_sem5_dict as input_data

app = Flask(__name__) 


def day_code(ip_day):
    if(ip_day=="MON"): return "M"
    elif(ip_day=="TUE"): return "T"
    elif(ip_day=="WED"): return "W"
    elif(ip_day=="THU"): return "H"
    elif(ip_day=="FRI"): return "F"
    elif(ip_day=="SAT"): return "Sa"
    elif(ip_day=="SUN"): return "Su"
    else: Exception("Please enter a valid day !")

@app.route('/', methods =["GET", "POST"])
def gfg():
    if request.method == "POST":
       # getting input with name = fname in HTML form
        cd = request.form.get("cd")
        
        courses = cd.split()
        chosen_courses = {i:input_data[i] for i in input_data.keys() if i in courses}
        with open("timetable.yaml", "wt") as out_file:
            for key, value in chosen_courses.items():
                for day_time in value:
                    out_file.write("- name: "+key+"\n")

                    # use the below line for when a course has same time for all the diven days
                    # out_file.write("  days: "+"".join([day_code(i[0]) for i in value])+"\n")

                    out_file.write("  days: "+day_code(day_time[0])+"\n")
                    out_file.write("  time: "+day_time[1]+"\n\n")
                    
        
        os.system("pdfschedule timetable.yaml")
        path = "timetable.pdf"
        return send_file(path, as_attachment=True)
        
    return render_template("index.html")
    


if __name__=="__main__":
    app.run()