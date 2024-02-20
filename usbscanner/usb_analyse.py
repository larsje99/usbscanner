def main():
    import subprocess
    import time
    import sys
    list_of_red_flags = ['Self Powered', 'Human Interface Device', 'Boot Interface Subclass', 'Keyboard', 'HID', 'bNumEndpoints           1', 'Interrupt']
    device_id = []
    
    def parse_usb_info(usb_info):
        list_of_important_fields = ['idVendor', 'idProduct', 'bmAttributes', 'Powered', 'bNumEndpoints', 'bInterfaceClass', 'bInterfaceSubClass', 'bInterfaceProtocol', 'HID', 'Endpoint Descriptor', 'bEndpointAddress', 'Transfer Type']
        list_of_flags = []
        lines = iter(usb_info.split('\n'))
        
        for line in lines:
            if line.startswith('Bus'):
                device = line
                confirmation = input("Do you want to analyze this device: " + "|" + device + "|" + "? " + "TYPE YES OR NO: ")
                if confirmation == "YES":
                    testing = device.split(' ')
                    code = testing[5]
                    device_id.append(code)
                    while True:
                        next_line = next(lines)
                        if next_line.startswith('Bus') or next_line == '':
                            print("\n")
                            break
                        for field in list_of_important_fields:
                            if field in next_line:
                                if field == 'idVendor':
                                    list_of_flags.append("\n-------------------------------------------------------------\n\n")
                                list_of_flags.append(next_line)
                                break
                    print("-----------------------------\n\033[1mDEVICE ANALYZED\033[0m\n-----------------------------\n\n")
                elif confirmation == "NO":
                    print("\n\n-----------------------------\n\033[1mSKIPPING TO NEXT DEVICE\033[0m\n-----------------------------\n\n")
                else:
                    print("\n\033[1mError, please input YES or NO\033[0m\n")

        return list_of_flags

    text = "LARS' BADUSB ANALYZER"
    box_width = len(text) + 4
    print("\n")
    print("*" * box_width)
    print("* {:^{}s} *".format(text, len(text)))
    print("*" * box_width)

    print("\n------------------------------------------------\n\033[1mALWAYS BE CRITICAL AND LOOK AT THE FULL REPORT!\033[0m\n------------------------------------------------\n")

    red_flags_counter = 0

    while True:
        input_choice = input("TYPE \'full\' FOR THE FULL USB REPORT, TYPE \'indiv\' FOR INDIVIDUAL USB ANALYSES: ")

        if input_choice == "full":
            lsusb_output = subprocess.run(['lsusb', '-v'], capture_output=True, text=True)

            if lsusb_output.returncode == 0:
                usb_info = lsusb_output.stdout
                print(usb_info)
                sys.exit()
                break
                
        elif input_choice == "indiv":
            lsusb_output = subprocess.run(['lsusb', '-v'], capture_output=True, text=True)

            if lsusb_output.returncode == 0:
                usb_info = lsusb_output.stdout
                print("\n")
                parsed_usb_info = parse_usb_info(usb_info)

                print("\n-----------------------------\n\033[1mRESULTS OF ANALYSES\033[0m\n-----------------------------\n↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓\n")
                for item in parsed_usb_info:
                    for red_flag in list_of_red_flags:
                        if red_flag in item:
                            red_flags_counter += 1
                    print(item)
            
                if red_flags_counter == 0:
                    text2 = "NO POTENTIAL RED FLAGS HAVE BEEN FOUND!"
                    box_width = len(text2) + 4
                    print("\n")
                    print("*" * box_width)
                    print("* {:^{}s} *".format(text2, len(text2)))
                    print("*" * box_width)
                    print("\n")
                    break
                elif red_flags_counter != 0:
                    text3 = str(red_flags_counter) + " POTENTIAL RED FLAGS DETECTED!"
                    box_width = len(text3) + 4
                    print("\n")
                    print("*" * box_width)
                    print("* {:^{}s} *".format(text3, len(text3)))
                    print("*" * box_width)
                    print("\n")
                    break
                    
            else:
                print("Error running lsusb command. Exit code:", lsusb_output.returncode)
                break
                
        else:
            print("\n-------------------------------------------------\nINVALID CHOICE, PLEASE CHOOSE \'full\' OR \'indiv\'\n-------------------------------------------------\n")
    
    print("********************************************************************************")
    time.sleep(4)
    print("\n-----------------------------\n\033[1mAUTHORIZING ANALYZED DEVICES\033[0m\n-----------------------------\n")
    
    for code in device_id:
        lines = iter(usb_info.split('\n'))
        for line in lines:
            if line.startswith('Bus') and code in line:
                authorize_confirm = input("\nDO YOU WANT TO AUTHORIZE THIS DEVICE FOR USE (WARNING USB WILL BE MOUNTED): " + line + " | TYPE \'YES\' OR \'NO\' \n: ")
                if authorize_confirm == "YES":
                    subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', f'sudo usbguard allow-device {code}'])
                                       
                else:
                    print("PASS")
    
if __name__ == "__main__":
    main()

