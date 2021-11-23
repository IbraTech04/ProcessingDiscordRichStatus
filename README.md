# ProcessingDiscordRichStatus
Simple script to display rich status when user is in the Processing IDE

This script uses the Windows win32gui python module, along with psutil to view what apps the user has open, along with which apps are open in the foreground. With this information, the script will update the users Discord Rich Status accordingly

As of right now the script only works on Windows NT. I see no reason for it not to work on macOS or Linux, however that would require the usage of different modules since the modules i currenty use are OS-specific
