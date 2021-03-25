# Turn the Raspberry PI into A VPN Server with OpenVPN

## What is a VPN?
A VPN stands for Virtual Private Network which means it gives you privacy online. Initially, VPNs were used by big organizations and governments because of obvious security reasons, but nowadays VPNs are used by everyone because it ensures privacy and data security.

1- Your locations stay private

2- Your data is encrypted

3- You can surf the web anonymously

## what is the benefit of using VPN ?
By enabling a VPN, you are adding an extra layer of security to your network

#### -  What will we use the VPN for ?
We will set up a VPN server on the home network using a Raspberry Pi. This way we can securely connect to my local network while we are not home. Also, we just don't want to leave an SSH port open for just anybody to hack in. 
When you send your data online, a VPN creates a tunnel between you and your called server, it is done by utilizing a second server, when you request a page on the internet without the VPN, it goes directly to your requested server, but with VPN enabled, your request gets encrypted and goes to the server of your VPN provider, and then it goes to your requested server.

## Project Prerequisites:
- Raspberry Pi Zero.

## Setting up Pi-hole on a Raspberry Pi. 
### First update and upgrade your pi by running these commands:
```
sudo apt-get update
sudo apt-get upgrade
```
## Installing OpenVPN with PiVPN in Raspberry Pi Zero
By following the steps below and you will have a VPN server in no time.

### Installation
```
curl -L https://install.pivpn.io | bash
```
### Test(unstable)Branch
```
curl -L https://install.pivpn.io | TESTING- bash
```

Next, SSH into your Raspberry PI and paste in your code and hit enter, this will download & set up all the necessary setup to run OpenVPN. After that, you will be greeted with the below screen saying it will convert your raspberry pi into OpenVPN

     ┌───────────────────┤ PiVPN Automated Installer ├────────────────────┐
     │                                                                    │ 
     │ This installer will transform your Raspberry Pi into an OpenVPN or │ 
     │ WireGuard server!                                                  │ 
     │                                                                    │ 
     │                                                                    │ 
     │                                                                    │ 
     │                                                                    │ 
     │                                                                    │ 
     │                               <Ok>                                 │ 
     │                                                                    │ 
     └────────────────────────────────────────────────────────────────────┘

### Asking you to set up a static IP address for your Raspberry Pi, we do not need to do it.


     ┌────────────────────────┤ DHCP Reservation ├────────────────────────┐
     │                                                                    │ 
     │ Are you Using DHCP Reservation on your Router/DHCP Server?         │ 
     │ These are your current Network Settings:                           │ 
     │                                                                    │ 
     │         IP address:    10.0.0.12/24                                │ 
     │         Gateway:       10.0.0.1                                    │ 
     │                                                                    │ 
     │ Yes: Keep using DHCP reservation                                   │ 
     │ No: Setup static IP address                                        │ 
     │ Don't know what DHCP Reservation is? Answer No.                    │ 
     │                                                                    |
     │                                                                    │ 
     │                  <Yes>                     <No>                    │ 
     │                                                                    │ 
     └────────────────────────────────────────────────────────────────────┘ 
                                                                           
### I will use the current network setting as a static Ip address

     ┌───────────────────────┤ Static IP Address ├────────────────────────┐
     │                                                                    │ 
     │ Do you want to use your current network settings as a static       │ 
     │ address?                                                           │ 
     │                                                                    │ 
     │         IP address:    10.0.0.12/24                                │ 
     │         Gateway:       10.0.0.1                                    │ 
     │                                                                    │ 
     │                                                                    |
     │                                                                    │ 
     │                  <Yes>                     <No>                    │ 
     │                                                                    │ 
     └────────────────────────────────────────────────────────────────────┘



### we need to specify a Local User for the server.

     ┌──────────────────────────┤ Local Users ├───────────────────────────┐
     │                                                                    │ 
     │ Choose a local user that will hold your ovpn configurations.       │ 
     │                                                                    |
     │                                                                    │ 
     │                               <Ok>                                 │ 
     │                                                                    │ 
     └────────────────────────────────────────────────────────────────────┘ 

### Hit enter and you will be presented with the user selection page, choose pi (Which is the default User), and hit enter

     ┌─────────────────────────┤ Choose A User ├──────────────────────────┐
     │ Choose (press space to select):                                    │ 
     │                                                                    │ 
     │    (*) pi                                                          │ 
     │    ( ) ahmed9                                                      │ 
     │                                                                    |
     │                                                                    │ 
     │                 <Ok>                     <Cancel>                  │ 
     │                                                                    │ 
     └────────────────────────────────────────────────────────────────────┘ 
                                                                           
