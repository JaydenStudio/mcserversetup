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
    print("Your minecraft version is : 1.19")
    print("downloading...")
    a=os.path.exists("./Minecraft/server.jar")
    if a == False:
        urllib.request.urlretrieve(mc1192, "./Minecraft/server.jar")
    else:
        os.system("cd Minecraft && java -jar server.jar")
        exit() 
    a=os.path.exists("./Minecraft/server.jar")
    if a == True:
        print("done downloading")
        print("save the file to /Minecraft/server.jar")
        os.system("cd Minecraft && java -jar server.jar")
        with open("./Minecraft/eula.txt", "w") as f:
            f.write("eula=True")
        os.system("cd Minecraft && java -jar server.jar")
    else:
        print("Could not download server.jar")
        print("restarting setuptools")
        install()
install()