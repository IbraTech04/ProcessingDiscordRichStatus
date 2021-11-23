from pypresence import Presence #Library Importing
import time
import time
from time import mktime
import psutil    
import win32gui

w=win32gui #Initializing win32gui
client_id = '912812476335259668'  #Client ID for HitFilm Express
RPC = Presence(client_id) #Setting up RPC connection
counter = 0
RPC.connect() #Connecting to RPC
mouse = win32gui.GetCursorPos()
print(mktime(time.localtime()))
while True: #Main Loop
    if ("javaw.exe" in (p.name() for p in psutil.process_iter())): #Checks if the program is runing
        start_time = mktime(time.localtime()) #Sets start time
        #start_time = 1535857560.0 #Sets start time
        while ("javaw.exe" in (p.name() for p in psutil.process_iter())): #While the user is still in HitFilm Express
            prevMouse = mouse
            mouse = win32gui.GetCursorPos()
            if (prevMouse == mouse):
                counter = counter + 1
            else:
                counter = 0
            status = ""
            state = ""
            if ("Open" in w.GetWindowText (w.GetForegroundWindow())): ##If the user is in the HitFilm window
                state = "In a file" 
                status = "Opening a sketch"
            elif ("Processing" in w.GetWindowText (w.GetForegroundWindow())): ##If the user is in the HitFilm window
                state = "In a File" 
                status = w.GetWindowText (w.GetForegroundWindow()).split("|",1)[0]
            else: ##If the user isn't even in the app in the first place
                state = "Idling"
                status = "Not even in the app lmao"
            if (counter >= 100):
                status = "Idling"
            (RPC.update(state=status, details=state, large_image="p5", small_image="java", small_text = "FXHome", large_text="HitFilm", start=start_time)) #Sending data
    RPC.clear() #If the while loop above does not (Meaning the user isn't in the app) run, clear the RPC (therefore removing the discord rich status)
    time.sleep(15) #Sleep for 5 seconds so the users PC doesn't blow up
