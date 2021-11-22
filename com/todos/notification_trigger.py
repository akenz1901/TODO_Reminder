import os
from win10toast import ToastNotifier
import time
list_of_to_do = {}
time_accumulator = []


def store_name_and_message(name: str, take: str):
    list_of_to_do[name] = take


def getListOfToDo():
    return list_of_to_do


# def get_to_do():
#     for i in list_of_to_do:
#         return i

def store_time(seconds):
    time_accumulator.append(seconds)


def get_times():
    return time_accumulator


def delay_alert_time(seconds):
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


def store_attributes():
    name = str(input("Enter a TODO name:"))
    todo = str(input("Enter a TODO:"))
    store_name_and_message(name, todo)


def time_management():
    seconds = int(input("Enter how many seconds you want to get an alert: "))
    store_time(seconds)


def new_to_app():
    notification_toaster = ToastNotifier()
    store_attributes()
    time_management()
    while True:
        print("Is there more TODO to add ?\n.\n.\n.\nEnter Yes if you have more todo and No if there is no more TODO")
        decision = str(input("Or enter Y/N: "))
        if decision.capitalize().startswith("Y"):
            store_attributes()
            time_management()
        else:
            break
    for name in getListOfToDo():
        for sc in get_times():
            delay_alert_time(sc)
            notification_toaster.show_toast(name, getListOfToDo().get(name))


new_to_app()