### We need to choose what type of VPN you like to use. It's the open VPN: Choose OpenVPN and hit Enter.


     ┌───────────────────────┤ Installation mode ├────────────────────────┐
     │ WireGuard is a new kind of VPN that provides near-instantaneous    │ 
     │ connection speed, high performance, and modern cryptography.       │ 
     │                                                                    │ 
     │ It's the recommended choice especially if you use mobile devices   │ 
     │ where WireGuard is easier on battery than OpenVPN.                 │ 
     │                                                                    │ 
     │ OpenVPN is still available if you need the traditional, flexible,  │ 
     │ trusted VPN protocol or if you need features like TCP and custom   │ 
     │ search domain.                                                     │ 
     │                                                                    │ 
     │ Choose a VPN (press space to select):                              │ 
     │                                                                    │ 
     │    ( ) WireGuard                                                   │ 
     │    (*) OpenVPN                                                     │ 
     │                                                                    │ 
     │                                                                    │ 
     │                 <Ok>                     <Cancel>                  │ 
     │                                                                    │ 
     └────────────────────────────────────────────────────────────────────┘ 
                                                                           

### It will prompt you to choose a protocol, options are TCP and UDP. I am using UDP because it is faster than TCP.


     ┌───────────────────────┤ Installation mode ├────────────────────────┐
     │                                                                    │ 
     │ PiVPN uses the following settings that we believe are good         │ 
     │ defaults for most users. However, we still want to keep            │ 
     │ flexibility, so if you need to customize them, choose Yes.         │ 
     │                                                                    │ 
     │ * UDP or TCP protocol: UDP                                         │ 
     │ * Custom search domain for the DNS field: None                     │ 
     │ * Modern features or best compatibility: Modern features (256 bit  │ 
     │ certificate + additional TLS encryption)                           │ 
     │                                                                    | 
     │                                                                    │ 
     │                  <Yes>                     <No>                    │ 
     │                                                                    │ 
     └────────────────────────────────────────────────────────────────────┘ 
                                                                            
###  I select the UDP port.

     ┌──────────────────────┤ Default openvpn Port ├──────────────────────┐
     │ You can modify the default openvpn port.                           │ 
     │ Enter a new value or hit 'Enter' to retain the default             │ 
     │                                                                    │ 
     │ 1194______________________________________________________________ │ 
     │                                                                    │ 
     │                                                                    |
     │                                                                    │ 
     │                 <Ok>                     <Cancel>                  │ 
     │                                                                    │ 
     └────────────────────────────────────────────────────────────────────┘ 
                                                                            

### Confirm the settings by selecting yes and hitting enter.

     ┌───────────────────┤ Confirm Custom Port Number ├───────────────────┐
     │                                                                    │ 
     │ Are these settings correct?                                        │ 
     │     PORT:   1194                                                   │ 
     │                                                                    │ 
     │                                                                    │ 
     │                  <Yes>                     <No>                    │ 
     │                                                                    │ 
     └────────────────────────────────────────────────────────────────────┘ 
                                                                            
### prompted to select a DNS provider. I am selecting Google as my DNS provider.

Setup PiVPN

     ┌──────────────────────────┤ DNS Provider ├──────────────────────────┐
     │ Select the DNS Provider for your VPN Clients (press space to       │ 
     │ select).                                                           │ 
     │ To use your own, select Custom.                                    │ 
     │                                                                    │ 
     │ In case you have a local resolver running, i.e. unbound, select    │ 
     │ "PiVPN-is-local-DNS" and make sure your resolver is listening on   │ 
     │ "10.8.0.1", allowing requests from "10.8.0.0/24".                  │ 
     │                                                                    │ 
     │    ( ) DNS.WATCH                                                   │ 
     │    ( ) Norton                                                  ▒   │ 
     │    ( ) FamilyShield                                            ▒   │ 
     │    ( ) CloudFlare                                                  │ 
     │    (*) Google                                                  ▒   │ 
     │    ( ) PiVPN-is-local-DNS                                          │ 
     │                                                                    │ 
     │                                                                    │ 
     │                 <Ok>                     <Cancel>                  │ 
     │                                                                    │ 
     └────────────────────────────────────────────────────────────────────┘ 
                                                                            
 ### We have to enter your dynamic DNS server name and hit enter, if everything is alright, you will receive your public IP address in the raspberry pi console.                                                                           
     ┌────────────────────────┤ Public IP or DNS ├────────────────────────┐
     │ Will clients use a Public IP or DNS Name to connect to your server │ 
     │ (press space to select)?                                           │ 
     │                                                                    │ 
     │    (*) 24.17.196.59  Use this public IP                            │ 
     │    ( ) DNS Entry     Use a public DNS                              │ 
     │                                                                    |
     │                 <Ok>                     <Cancel>                  │ 
     │                                                                    │ 
     └────────────────────────────────────────────────────────────────────┘ 
                                                                     
  ### Telling us to enable automatic updates for bug fixes and security updates.                                 

     ┌──────────────────────┤ Unattended Upgrades ├───────────────────────┐
     │                                                                    │ 
     │ Since this server will have at least one port open to the          │ 
     │ internet, it is recommended you enable unattended-upgrades.        │ 
     │ This feature will check daily for security package updates only    │ 
     │ and apply them when necessary.                                     │ 
     │ It will NOT automatically reboot the server so to fully apply some │ 
     │ updates you should periodically reboot.                            │ 
     │                                                                    |
     │                                                                    │ 
     │                               <Ok>                                 │ 
     │                                                                    │ 
     └────────────────────────────────────────────────────────────────────┘ 
                                                                            
