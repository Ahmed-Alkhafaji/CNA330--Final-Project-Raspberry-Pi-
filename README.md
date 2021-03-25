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
### It might you need curl tool, to install it:
```
sudo apt-get install curl
```
## To install Pi-hole, run this command:
```
curl -sSL https://install.pi-hole.net | bash
```
## Installing OpenVPN with PiVPN in Raspberry Pi Zero
By following the steps below and you will have a VPN server in no time.

### Installation
```
curl -L https://install.pivpn.io | bash
```
### Installation
```
curl -L https://install.pivpn.io | TESTING- bash
```







