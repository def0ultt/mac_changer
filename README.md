🔧 MAC Changer
A fast and user-friendly Python script to change or spoof your MAC address on the fly.

This lightweight tool lets you easily change your MAC address — useful for privacy, penetration testing, or bypassing MAC-based filters.
If no custom MAC is provided, it generates a random valid MAC address with a real vendor prefix (OUI).

⚙️ Usage
-------------------------------------------------------------------------------------
python3 mac_changer.py -i <interface>  [-m <new_mac>]
----------------------------------------------------------------------------------
-i or --interface: (required) The network interface to change the MAC address on.

-m or --mac: (optional) A custom MAC address to set.

If this option is not used, the script generates a random MAC address, with the first 3 bytes matching a real hardware vendor.

💡 Examples
Change the MAC address of eth0 to a specific value:
--------------------------------------------------------
  python3 mac_changer.py -i eth0 -m 00:11:22:33:44:55
-----------------------------------------------------------
💡 Examples 2

Change the MAC address of wlan0 to a random valid one:
-------------------------------------------------------
  python3 mac_changer.py -i wlan0
---------------------------------------------------
