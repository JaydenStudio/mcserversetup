import urllib.request
import os
#https://space.bilibili.com/1956516963
#This is the download link
pmc1192 = "https://api.papermc.io/v2/projects/paper/versions/1.19.2/builds/258/downloads/paper-1.19.2-258.jar"
pmc1182 = "https://api.papermc.io/v2/projects/paper/versions/1.18.2/builds/388/downloads/paper-1.18.2-388.jar"
pmc1171 = "https://api.papermc.io/v2/projects/paper/versions/1.17.1/builds/411/downloads/paper-1.17.1-411.jar"
pmc1165 = "https://api.papermc.io/v2/projects/paper/versions/1.16.5/builds/794/downloads/paper-1.16.5-794.jar"
pmc1152 =  "https://api.papermc.io/v2/projects/paper/versions/1.15.2/builds/393/downloads/paper-1.15.2-393.jar"
pmc1144 = "https://api.papermc.io/v2/projects/paper/versions/1.14.4/builds/245/downloads/paper-1.14.4-245.jar"
pmc1132 = "https://api.papermc.io/v2/projects/paper/versions/1.13.2/builds/657/downloads/paper-1.13.2-657.jar"
pmc1122 = "https://api.papermc.io/v2/projects/paper/versions/1.12.2/builds/1620/downloads/paper-1.12.2-1620.jar"
vmc1193 = "https://piston-data.mojang.com/v1/objects/c9df48efed58511cdd0213c56b9013a7b5c9ac1f/server.jar"
vmc1182 = "https://launcher.mojang.com/v1/objects/c8f83c5655308435b3dcf03c06d9fe8740a77469/server.jar"
vmc1171 = "https://launcher.mojang.com/v1/objects/a16d67e5807f57fc4e550299cf20226194497dc2/server.jar"
vmc1165 = "https://launcher.mojang.com/v1/objects/1b557e7b033b583cd9f66746b7a9ab1ec1673ced/server.jar"
vmc1152 = "https://launcher.mojang.com/v1/objects/bb2b6b1aefcd70dfd1892149ac3a215f6c636b07/server.jar"
vmc1144 = "https://launcher.mojang.com/v1/objects/3dc3d84a581f14691199cf6831b71ed1296a9fdf/server.jar" #1145141919810
vmc1132 = "https://launcher.mojang.com/v1/objects/3737db93722a9e39eeada7c27e7aca28b144ffa7/server.jar"
vmc1122 = "https://launcher.mojang.com/v1/objects/3737db93722a9e39eeada7c27e7aca28b144ffa7/server.jar"

#code
def fail():
    #????????
    print("error downloading")#print error donloading
    print("Please try again!")#print Please try again
    exit()#exit python
def install_vanilla():#Function install_vanilla
    print("Your server is vanilla")#print Your server is vanilla
    a = os.path.exists("./Minecraft")#True or False
    if a == True:#if a is True
        print("Foder exists")#print Foder exists
    else:#if a is False
        os.mkdir("Minecraft")#make directory Minecraft
    #print all versions
    print("1. 1.19(1.19.3)")
    print("2. 1.18(1.18.2)")
    print("3. 1.17(1.17.1)")
    print("4. 1.16(1.16.5)")
    print("5. 1.15(1.15.2)")
    print("6. 1.14(1.14.4)")
    print("7. 1.13(1.13.3)")
    print("8. 1.12(1.12.2)")
    #input version
    a = input("Your Minecraft server version is:")
    if a == "1":#if a == 1 / if user selected 1.19
        print("Your minecraft version is : 1.19")#print your minecraft server version is 1.19
        urllib.request.urlretrieve(vmc1193, "./Minecraft/server.jar")#download minecraft server
        print("downloading...")#print downloading...
        b=os.path.exists("./Minecraft/server.jar")#True or False
        if b == True:#if b is True
            print("done downloading")#print done downloading
        else:
            fail()
    if a == "2":#if a = 2
        print("Your minecraft version is : 1.18")#print your minecraft version is 1.18
        print("downloading...")#print downloading...
        urllib.request.urlretrieve(vmc1182, "./Minecraft/server.jar")#download minecraft server
        b=os.path.exists("./Minecraft/server.jar")#True or False
        if b == True:# if b = True
            print("done downloading")#print done downloading
        else:#if b = False
            fail()
    if a == "3":#if a = 3
        print("Your minecraft version is : 1.17")#print your minecraft version is 1.17
        print("downloading...")#print downloading...
        urllib.request.urlretrieve(vmc1171, "./Minecraft/server.jar")#download server
        b=os.path.exists("./Minecraft/server.jar")#True or false
        if b == True:#if b is True
            print("done downloading")#print done downloading
        else:#if b is False
            fail()
    if a == "4":#if a = 4
        print("Your minecraft version is : 1.16")#print your minecraft version is 1.16
        print("downloading...")#print downloading...
        urllib.request.urlretrieve(vmc1165, "./Minecraft/server.jar")#download server
        b=os.path.exists("./Minecraft/server.jar")#True or False
        if b == True:#if b = True
            print("done downloading")#print done downloading
        else:#if b is False
            fail()
    if a == "5":#if a = 5
        print("Your minecraft version is : 1.15")#print your minecraft version is 1.15
        print("downloading...")#print downloading...
        urllib.request.urlretrieve(vmc1152, "./Minecraft/server.jar")#download server
        b=os.path.exists("./Minecraft/server.jar")#True or False
        if b == True:#if b = True
            print("done downloading")#print done downloading
        else:#if b = False
            fail()
    if a == "6":#if a = 6
        print("Your minecraft version is : 1.14")#print your minecraft version is 1.14
        print("downloading...")#print downloading...
        urllib.request.urlretrieve(vmc1144, "./Minecraft/server.jar")#download server.jar
        b=os.path.exists("./Minecraft/server.jar")#True or False
        if b == True:#if b = True
            print("done downloading")#print done downloading
        else:
            fail()
    if a == "7":#if a = 7
        print("Your minecraft version is : 1.13")#print your minecraft version is 1.13
        print("downloading...")#print downloading...
        urllib.request.urlretrieve(vmc1132, "./Minecraft/server.jar")#download server
        b=os.path.exists("./Minecraft/server.jar")#True or False
        if b == True:#if b = True
            print("done downloading")#print done downloading
        else:#if b = False
            fail()
    if a == "8":#if a = 8
        print("Your minecraft version is : 1.12")#print your minecraft version is 1.12
        print("downloading...")#print downloading...
        urllib.request.urlretrieve(vmc1122, "./Minecraft/server.jar")#print downloading...
        b=os.path.exists("./Minecraft/server.jar")#True or False
        if b == True:#if b = True
            print("done downloading")#print done downloading...
        else:
            fail()
    c = input("Are you sure you want to accept this eula https://www.minecraft.net/zh-hans/eula (T/F)?")#accept eula
    if c == "T" or c == "t":#if c = t
        print("Accept")#print Accept
        with open("./Minecraft/eula.txt", "w", encoding="utf-8") as f:#open eula file
            f.write("eula=True")#accept the eula
        os.system("cd Minecraft && java -jar server.jar")#start server
        exit()#exit python
    elif c == "F" or c == "f":#if user is not accepted eula
        print("Error!Please accept eula!")#print ErrorMessage
        print("This is not a bug!")#print this is not a bug
        print("Exiting!")#print exiting
        exit()#exit python
    else:
        print("Error!Please enter t or f!")#if c is not t or f 
        print("This is not a bug!")#print This is not a bug
        print("Exiting!")#print exiting
        exit()#exit python
