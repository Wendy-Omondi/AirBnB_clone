# **AirBnB_clone**

## **Project Description**

## **The Console**
Contains the entry point of the command interpreter
#### **How to start it**
Start the console by running the executable python modue i.e ./console.py
#### **How to use it**
To use the console in interactuve mode, run the executable file console.py as shown in the example below
Enter the command `quit` to exit the console
An empty line + Enter executes anything

#### **Example**
```
vagrant@vagrant-ubuntu-trusty-64:~/AirBnB$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb) help quit
Quit command to exit the program

(hbnb) 
(hbnb) 
(hbnb) quit 
vagrant@vagrant-ubuntu-trusty-64:~/AirBnB$

```
## **Console Commands**                                                                                                            
#### **create**                                                                                                             
Creates a new instance of `BaseModel`, saves it (to a JSON file) and prints the `id.`                                      
``` Ex: $ create BaseModel```                                                                                              
#### **show:**                                                                                                               
Prints the string representation of an instance based on the class name and `id.`                                          
```Ex: $ show BaseModel 1234-1234-1234.```                                                                                 
###### **destroy:**                                                                                                        
Deletes an instance based on the class name and `id` (saves the change into the JSON file).                                
```Ex: $ destroy BaseModel 1234-1234-1234.```                                                                              
###### **all:**                                                                                                          
Prints all string representation of all instances based or not on the class name.                                          
```Ex: $ all BaseModel or $ all.```                                                                                        
###### update:**                                                                                                        
Updates an instance based on the class name and `id` by adding or updating attribute (saves the change into the JSON file).
```Ex: $ update BaseModel 1234-1234-1234 email "aibnb@holbertonschool.com".```                                             

## **Author**

Wendy Omondi <w.omondi19@launchpad.com>