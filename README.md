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

  ──────────────────────────┤ Installing packages ├──────────────────────────┐
 │               Configuring netfilter-persistent (armhf)                    │ 
 │                                                                           │ 
 │                                                                           │ 
 │                                                                           │ 
 │                                    80%                                    │ 
 │                                                                           │ 
 └───────────────────────────────────────────────────────────────────────────┘

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

## Asking you to set up a static IP address for your Raspberry Pi, we do not need to do it.


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
                                                                           
## I will use the current network setting as a static Ip address

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



## we need to specify a Local User for the server.

     ┌──────────────────────────┤ Local Users ├───────────────────────────┐
     │                                                                    │ 
     │ Choose a local user that will hold your ovpn configurations.       │ 
     │                                                                    │ 
     │                                                                    │ 
     │                                                                    │ 
     │                                                                    │ 
     │                                                                    │ 
     │                                                                    │ 
     │                                                                    │ 
     │                                                                    │ 
     │                                                                    │ 
     │                                                                    │ 
     │                                                                    │ 
     │                                                                    │ 
     │                                                                    │ 
     │                                                                    │ 
     │                               <Ok>                                 │ 
     │                                                                    │ 
     └────────────────────────────────────────────────────────────────────┘ 

## Hit enter and you will be presented with the user selection page, choose pi (Which is the default User), and hit enter

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
                                                                           
## We need to choose what type of VPN you like to use. It's the open VPN: Choose OpenVPN and hit Enter.


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
                                                                           

## It will prompt you to choose a protocol, options are TCP and UDP. I am using UDP because it is faster than TCP.


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
                                                                            










