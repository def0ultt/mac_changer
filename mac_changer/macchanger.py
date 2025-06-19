import subprocess 
import argparse 
import re 
import random


mac_prifx_path = "default_mac/oui"
mac_Suffix_path = "default_mac/suffix"

def random_mac(mac_prifx_path, mac_Suffix_path):
    with open(mac_prifx_path, "r") as file:
        prefixes = [line.strip() for line in file if line.strip()]
        random_prefix = random.choice(prefixes)

    with open(mac_Suffix_path, "r") as file:
        rests = [line.strip() for line in file if line.strip()]
        random_rest = random.choice(rests)

    new_mac = f"{random_prefix}:{random_rest}"
    return new_mac


def change_mac(interface_name,new_mac):
    subprocess.call(f"ifconfig {interface_name} down", shell=True)
    subprocess.call(f"ifconfig {interface_name} hw ether {new_mac}", shell=True)
    subprocess.call(f"ifconfig {interface_name} up", shell=True)
    print(f"[+] Initiating MAC address change to {new_mac}")


def chek_mac(interface_name, new_mac):
    ifconfig = subprocess.check_output(f"ifconfig {interface_name}", shell=True).decode("UTF-8")
    mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig)
    mac_address = mac[0]
    if mac_address.lower() == new_mac.lower():
        print(f"[✓] MAC address successfully updated to: {mac_address}")
    else:
        print("[-] MAC address verification failed. Possible error during update.")


def main():
    parser = argparse.ArgumentParser(description="Change MAC address tool")
    parser.add_argument('-i', '--interface', type=str, required=True, help='Interface name (e.g. eth0)')
    parser.add_argument('-m', '--mac', type=str, required=False, help='new MAC address')

    argument = parser.parse_args()

    interface_name = argument.interface
    new_mac = argument.mac


    if not new_mac:
        new_mac = random_mac(mac_prifx_path, mac_Suffix_path)
       

    change_mac(interface_name, new_mac)
    chek_mac(interface_name, new_mac)

if __name__ == "__main__":

    main()


        