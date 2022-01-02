from pathlib import Path
import os
import time 

def convert_in_miniflix_list(title, image, stream):
    if (len(title) > 3):    
        link = "<a href=\"javascript:html5Player('" + str(stream) + "','" + str(image) + "','" + str(title) + "')\">" + str(title) + "</a></br>\n\n"
        file = open("code.html", "a")
        file.write(link)

# Open file and run process
def open_m3u_file():
    file = open("miniflix.m3u", "r")
    
    file_content = ""
    
    try:
        file_content = file.readlines()
    except:
        print("Finish reading miniflix")

    i = 0 
    for item in file_content:
        
        string = str(item)
        string = string.replace("#EXTINF:-1 group-title=\"Mini-Flix MOVIES\" tvg-logo=\"","")
        string = string.replace("\" group-title=\"VOD","")
        
        hint = string.find(",")
        
        image = string[0:hint-1]

        try:
            stream = file_content[i + 1]  
        except:
            exit(0)

        stream = str(stream)

        title = string[hint:len(string)].replace(",", " ")
        title = title.strip()

        convert_in_miniflix_list(title, image, stream)

        i+=1

# Main list building process
def main_process():

    # User interaction mesg
    print("\n\n\n\nWelcome to mini-flix builder 1.0")
    print("Writen by SIM @ 2021")
    print("Contact : gfm.mail.72@gmail.com")
    print("________________________________")
    print("Memosasoft 28-11-2021")
    print("")
    print("Starting list merging process")
    print("The task will start soon please wait...")

    open_m3u_file()

main_process()