-DO NOT MERGE THIS FILE TO MASTER. THIS FILE SHOULD BE REMOVED BEFORE A MERGE
This tutorial was made by Eli Schiff if you need help figuring something out.

Testing the pwa on Android
- 1) Run `vagrant ssh`  
- 2) Run `sudo python3 /usr/local/submitty/GIT_CHECKOUT/Submitty/.setup/CONFIGURE_SUBMITTY.py`  
- 3) Keep everything the default value except:  
  - a) Set the url for submission to `http://localhost:8081`  
  - b) Set the authentication method to `Database`  
- 4) Run `sudo /usr/local/submitty/.setup/INSTALL_SUBMITTY.sh`  
- 5) Plug your phone into your computer  
- 6) Enable usb debugging and switch the mode to `PTP`  
- 7) Open up google chrome on your computer and go to `chrome://inspect/#devices`  
- 8) Click the port forwarding button and set it to foward `8081` to `192.168.56.111:80`  
- 9) Make sure to click the enable port forwarding checkbox  
- 10) Open `http://localhost:8081` on the chrome app on your phone  

Please note once you change the url you cannot open submitty on your computer.  
To change it back run steps 1-4 but used `http://192.168.56.111` as the url  
