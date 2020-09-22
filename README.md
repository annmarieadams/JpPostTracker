# JpPostTracker
## About
This script sends a text message alert when a package from Japan Post is on it's way to the user's home. 
## How to Use
This script takes 3 arguments the first time it is run: 1) the tracking number, 2) a phone number (digits only), 3) the SMS email gateway (in the @ format --ex @vtext.com)
You will need to enable the gmail API to use this script and place a `credentials.json` file in the same folder as the script. [(See here)](https://developers.google.com/gmail/api/quickstart/python/)
The first time this program is run you will need to give the script access to the gmail account the `credentials.json` file is associated with.
### Other Information
Personally I use this script on a task scheduler when I'm expecting a package and remove it afterwards. This script is pretty dirty, it lacks input validation and you might encounter some problems trying to use EZGmail. I might try to make some improvements to it in the future.
