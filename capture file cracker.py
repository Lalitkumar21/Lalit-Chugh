import os

def banner():
    print("banner")

adapter_name="wlan0"

def stop_mon():
    e_mon_mode= "airmon_ng stop " +  adapter_name+"mon"
    os.system(e_mon_mode)

def menu1():
    print("[A] start\n[B] EXIT")

def adapter_config():
    s_mon_mode= "airmon_ng start "+ adapter_name
    os.system(s_mon_mode)

def menu2():
    print("\n[E] Scan\n[D] Back \n[B] Exit")

def scan_net():
    scan_network="airdump - ng " + adapter_name
    os.system(scan_network)

def menu3():
    pro_name= input("\n profect_name ~$")
    bssid= input("\n bssid ~$")
    channel = input("\nchannel ~$")
    gst_inside= "airodump -ng --bssid "+bssid+" -c "+channel+" --write "+pro_name
    os.system(gst_inside)

def menu4():
    print("\n[E] Start Cracking\n[F]Stop Monitor Mode \n[B] Exit")
    
def crack():
    cap_location = input("\nCap File Location ~$")
    wordlist=input("\nWordlist Location ~$")
    crack = "aircrack-ng "+cap_location+" -w "+wordlist
    os.system(crack)

menu1()
banner()

while True:
    shell= input("\n~$")

    if shell == "A" or shell== "a":
        adapter_config()
        menu2()

    if shell == "B" or shell=="b":
        break

    if shell =="C" or shell=="c":
        scan_net()
        menu3()
        menu4()

    if shell =="D" or shell=="d":
        menu1()

    if shell =="E" or shell=="e":
        crack()

    if shell =="F" or shell=="f":
        stop_mon()

    else:
        print("Not a command")


    
