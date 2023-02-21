# StudyEnvironment

## Description
This project is the study environment for the students, where the application has two parts, to-do list and the timer. It will be useful for the student who needs to pay attention to their study. The application will furthermore remember the to-do list according to their account. Thus, this application will also include log-in functionality. This programming process was brought from the course I took, CPSC 210 Software Engineering in University of British Columbia. The project is divided into 4 different phases: 1) console based application, 2) data persistence, 3) GUI, 4) EventLog and theoreticals. However I have moved the EventLog part to the second phase and the fourth phase will be on filling up gaps, looking more bugs and making the program more robust.

## User Stories
- As an user, I want to be able to register for an account
- As an user, I want to be able to log in
- As an user, I want to be able to add tasks to my to-do list
- As an user, I want to be able to edit my profile
- As an user, I want to be able to delete my account

## Phase 1 (Console Based Application)
- [x] construct model package and its necessary classes
    - [x] Account, Task, Tasks, etc classes
- [ ] construct ui package and its necessary classes (console base)
    - [x] log in (and retrieving tasks when logged in)
    - [x] register
    - [x] log out
    - [x] add task
- [x] construct tests for each and every model classes
- [x] construct exceptions
- [x] add a TaskComponent class so that tasks can have a sub-tasks (try Composite design pattern)
- [ ] add a timer to keep track of study time

## Phase 2 (Data Persistance)
- [x] add a super class of Account so that the data can be persisted in json(Recordable)
- [x] add a folder called 'data' so that the json files can be organized
- [x] appropriately modify each Task and Tasks class to be persisted
- [ ] add a log functionality so that it records each activity taken (try Singleton design pattern)


## Daily log
(... no record)
*01/03/23*
- Created and modified Account and Recordable classes
    - Recordable class was for data persistance which was supposed to be done in Phase 2
    - Applied inheritence
- Added toJson() methods in both Task and Tasks classes so that the data from each class can be neatly persisted
- Added data package/folder for the json files

*01/06/23*
- Created a Subject class
    - This class is a study task (inheritance) for a given subject with the time allocated to study
- Created a TaskComponent class 
    - Applied Composite Desgin Pattern
- Rendered TasksTest class

*01/08/23*
- Finished up tests

*01/12/23*
- Started constructing StudyEnvironment class
- Had trouble with "log in" functionality but **fixed**
    - after registration and adding a task, logging in and retrieving the tasks was not successful
- Added registration method
- In need of adding section (or tasks inside of tasks) and study task (or subject)

*02/21/2023*
- From *01/12/23* till now, have been editing the scripts; deleted some classes and fixed up certain data persistence mechanism
- Added tasks list and adder frame on the left of the screen
- Had trouble with fromJson() and toJson() methods, since when froJson() is called, each Task data is not converted to Task class. - *fixed; but needs to be analyzed further*
- wants to change the design of the menubutton/button of each task