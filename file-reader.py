import json
class JSON():
    enterName = input ("Enter Your name")
    with open ("mydata.txt") as file_data:
        name =  json.load(file_data)
        if (name == enterName):
            print("Welcome back")
        else:
            with open ("mydata.txt",'w') as file_write:
                json.dump(enterName,file_write)