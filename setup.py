from link import *
import urllib.request
import os

def install():
    print("Installing...")
    print("Your server is Papermc")
    a = os.path.exists("./Minecraft")
    if a == True:
        print("Foder exists")
    else:
        os.mkdir("Minecraft")
    print("1. 1.19(1.19.2)")
    print("2. 1.18(1.18.2)")
    print("3. 1.17(1.17.1)")
    print("4. 1.16(1.16.5)")
    print("5. 1.15(1.15.2)")
    print("6. 1.14(1.14.4)")
    print("7. 1.13(1.13.3)")
    print("8. 1.12(1.12.2)")
    a = input("Your Minecraft server version is:")
    if a == "1":
        print("Your minecraft version is : 1.19")
        urllib.request.urlretrieve(mc1192, "./Minecraft/server.jar")
        b=os.path.exists("./Minecraft/server.jar")
        print("downloading...")
        if b == True:
            print("done downloading")
        else:
            print("error downloading")
            print("Please try again!")
    if a == "2":
        print("Your minecraft version is : 1.18")
        print("downloading...")
        urllib.request.urlretrieve(mc1182, "./Minecraft/server.jar")
        b=os.path.exists("./Minecraft/server.jar")
        if b == True:
            print("done downloading")
        else:
            print("error downloading")
            print("Please try again!")
    if a == "3":
        print("Your minecraft version is : 1.17")
        print("downloading...")
        urllib.request.urlretrieve(mc1171, "./Minecraft/server.jar")
        b=os.path.exists("./Minecraft/server.jar")
        if b == True:
            print("done downloading")
        else:
            print("error downloading")
            print("Please try again!")
    if a == "4":
        print("Your minecraft version is : 1.16")
        print("downloading...")
        urllib.request.urlretrieve(mc1165, "./Minecraft/server.jar")
        b=os.path.exists("./Minecraft/server.jar")
        if b == True:
            print("done downloading")
        else:
            print("error downloading")
            print("Please try again!")
    if a == "5":
        print("Your minecraft version is : 1.15")
        print("downloading...")
        urllib.request.urlretrieve(mc1152, "./Minecraft/server.jar")
        b=os.path.exists("./Minecraft/server.jar")
        if b == True:
            print("done downloading")
        else:
            print("error downloading")
            print("Please try again!")
    if a == "6":
        print("Your minecraft version is : 1.14")
        print("downloading...")
        urllib.request.urlretrieve(mc1144, "./Minecraft/server.jar")
        b=os.path.exists("./Minecraft/server.jar")
        if b == True:
            print("done downloading")
        else:
            print("error downloading")
            print("Please try again!")
    if a == "7":
        print("Your minecraft version is : 1.13")
        print("downloading...")
        urllib.request.urlretrieve(mc1132, "./Minecraft/server.jar")
        b=os.path.exists("./Minecraft/server.jar")
        if b == True:
            print("done downloading")
        else:
            print("error downloading")
            print("Please try again!")
    if a == "8":
        print("Your minecraft version is : 1.12")
        print("downloading...")
        urllib.request.urlretrieve(mc1122, "./Minecraft/server.jar")
        b=os.path.exists("./Minecraft/server.jar")
        if b == True:
            print("done downloading")
        else:
            print("error downloading")
            print("Please try again!")
    c = input("Are you sure you want to accept this eula https://www.minecraft.net/zh-hans/eula (T/F)?")
    if c == "T" or c == "t":
        print("Accept")
        with open("./Minecraft/eula.txt", "w", encoding="utf-8") as f:
            f.write("eula=True")
        os.system("cd Minecraft && java -jar server.jar")
    elif c == "F" or c == "f":
        print("Error!Please accept eula!")
        print("This is not a bug!")
        print("Exiting!")
        exit()
    else:
        print("Error!Please enter t or f!")
        print("This is not a bug!")
        print("Exiting!")
        exit()
install()