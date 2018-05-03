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


class TaskDict:
    def __init__(self):
        self.dictionary = []

    def appendToDict(self, task):
        if type(task) is Task:
            self.dictionary.append(task)
        else:
            print(task)
            print('Warning: task in not Task Object!')

    def toString(self):
        info = "Your tasks for today:"
        for task in self.dictionary:
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
    taskDict = TaskDict()
    while True:
        cmd = input(">> ").split()
        if cmd[0] == "exit":
            break
        elif cmd[0] == "add":
            if len(cmd) > 1:
                if cmd[1] == "task":
                    taskDict.appendToDict(getTask())
                    sortDict(taskDict)
            else:
                print("Warning: Not enough params")
        elif cmd[0] == "status":
            print(taskDict.toString())
        else:
            print("Wrong command!")


def main():
    print("DEBUG MODE")
    interface()


if __name__ == '__main__':
    main()
