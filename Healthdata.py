def getdate():
    import datetime
    return datetime.datetime.now()
with open("Clients_name") as f:
    client=f.read().splitlines()
lock_list = {1: "Exercise", 2: "Diet"}

def add_client():
    with open("Clients_name", "a") as f:
        print("Enter Name: ")
        new_client=input()
        client=f.write("\n"+new_client)



def select_client():
    for index,value in enumerate(client):
        print("Select",index,"for",value)
    global client_name
    client_name=int(input())
    print("You selected:",client[client_name])

def lock():
    for key, value in lock_list.items():
        print("Press", key, "to lock", value, "\n", end="")

    lock_name = int(input())

    print("Selected Job : ", lock_list[lock_name])

    f = open(client[client_name] + "_" + lock_list[lock_name] + ".txt", "a")

    k = 'y'

    while (k != "n"):
        print("Enter", lock_list[lock_name], "\n", end="")

        mytext = input()

        f.write("[ " + str(getdate()) + " ] : " + mytext + "\n")

        k = input("ADD MORE ? y/n:")

        continue

    f.close()

def retrieve():
    for key, value in lock_list.items():
        print("Press", key, "to retrieve", value, "\n", end="")

    lock_name = int(input())

    print(client[client_name], "-", lock_list[lock_name], "Report :", "\n", end="")

    f = open(client[client_name] + "_" + lock_list[lock_name] + ".txt", "rt")

    contents = f.readlines()

    for line in contents:
        print(line, end="")

    f.close()


print("Total clients are",client,)
add=input("Do you want to add another client (y): ")
if add=="y":
    add_client()
    print("New client has been added.")


else:
    select_client()
    lr=int(input("Press 1 for Lock \nPress 2 for Retrieve "))
    if lr==1:
        lock()
    elif lr==2:
        retrieve()
    else:
        print("Invalid Value!!!")


















