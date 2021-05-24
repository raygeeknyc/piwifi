Piwifi - easy setup of Raspberry Pi Wifi networks
* Clone this repos into~pi/Documents/workspace

* Copy the contents of the etc_* file into your /etc/rc.local file
   * Do not replace the rc.local file, use an editor to embed the contents into your existing file
* Customize your list of networks in the file networks_list.txt
* Reboot


Make future changes in your network list in the file /boot/network_files/networks_list.txt
* Since the /boot partition is mounted by Windows, macOS and Linux, you can insert your Raspberry Pi's SD card into a laptop or desktop computer and edit the network list
