from win10toast import ToastNotifier
import time

list_of_to_do = []

predicted_time = 1 * 10


def toDoInterFace():
    take = str(input("Enter A TODO: "))
    list_of_to_do.append(take)
    return take


def get_to_do():
    for i in list_of_to_do:
        return i


def time_calculator(minutes):
    return time.sleep(minutes)


def todo_notifier():
    notification_toaster = ToastNotifier()
    message = get_to_do()
    name = "TODO"
    time_calculator(1800)
    notification_toaster.show_toast(name, message)


def store_todo():
    toDoInterFace()
    store_reminder_time()
    print("Is there more TODO to add ?\n.\n.\n.\nEnter Yes if you have more todo and No if there is no more TODO")
    decision = str(input("Or enter Y/N"))
    return decision


def store_reminder_time():
    thread_for_each_todo = []
    minutes = int(input("Enter Notification Time: "))
    thread_for_each_todo.append(minutes)


def new_to_app():
    notification_toaster = ToastNotifier()
    print("Hey Welcome")
    while True:
        store_todo()
        if store_todo().capitalize().startswith("Y"):
            print("You can store as much as you desire")
            pass
        elif store_todo().capitalize().startswith("N"):
            return False


todo_notifier()
