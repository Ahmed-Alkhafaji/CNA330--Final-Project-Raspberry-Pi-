# CNA330--Final-Project-Raspberry-Pi-

# CNA330 Raspberry-Pi Final Project
## What is a Pi-hole?
Pi-hole is a network-wide ad blocker.
I will install and set up a Pi-hole on Raspberry Pi to block advertisements on all devices connected to my home network.

## what is the benefit of using Pi-hole?
#### - PI-HOLE CAN MAKE YOUR NETWORK FASTER:
Pi-hole work at the DNS level.  So when an ad is blocked, it’s actually prevented from being downloaded 
in the first place because the DNS query is intercepted. Since these ad images, videos, and sounds are not being downloaded, your network will perform better.
#### -  PI-HOLE CAN PROTECT YOUR NETWORK FROM MALWARE:
We can add additional block lists to your installation that will prevent domains that are known to serve malware or act as a phishing site from ever entering your network.
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
