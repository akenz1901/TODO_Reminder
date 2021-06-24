from win10toast import ToastNotifier

time = 1
list_of_to_do = []


def get_to_do():
    message = str(input("Enter A TODO: "))
    list_of_to_do.append(message)
    for i in list_of_to_do:
        return i


def notifier():
    name = "TODO"
    message = get_to_do()
    notification_toaster = ToastNotifier()

    notification_toaster.show_toast(name, message)


notifier()
