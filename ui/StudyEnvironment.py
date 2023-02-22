import tkinter as tk
import sys
sys.path.append("/Users/yushinnam/Desktop/python3/StudyEnvironment/model")
from Account import Account 
from Accounts import Accounts 
from Tasks import Tasks
from Task import Task

class StudyEnvironment(tk.Tk):

    def __init__(self) -> None:
        self.accountList = Accounts()
        self.account = None
        super().__init__()
        self.title("Study Environment")
        self.geometry("600x400+600+300") # was 700x400
        self.resizable(width=False, height=False)


        self.logIntWindow()
    

    def logIntWindow(self) -> None:
        self.loginWindow = tk.Toplevel(self)
        self.loginWindow.title("Log In")
        self.loginWindow.geometry("430x100+665+400")
        self.loginWindow.resizable(width=False, height=False)

        fieldFrame = tk.Frame(self.loginWindow)

        id = tk.Entry(fieldFrame)
        password = tk.Entry(fieldFrame, show="*")
        loginButton = tk.Button(self.loginWindow, text="Login", height=3, command=lambda:self.logIn(id.get(), password.get()))
        registerButton = tk.Button(self.loginWindow, text="Register", height=3, command=lambda:self.register_execute(id.get(), password.get()))
        closeButton = tk.Button(self.loginWindow, text="Close", height=3, command=lambda:self.destroy())

        id.pack()
        password.pack()


        fieldFrame.pack(side="left", padx=5, pady=5)
        loginButton.pack(side="left")
        registerButton.pack(side="left")
        closeButton.pack(side="left")

        self.withdraw()
        self.mainloop()



    def logIn(self, id, password) -> None:

        self.accountList.fromJson()

        for account in self.accountList.getAccounts():
            if account.getUsername() == id and account.getPassword() == password:

                self.account = account
                self.account.logIn()
                self.accountList.toJson()
                print("Successfully logged in")

                self.loginWindow.destroy()
                self.deiconify()
                self.main_window()

            elif account.getUsername() == id and account.getPassword()!= password:
                print("Wrong password")

            else:
                print("Account not found")

        

    
    def register_execute(self, id: str, password: str) -> None:
        if not(self.already_exists(id, password)):
            self.account = Account(id, password)
            self.accountList.addAccount(self.account)
        
        else:
            print("Account already exists")

        self.accountList.toJson()


    def already_exists(self, id: str, password: str) -> bool:
        for account in self.accountList.getAccounts():
            return account.getUsername() == id and account.getPassword() == password


    # needs work on panedwindow
    def main_window(self) -> None:
        # frame = tk.PanedWindow(orient=tk.HORIZONTAL)
        # frame.pack(fill=tk.BOTH, expand=1)


        # time_space = tk.Listbox(frame)

        # frame.add(task_list)
        # frame.add(time_space)

        task_containter = tk.Frame(self)

        task_list = tk.Listbox(task_containter)
        task_adder = tk.Frame(task_containter)
        task_adder_entry = tk.Entry(task_adder)


        task_list.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        description = tk.Entry(task_adder_entry)
        prio = tk.Entry(task_adder_entry)
        adder_button = tk.Button(task_adder, text="Add Task", height=3, command=lambda:self.add_task(self.account.getTasks(), description.get(), int(prio.get())))

        description.pack(side=tk.TOP)
        prio.pack(side=tk.BOTTOM)
        task_adder_entry.pack(side=tk.LEFT)
        adder_button.pack(side=tk.RIGHT)

        task_adder.pack(side=tk.BOTTOM)

        if (self.account.getTasks().getTasks() != []):
            for task in self.account.getTasks().getTasks():
                task_button = tk.Menubutton(task_list, text=task.getDescription(), height=10, width=20, compound=tk.BOTTOM) # add command
                
                menu = tk.Menu(task_button)
                task_button["menu"] = menu

                menu.add_command(label="Mark as done", command=lambda:self.setFinished(task))
                menu.add_command(label="Edit Task", command=lambda:self.editTask(task, description.get(), int(prio.get())))

                task_button.pack()

        task_containter.pack(side=tk.LEFT, fill=tk.BOTH, expand=0)

        self.mainloop()

    
    def add_task(self, tasks: Tasks, description: str, prio: int) -> None:
        task = Task(description, prio)
        tasks.addTask(task)

        self.accountList.toJson()


    def setFinished(self, task: Task) -> None:
        task.setFinished()
        self.account.getTasks().removeTask(task)
        self.accountList.toJson()


    def editTask(self, task: Task, description: str, prio: int) -> None:
        task.setDescription(description)
        task.setPrio(prio)
        self.accountList.toJson()