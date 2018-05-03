import time


class Task:
    def __init__(self, name, time, deadline):
        self.name = name
        self.time = time  # in seconds
        self.deadline = deadline  # timestamp
        print("Log: Task object was created successfully")

    def toString(self):
        return ("Task name: " + self.name +
                "\nTask time: " + str(self.time) +
                "\nTask deadline: " + str(self.deadline))

tasks = []


def tasksToString(tasks):
    info = "Your tasks for today:"
    for task in tasks.dictionary:
        info += "\n----------------------\n"  # ASCII art :)
        info += task.toString()
        info += "\n----------------------\n"  # ASCII art :)
    return info


def getTask():
    name = input("What's the name?: ")
    time = input("How much time doues it take to do your task?: ")
    deadline = input("When is your deadline of task?: ")
    return Task(name, time, deadline)


def sortDict(taskDict):
    taskDict.dictionary = sorted(taskDict.dictionary, key=lambda task: task.deadline)


def interface():
    global tasks
    while True:
        cmd = input(">> ").split()
        if cmd[0] == "exit":
            break
        elif cmd[0] == "add":
            if len(cmd) > 1:
                if cmd[1] == "task":
                    tasks.append(getTask())
                    sortDict(tasks)
            else:
                print("Warning: Not enough params")
        elif cmd[0] == "status":
            print(tasksToString(tasks))
        else:
            print("Wrong command!")


def main():
    print("DEBUG MODE")
    interface()


if __name__ == '__main__':
    main()
