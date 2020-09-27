import pyttsx3
import os
import speech_recognition as sr

# pyttsx3.speak("Welcome to my tools")

# IDE
print("ALl IDE'S ARE AVAILABLE HERE")
print("Pleas Say to Open Visual Studio code")
print("Pleas Say to Open NetBeans IDE")
print("Pleas Say to Open Pycharm IDE")

print()

# COMMON USE
print("COMMON USE")
print("Pleas Say to Open Chrome Browser")
print("Pleas Say to Open Notepad")
print("Pleas Say to Open File Explorer")

print()

# OFFICE AREA
print("OFFICE AREA")
print("Pleas Say to Open Microsoft Word")
print("Pleas Say to Open Microsoft Paint")
print("Pleas Say to Open Microsoft Access")  # MSACCESS #
print("Pleas Say to Open Microsoft Publisher")  # MSPUB #
print("Pleas Say to Open Microsoft Outlook")  # OUTLOOK #
print("Pleas Say to Open Microsoft PowerPoint")  # POWERPNT #
print("Pleas Say to Open Microsoft Skype for Bussiness")  # lync #
print("Pleas Say to Open Microsoft Manage Microsoft offlice file upload to Webservers")  # MSOUC #
print("Pleas Say to Open Microsoft Skype for Business Recording Manager")  # OcPubMgr #
print("Pleas Say to Open Microsoft Outlook Mail Setup")  # OLCFG #
print("Pleas Say to Open Microsoft Organization Chart Add-in for Microsoft Office programs")  # ORGCHART #

print("Write exit to leave")
print()



while True:
  obj =sr.Recognizer()

  with sr.Microphone() as source:
    print("Please Pleas Say your cmd to run")
    audio = obj.listen(source)
    print("Done")

    
    p= obj.recognize_google(audio)
    print(p)
    
    if not ("do not" in p) or "don't" in p:
        # 1
        if (("run" in p) or ("execute" in p)) and (("chrome" in p) or ("chromebrowser" in p)):
            os.system("chrome")
        # 2
        elif (("run" in p) or ("execute" in p)) and (("NetBeans IDE" in p) or ("netbeanside" in p)):
            os.system("netbeans")
        # 3
        elif (("run" in p) or ("execute" in p)) and (
                ("Microsoft" in p) or ("MicrosoftWord" in p) or ("msword" in p) or ("Word" in p) or ("msword" in p)):
            os.system("winword")
        # 4
        elif (("run" in p) or ("execute" in p)) and (
                ("Microsoft" in p) or ("MicrosoftExcel" in p) or ("msexcel" in p) or ("excel" in p)):
            os.system("excel")
        # 5
        elif (("run" in p) or ("execute" in p)) and (("notepad" in p) or ("editor" in p)):
            os.system("notepad")
        # 6
        elif (("run" in p) or ("execute" in p)) and (("control panel" in p) or ("panel" in p)):
            os.system("control panel")

        # 7
        elif (("run" in p) or ("execute" in p)) and (
                ("Microsoft" in p) or ("MicrosoftAccess" in p) or ("msaccess" in p) or ("access" in p) or (
                "msaccess" in p)):
            os.system("MSACCESS")
        # 8
        elif (("run" in p) or ("execute" in p)) and (
                ("Microsoft" in p) or ("MicrosoftPublisher" in p) or ("mspublisher" in p) or ("publisher" in p) or (
                "mspublisher" in p)):
            os.system("MSPUB")
        # 9
        elif (("run" in p) or ("execute" in p)) and (
                ("Microsoft" in p) or ("MicrosoftOutlook" in p) or ("msoutlook" in p) or ("outlook" in p) or (
                "msoutlook" in p)):
            os.system("OUTLOOK")
        # 10
        elif (("run" in p) or ("execute" in p)) and (
                ("Microsoft" in p) or ("MicrosoftPowerpoint" in p) or ("mspowerpoint" in p) or ("powerpoint" in p) or (
                "mspowerpoint" in p)):
            os.system("POWERPNT")
        # 11
        elif (("run" in p) or ("execute" in p)) and (
                ("Microsoft" in p) or ("Microsoft Skype for Bussiness" in p) or ("msskype" in p) or (
                "Skype for Bussiness" in p) or ("msskype for bussiness" in p)):
            os.system("lync")
        # 12
        elif (("run" in p) or ("execute" in p)) and (
                ("Microsoft" in p) or ("Microsoft offlice file upload to Webservers" in p) or (
                "msofflice file upload to webservers" in p) or ("offlice file upload to Webservers" in p) or (
                        "msofflice file upload to Webservers" in p)):
            os.system("MSOUC")
        # 13

        elif (("run" in p) or ("execute" in p)) and (
                ("Microsoft" in p) or ("Microsoft Skype for Business Recording Manager" in p) or (
                "msskype skype for business recording manager" in p) or (
                        "Skype for Business Recording Manager" in p) or (
                        "msSkype for Business Recording Manager" in p)):
            os.system("OcPubMgr")

        # 14
        elif (("run" in p) or ("execute" in p)) and (
                ("Microsoft" in p) or ("Microsoft Outlook Mail Setup" in p) or ("outlook main setup" in p) or (
                "Outlook Mail Setup" in p) or ("msoutlook mail setup" in p)):
            os.system("OLCFG")

        # 15
        elif (("run" in p) or ("execute" in p)) and (
                ("Microsoft" in p) or ("Microsoft Organization Chart Add-in for Microsoft Office programs" in p) or (
                "msskype organization chart add-in for microsoft office programs" in p) or (
                        "Organization Chart Add-in for Microsoft Office programs" in p) or (
                        "msOrganization Chart Add-in for Microsoft Office programs" in p)):
            os.system("ORGCHART")

        # 16
        elif (("run" in p) or ("execute" in p)) and (
                ("Microsoft" in p) or ("Microsoft Paint" in p) or ("msskype paint" in p) or ("paint" in p) or (
                "mspaint" in p)):
            os.system("mspaint")

        # Exit
        elif ("exit" in p) or ("quit" in p):
            break

        else:
            print("Please say it again and correctly")

    else:
        print("Sorry But You ask to don't run")


print("Thanks for Using My Machine")
