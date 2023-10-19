import json
import socket  # importing the module
import time
import os
with open("coincount.txt") as d:
    user_data = json.loads(d.read()) # this loads in the dictonary from the txt
####Function
def save():
    with open("coincount.txt", "w") as d:
        d.write(json.dumps(user_data)) # Writes the dictonary to the first line
    print("Data saved!")
def coin_index(cointype):
    match cointype:
        case "£2":
            return 0
        case "£1":
            return 1
        case "50p":
            return 2
        case "20p":
            return 3
        case "10p":
            return 4
        case "5p":
            return 5
        case "2p":
            return 6
        case "1p":
            return 7
        case _:
            return -1
####applications
def count():
    coin_data = [[200,100,50,20,10,5,2,1],[2000,2000,1000,1000,500,500,100,100],[12,8.75,8,5,6.5,2.35,7.12,3.56],[]]
    correct_bag = 0
    # set data set index 0 is the coin values, index 1 is bag values and index 2 is the weights of singular coins
    volunteer = input("Enter the volunteer's name >:")
    cointype = input("Enter the type of coins being counted eg(£1,10p) >:")
    coin_i = coin_index(cointype)
    #gets the index for coin data to make it easier for the 2d array

    if coin_i == -1:
        #minnus -1 is returned when the coin type is not in the match statement and the user if notified of the correct format.
        print("Coin type was incorrect types are (£2, £1, 50p, 20p, 10p, 5p, 2p, 1p)")
        return # returns to main program

    weight = float(input("Enter the current bag weight :>"))
    # the user inputs data
    coin_i = coin_index(cointype)
    #gets the index for coin data to make it easier for the 2d array

    good_weight = (coin_data[1][coin_i]/coin_data[0][coin_i])*coin_data[2][coin_i]
    # it calculates the correct weight useing the gotten coin index and coin data using the calculation (bag value/coin value)*Coin weight

    if good_weight == weight:
        # Checks the calculated weight with the inputed weight
        correct_bag = 1
        print("Coins counted correctly")
    else:
        print(f"Coins where not counted correctly you need to change the bag by {int((good_weight-weight)/coin_data[2][coin_i])} coins.")
        #tells the user how many to remove.


    # stores the total counted checks is the volenter is stored allready
    if volunteer in user_data:
        user_data[volunteer]["counted bags"] += 1
        user_data[volunteer]["Correct bags"] += correct_bag
        # if zero the code won't atempt to divide by zero
        if user_data[volunteer]["Correct bags"] > 1:
            user_data[volunteer]["Percent"] = (user_data[volunteer]["Correct bags"] / user_data[volunteer]["counted bags"]) * 100
        else:
            user_data[volunteer]["Percent"] = 0
        user_data[volunteer]["Total"] += coin_data[1][coin_i]

    else:
        user_data[volunteer] = {}
        user_data[volunteer]["counted bags"] = 1
        user_data[volunteer]["Correct bags"] = correct_bag

        if correct_bag == 1:
                user_data[volunteer]["Percent"] = (user_data[volunteer]["Correct bags"] / user_data[volunteer]["counted bags"]) * 100
        else:
                user_data[volunteer]["Percent"] = 0

        user_data[volunteer]["Total"] = coin_data[1][coin_i]

    save() #data is saved after every time the userdata is updated beacuse some users will press x without proply quitting

def stats():
    user_i = input("To view seprate stats input a name name or leave blank for all :>")
    if user_i == "":
        s_names = sorted(user_data, key=lambda x: (user_data[x]["Percent"]),reverse=True)
        #Storts the names of by there nested percent value then sores the names in a list.
        for name in s_names:
            print(f"""{name}'s Stats are
            Counted bags : {user_data[name]["counted bags"]}
            Correct bags : {user_data[name]["Correct bags"]}
            How much they counted : £{(user_data[name]["Total"]) / 100}
            Accuracy : {user_data[name]["Percent"]}%
            
            """)
            #prints the stats name by name as ordered by the list.
        sum = 0
        for name in user_data:
            sum += user_data[name]["Total"]
        #gets the total from each volenter
        print(f"The total counted is £{sum / 100}")
    else:
        if user_i in user_data:
            print(f"""{user_i}'s Stats are
Counted bags : {user_data[user_i]["counted bags"]}
Correct bags : {user_data[user_i]["Correct bags"]}
How much they counted : £{(user_data[user_i]["Total"])/100}
Accuracy : {user_data[user_i]["Percent"]}%
""")
            #prints the indervisuals data.
### cool things
def upload():
    ip = input("custom server ip leave blank for default :")
    if ip == "":
        ip = socket.gethostbyname("Enter Domain Name")
    elif ip == "@":
        ip = "127.0.0.1"
    port = 89
    cSct = socket.socket()  # creating the socket
    print("Please wait while connecting you there may not be a slot ready.")
    cSct.connect((ip, port))# connecting to the server
    print(cSct.recv(1024).decode())
    cSct.send(bytes("PING", "utf-8"))
    cSct.send(bytes("1", "utf-8"))##chacnge point
    cSct.send(bytes(input("Enter the name of the file and note it some where!>:"), "utf-8")) # 1 is for sending
    print(cSct.recv(1024).decode())
    cSct.send(bytes(json.dumps(user_data), "utf-8"))

def download():
    ip = input("custom server ip leave blank for default :")
    if ip == "":
        ip = socket.gethostbyname("Enter Domain Name")
    elif ip == "@":
        ip = "127.0.0.1"
    port = 89
    cSct = socket.socket()  # creating the socket
    print("Please wait while connecting you there may not be a slot ready.")
    cSct.connect((ip, port))# connecting to the server
    print(cSct.recv(1024).decode())
    cSct.send(bytes("PING", "utf-8"))
    cSct.send(bytes("0", "utf-8"))#change point
    cSct.send(bytes(input("Enter the name of the file:"), "utf-8")) # 0 is for downloading
    print(cSct.recv(1024).decode())
    return json.loads(cSct.recv(1024).decode())




def format_dat():
    comfirm = input("Are you sure yuo want to erase all data stored!  (Y/N) >:") #confirmation just incase a user wants to keep data
    if comfirm == "Y":
        user_data = {}
        print("User_data has been formated")
        with open("coincount.txt", "w") as d:
            d.write(json.dumps({})) #writes a empty dictinary to the txt
        print("coincount.txt has been formated")
    else:
        print("Format aborted!")
    #this feature was added for testing and made life alot essier
while True:
    print("CoinCount v1.4!!P By Peter Cakebread 2023")
    user = input("Select a option count, stats, format or exit:>")
    match user:
        case "count"|"c":
            count()
        case "format":
            format_dat()
            user_data = {}
        case "exit"|"e":
            save()
            break
        case "stats"|"s":
            stats()
        case "upload"|"u":
            upload()
        case "download"|"d":
            user_data = download()
            save()
        case _:
            print("Option  is univalible")
#the main section which calls the function as requested.
