from pygame import joystick

#function to check if the joysticks are initialized
def initJoysticks():
    for x in range (joystick.get_count()):
        j = joystick.Joystick(x)
        j.init()
        #print the name of every joystick pygame is able to detect in the terminal
        txt = "Enabled joystick: " + j.get_name()
        print(txt)
    #if no joysticks are detected, print "no joysticks to initialize" in the terminal   
    if not joystick.get_count():
        print("No Joysticks to Initialize")
