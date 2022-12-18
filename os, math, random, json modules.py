import os
import math

#OS module handles directories, changing dirs, making subdirs, and operates mainly with dirs

#print(os.getcwd())
#os.chdir("D:\\Python\\Py_Scripting")
#print(os.getcwd())

#make sub-directory
#os.mkdir("D:\\Python\\Py_Scripting\\SubDir")
#remove subdir
#os.rmdir("D:\\Python\\Py_Scripting\\SubDir")

#remove the directories
#os.remove("C:\\Users\\HP\\PycharmProjects\\Python Scripting\\SysModule.py")

#join os module path to the directory
#print(os.path.join("C:\\Users\\HP\\PycharmProjects\\Python Scripting", "C:\\Users\\HP\\PycharmProjects\\Python Scripting\\os, math, random, json modules.py"))

#split fxn
#print(os.path.split("C:\\Users\\HP\\PycharmProjects\\Python Scripting\\OSmodule"))

#Does the path exist
#print(os.path.exists("C:\\Users\\HP\\PycharmProjects\\Python Scripting"))

#Mathematical operations karenge math module se
#print(math.trunc(4.1))

import random

#print(random.randrange(0, 45, 5))

import datetime

#print(datetime.datetime.today())
#now = datetime.datetime.today()
#past = datetime.datetime(1994, 10, 10, 17, 59)
#print(now - past)

import json

#employee_data ='''
#{
#"people":[
#{
#"name": "Jack",
#"mailid": ["jck@gmail.com", "jc@gmail.com"],
#"salary": false
#},
#{
#"name": "Jill",
#"mailid": ["jll@gmail.com", "ji@gmail.com"],
#"salary": true
# }
#]
#}


#print json file
#print(employee_data)

#json file ko py file mein convert kar diya
#data =json.loads(employee_data)
#print(data)






