import time
import ExcelInterface as ex

class Task:
    def __init__(self, name, time, deadline):
        self.name = name
        self.time = timelook_from(time)  # in seconds
        self.deadline = timelook_from(deadline)  # timestamp
        print("Log: Task object was created successfully")

    def toString(self):
        return ("Task name: " + self.name +
                "\nDo task at: " + str(timelook_to(times[self.name][0])) +
                "\nTask time: " + str(timelook_to(self.time)) +
                "\nTask deadline: " + str(timelook_to(self.deadline)))
    def valu(self):
        return [self.name,int(self.time),int(self.deadline)]

tasks = []
times = dict()


def timelook_from(s):
    S = list(s.split(':'))
    if len(S) > 1:
        return int(S[0])*60 + int(S[1])
    else:
        return int(S[0])
    
def timelook_to(s):
    hours = str(s//60)
    seconds = str(s%60)
    if s//60 < 10:
        hours = '0'+str(s//60)
    if s%60 < 10:
        seconds = '0'+str(s%60)
    return hours+':'+seconds


def tasksToString():
    global tasks
    global times
    info = "Your tasks for today:"
    for task in tasks:
        info += "\n----------------------\n"  # ASCII art :)
        info += task.toString()
        info += "\n----------------------\n"  # ASCII art :)
    return info


def getTask():
    name = input("What's the name?: ")
    time = input("How much time doues it take to do your task?: ")
    deadline = input("When is your deadline of task?: ")
    return Task(name, time, deadline)


def sortDict():
    global tasks
    tasks = sorted(tasks, key=lambda task: task.deadline)


def interface():
    global tasks
    global times
    while True:
        cmd = input(">> ").split()
        if cmd[0] == "exit":
            break
        elif cmd[0] == "add":
            if len(cmd) > 1:
                if cmd[1] == "task":
                    tasks.append(getTask())
                    sortDict()
                    ex.initial() #backup
                    lasttime = 9*60
                    for i in tasks:
                        if lasttime + i.valu()[1] < 22*60:
                            times[i.valu()[0]] = [lasttime]
                            lasttime += i.valu()[1]
                        else:
                            if 22*60 - lasttime + i.valu()[1] > 60:
                                times[i.valu()[0]] = [22*60,9*60+22*60 - lasttime + i.valu()[1] - 60]
                                lasttime = 9*60
                                
                            else:
                                times[i.valu()[0]] = [9*60]
                                lasttime = 9*60
                        ex.addRow(i)
            else:
                print("Warning: Not enough params")
        elif cmd[0] == "status":
            print(tasksToString())
        else:
            print("Wrong command!")


def main():
    print("DEBUG MODE")
    interface()


if __name__ == '__main__':
    main()
