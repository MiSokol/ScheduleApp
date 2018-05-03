import time
import ExcelInterface as ex

class Task:
    def __init__(self, name, time, deadline):
        self.name = name
        self.time = time  # in seconds
        self.deadline = deadline  # timestamp
        self.completed = False
        print("Log: Task object was created successfully")

    def toString(self):
        return ("Task name: " + self.name +
                "\nTask time: " + str(self.time) +
                "\nTask deadline: " + str(self.deadline) +
                "\nTask completed: " + str(self.completed))

tasks = []


def tasksToString():
    global tasks
    info = "Your tasks for today:"
    for task in tasks:
        info += "\n----------------------\n"  # ASCII art :)
        info += task.toString()
        info += "\n----------------------\n"  # ASCII art :)
    return info


def getTask():
    name = input("What's the name?: ")
    time = int(input("How much time does it take to do your task?: "))
    deadline = int(input("When is your deadline of task?: "))
    return Task(name, time, deadline)


def sortDict():
    global tasks
    tasks = sorted(tasks, key=lambda task: task.deadline)


def interface():
    global tasks
    ex.initial()
    while True:
        cmd = input(">> ").split()
        if cmd[0] == "exit":
            break
        elif cmd[0] == "add":
            if len(cmd) > 1:
                if cmd[1] == "task":
                    tasks.append(getTask())
                    sortDict()
                    ex.initial()  # backup

                    counter = 0
                    for i in tasks:
                        ex.addRow(i)
                        if i.completed:
                            ex.makeRowCompleted(counter)
                            counter += 1
            else:
                print("Warning: Not enough params")
        elif cmd[0] == "status":
            print(tasksToString())
        elif cmd[0] == "import":
            tasks = ex.readFromList()
            sortDict()
            ex.initial()  # backup

            counter = 0
            for i in tasks:
                ex.addRow(i)
                if i.completed:
                    ex.makeRowCompleted(counter)
                    counter+=1

        elif cmd[0] == "set":
            if len(cmd) > 3:
                if cmd[1] == "status":
                    taskID = cmd[2]
                    status = cmd[3]
                    if status == "completed":
                        try:
                            tsk = tasks[int(taskID)]
                            tsk.completed = True
                            ex.makeRowCompleted(int(taskID))
                            print(taskID, "set to completed")
                        except Exception as exception:
                            print(exception)
                            print("ERROR: No such TaskID!!!")
            else:
                print("Warning: Not enough params")
        else:
            print("Warning: Wrong command!")


def main():
    print("DEBUG MODE")
    interface()


if __name__ == '__main__':
    main()
