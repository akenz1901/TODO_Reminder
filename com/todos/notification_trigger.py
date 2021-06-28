from win10toast import ToastNotifier
import time

list_of_to_do = []

predicted_time = 1 * 10


def toDoInterFace():
    take = str(input("Enter A TODO: "))
    return take


def get_to_do():
    list_of_to_do.append(toDoInterFace())
    for i in list_of_to_do:
        return i


def time_calculator(minutes):
    return time.sleep(minutes)


def todo_notifier():
    message = get_to_do()
    name = "TODO"
    notification_toaster = ToastNotifier()
    time_calculator(60)
    notification_toaster.show_toast(name, message)


todo_notifier()
