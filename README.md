# Turn the Raspberry PI into A VPN Server with OpenVPN

## What is a VPN?
A VPN stands for Virtual Private Network which means it gives you privacy online. Initially, VPNs were used by big organizations and governments because of obvious security reasons, but nowadays VPNs are used by everyone because it ensures privacy and data security.

1- Your locations stay private

2- Your data is encrypted

3- You can surf the web anonymously

## what is the benefit of using VPN ?
By enabling a VPN, you are adding an extra layer of security to your network

#### - PI-HOLE CAN MAKE YOUR NETWORK FASTER:
Pi-hole work at the DNS level.  So when an ad is blocked, it’s actually prevented from being downloaded 
in the first place because the DNS query is intercepted. Since these ad images, videos, and sounds are not being downloaded, your network will perform better.

#### -  What will we use the VPN for ?
We will set up a VPN server on the home network using a Raspberry Pi. This way we can securely connect to my local network while we are not home. Also, we just don't want to leave an SSH port open for just anybody to hack in. 
When you send your data online, a VPN creates a tunnel between you and your called server, it is done by utilizing a second server, when you request a page on the internet without the VPN, it goes directly to your requested server, but with VPN enabled, your request gets encrypted and goes to the server of your VPN provider, and then it goes to your requested server.
#### -  PI-HOLE CAN BLOCK ADS IN NON-TRADITIONAL PLACES:
Advertisements in smart TVs and mobile apps can’t be blocked by browser-based ad blockers because smart TVs and  mobile apps don’t run in a browser.  This is where Pi-hole shines; since the ads are prevented at the network level (before the ads reach the device), you can prevent ads from appearing on Internet-connected devices that aren’t 
a Web browser.
## How does the Pi-hole work?
Pi-hole functions as an internal, private DNS server for my home network.
Usually the DNS server is running on the router. So, I will install Pi-hole on the Raspberry Pi and sets the Raspberry Pi to be the DNS for my home network.
Pi-hole will intercept any queries for known ad-serving domains and deny them access, so ads won’t be downloaded.

## Project Prerequisites:
- Raspberry Pi Zero W with Raspbian Lite image installed on it.

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
### Follow this instruction to finish the installation: (press enter to continue)