### Hit yes here

     ┌──────────────────────┤ Unattended Upgrades ├───────────────────────┐
     │                                                                    │ 
     │ Do you want to enable unattended upgrades of security patches to   │ 
     │ this server?                                                       │ 
     │                                                                    |
     │                                                                    │ 
     │                  <Yes>                     <No>                    │ 
     │                                                                    │ 
     └────────────────────────────────────────────────────────────────────┘ 
                                                                            
### It will run the code and install everything necessary.

### we have to log back into the raspberry pi and run pivpn add

 it so.

     ┌─────────────────────┤ Installation Complete! ├─────────────────────┐
     │                                                                    │ 
     │ Now run 'pivpn add' to create the client profiles.                 │ 
     │ Run 'pivpn help' to see what else you can do!                      │ 
     │                                                                    │ 
     │ If you run into any issue, please read all our documentation       │ 
     │ carefully.                                                         │ 
     │ All incomplete posts or bug reports will be ignored or deleted.    │ 
     │                                                                    │ 
     │ Thank you for using PiVPN.                                         │ 
     |                                                                    |
     │                               <Ok>                                 │ 
     │                                                                    │ 
     └────────────────────────────────────────────────────────────────────┘ 
                                                                            
## Finally, you need to reboot your pi and finish the setup process.

     ┌─────────────────────────────┤ Reboot ├─────────────────────────────┐
     │                                                                    │ 
     │ It is strongly recommended you reboot after installation.  Would   │ 
     │ you like to reboot now?                                            │ 
     |                                                                    |
     │                                                                    │ 
     │                  <Yes>                     <No>                    │ 
     │                                                                    │ 
     └────────────────────────────────────────────────────────────────────┘ 
                                                                            
## NOW
After, the Raspberry Pi reboots log back into the Pi using SSH and run the command:
```
pivpn add
```
This will create a new VPN profile, we need to create a VPN profile for every device we need to connect to. When you enter pivpn add into your terminal and hit enter, you will be prompted with some options, which is shown below.
```
pi@raspberrypi:~ $ pivpn add
::: Create a client ovpn profile, optional nopass
:::
::: Usage: pivpn <-a|add> [-n|--name <arg>] [-p|--password <arg>]|[nopass] [-d|--days <number>] [-b|--bitwarden] [-i|--iOS] [-o|--ovpn] [-h|--help]
:::
::: Commands:
:::  [none]               Interactive mode
:::  nopass               Create a client without a password
:::  -n,--name            Name for the Client (default: 'raspberrypi')
:::  -p,--password        Password for the Client (no default)
:::  -d,--days            Expire the certificate after specified number of days (default: 1080)
:::  -b,--bitwarden       Create and save a client through Bitwarden
:::  -i,--iOS             Generate a certificate that leverages iOS keychain
:::  -o,--ovpn            Regenerate a .ovpn config file for an existing client
:::  -h,--help            Show this help dialog

Enter a Name for the Client:  ahmed9
How many days should the certificate last?  1080
Enter the password for the client:  
Enter the password again to verify:  
spawn ./easyrsa build-client-full ahmed9

Client's cert found: ahmed9.crt
Client's Private Key found: ahmed9.key
CA public Key found: ca.crt
tls Private Key found: ta.key


========================================================
Done! ahmed9.ovpn successfully created! 
ahmed9.ovpn was copied to:
  /home/pi/ovpns
for easy transfer. Please use this profile only on one
device and create additional profiles for other devices.
========================================================
```



