<h1>LARS' USB SCANNER</h1>

<h2>INSTALLATION GUIDE:</h2>

1. RUN 'sudo apt update' | *This will update apt instance*
2. RUN 'sudo apt install git pip python usbguard usbutils udisks2' | *Install required packages for this project*
3. RUN 'sudo systemctl enable usbguard.service --now' | *Will enable USBGuard service and configure it to run on boot*
4. RUN 'sudo git clone https://github.com/larsje99/usbscanner.git' | *Clone the repository into home directory*
5. RUN 'cd usbscanner/usbscanner' | *Navigate to the folder*
6. RUN 'sudo mv usbscannerlars /usr/local/bin' | *Move the bash script to PATH environment*
7. RUN 'sudo chmod +x /usr/local/bin/usbscannerlars' | *Make the script executable*
8. RUN 'cd ..' | *Go back to home directory*
9. RUN 'sudo usbscannerlars' | *Now you can run the script!*

VERSION 0.0.1
FUTURE UPDATES COMING SOON!