def install_papermc():
    #What?
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
        urllib.request.urlretrieve(pmc1192, "./Minecraft/server.jar")
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
        urllib.request.urlretrieve(pmc1182, "./Minecraft/server.jar")
        b=os.path.exists("./Minecraft/server.jar")
        if b == True:
            print("done downloading")
        else:
            print("error downloading")
            print("Please try again!")
    if a == "3":
        print("Your minecraft version is : 1.17")
        print("downloading...")
        urllib.request.urlretrieve(pmc1171, "./Minecraft/server.jar")
        b=os.path.exists("./Minecraft/server.jar")
        if b == True:
            print("done downloading")
        else:
            print("error downloading")
            print("Please try again!")
    if a == "4":
        print("Your minecraft version is : 1.16")
        print("downloading...")
        urllib.request.urlretrieve(pmc1165, "./Minecraft/server.jar")
        b=os.path.exists("./Minecraft/server.jar")
        if b == True:
            print("done downloading")
        else:
            print("error downloading")
            print("Please try again!")
    if a == "5":
        print("Your minecraft version is : 1.15")
        print("downloading...")
        urllib.request.urlretrieve(pmc1152, "./Minecraft/server.jar")
        b=os.path.exists("./Minecraft/server.jar")
        if b == True:
            print("done downloading")
        else:
            print("error downloading")
            print("Please try again!")
    if a == "6":
        print("Your minecraft version is : 1.14")
        print("downloading...")
        urllib.request.urlretrieve(pmc1144, "./Minecraft/server.jar")
        b=os.path.exists("./Minecraft/server.jar")
        if b == True:
            print("done downloading")
        else:
            print("error downloading")
            print("Please try again!")
    if a == "7":
        print("Your minecraft version is : 1.13")
        print("downloading...")
        urllib.request.urlretrieve(pmc1132, "./Minecraft/server.jar")
        b=os.path.exists("./Minecraft/server.jar")
        if b == True:
            print("done downloading")
        else:
            print("error downloading")
            print("Please try again!")
    if a == "8":
        print("Your minecraft version is : 1.12")
        print("downloading...")
        urllib.request.urlretrieve(pmc1122, "./Minecraft/server.jar")
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
        exit()#exit python
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
def install():
    print("Installing...")#print installing...
    #print all versions
    print("1.Papermc")
    print("2.vanilla")
    x = input("Your server is:")#input version
    if x == "1":#if x = 1
        install_papermc()#install papermc
    if x == "2":#if x = 2
        install_vanilla()#install vanilla
    else:#if x not is 1 or 2
        print("Please select 1 or 2!")#print please select 1 or 2
        y = input("Are you sure you want to install Papermc(Y/N)?")#input yes or no
        if y == "Y" or y == "y":#if y = y
            install_papermc()#install papermc
        elif y == "n" or y == "N":#if y = n
            print("OK")#print OK
            exit()#exit python
        else:#if if y is not y or f
            print("Please select y or n!")#print Please select y or n
            print("This is not a bug!")#print This is not a bug
            exit()#exit python
install()#go!