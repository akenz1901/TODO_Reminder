from win10toast import ToastNotifier
import time

list_of_to_do = {""}


def store_name_and_message(name: str, take: str):
    list_of_to_do.update(name, take)


def getListOfToDo():
    return list_of_to_do


# def get_to_do():
#     for i in list_of_to_do:
#         return i


def time_calculator(seconds):
    return time.sleep(seconds)


# def todo_notifier():
#     notification_toaster = ToastNotifier()
#     message = get_to_do()
#     name = "TODO"
#     time_calculator(1800)
#     notification_toaster.show_toast(name, message)
# todo_notifier()

def store_todo():
    print("Is there more TODO to add ?\n.\n.\n.\nEnter Yes if you have more todo and No if there is no more TODO")
    decision = str(input("Or enter Y/N: "))
    return decision


def store_reminder_time():
    minutes = int(input("How many minutes time do you intend to get notification: "))
    tem_time = minutes * 60
    return tem_time


def new_to_app():
    notification_toaster = ToastNotifier()
    thread_for_each_todo = []
    print("Hey Welcome")
    name = str(input("Enter to name: "))
    take = str(input("Enter A TODO: "))
    while True:
        store_name_and_message(name, take)
        # thread_for_each_todo.append(store_reminder_time())
        store_todo()
        if store_todo().capitalize().startswith("Y"):
            print("You can store as much as you desire")
            continue
        elif store_todo().capitalize().startswith("N"):
            break
    print("Saving........")
    time_calculator(seconds=10)
    print("Saved!")
    for t in thread_for_each_todo:
        time_calculator(seconds=t)
        i = 0
        ii = 1
        for n, m in getListOfToDo():
            notification_toaster.show_toast(n, m)
            i += 1
            if i is ii:
                ii += 1
                break


new_to_app()
