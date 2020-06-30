import paho.mqtt.publish as publish
from tkinter import *
from tkinter import font

BACKGROUND = "yellow"
FONT = "comic sans ms"


def lightClickOn():
    lightOn = Label(window, text="Lights are on", bg=BACKGROUND)
    lightOn.place(x=465, y=120)
    lightOn.config(font=(FONT, 12))
    lightOn.after(1000, lambda: lightOn.destroy())
    publish.single("vishwas/lights", "LIGHT_ON", hostname="test.mosquitto.org")
    print("sent)")


def lightClickOff():
    lightOff = Label(window, text="Lights are off", bg=BACKGROUND)
    lightOff.place(x=465, y=120)
    lightOff.config(font=(FONT, 12))
    lightOff.after(1000, lambda: lightOff.destroy())
    publish.single("vishwas/lights", "LIGHT_OFF",
                   hostname="test.mosquitto.org")


def change_rgb():
    colour = "Changed to R:" + str(r.get()) + \
        " G:" + str(g.get()) + " B:" + str(b.get())
    changeLabel = Label(window, text=colour, bg=BACKGROUND)
    changeLabel.place(x=425, y=120)
    changeLabel.config(font=(FONT, 12))
    changeLabel.after(1000, lambda: changeLabel.destroy())
    msg = str(r.get()) + ":" + str(g.get()) + ":" + str(b.get())
    #publish.single("vishwas/colour", msg, hostname="iot.eclipse.org")


def coolerClickOff():
    coolerOff = Label(window, text="cooler is off", bg=BACKGROUND)
    coolerOff.place(x=465, y=120)
    coolerOff.config(font=(FONT, 12))
    coolerOff.after(1000, lambda: coolerOff.destroy())
    #publish.single("Automation/Cooler", "COOLER_OFF", hostname="iot.eclipse.org")


def coolerClickOn():
    coolerOn = Label(window, text="cooler is on", bg=BACKGROUND)
    coolerOn.place(x=465, y=120)
    coolerOn.config(font=(FONT, 12))
    coolerOn.after(1000, lambda: coolerOn.destroy())
    #publish.single("Automation/Cooler", "COOLER_ON", hostname="iot.eclipse.org")


def coolerSpeed():
    st = "cooler speed is " + str(speed.get())
    sLabel = Label(window, text=st, bg=BACKGROUND)
    sLabel.place(x=470, y=120)
    sLabel.config(font=(FONT, 12))
    sLabel.after(1000, lambda: sLabel.destroy())
    #publish.single("Automation/CoolerSpeed", str(speed.get), hostname="iot.eclipse.org")


def coolType():
    cool = "cooler type changed to cool"
    coolLabel = Label(window, text=cool, bg=BACKGROUND)
    coolLabel.place(x=430, y=120)
    coolLabel.config(font=(FONT, 12))
    coolLabel.after(1000, lambda: coolLabel.destroy())
    #publish.single("Automation/CoolerType", "COOL", hostname="iot.eclipse.org")


def coolSwingType():
    coolSwing = "cooler type changed to cool+swing"
    coolSwingLabel = Label(window, text=coolSwing, bg=BACKGROUND)
    coolSwingLabel.place(x=400, y=120)
    coolSwingLabel.config(font=(FONT, 12))
    coolSwingLabel.after(1000, lambda: coolSwingLabel.destroy())
    #publish.single("Automation/CoolerType", "COOLSWING", hostname="iot.eclipse.org")


def swingType():
    swing = "cooler type changed to swing"
    swingLabel = Label(window, text=swing, bg=BACKGROUND)
    swingLabel.place(x=430, y=120)
    swingLabel.config(font=(FONT, 12))
    swingLabel.after(1000, lambda: swingLabel.destroy())
    #publish.single("Automation/CoolerType", "SWING", hostname="iot.eclipse.org")


########MAIN WINDOW OPTIONS############
window = Tk()
window.geometry('1000x500')
myFont = font.Font(family='Times New Roman', weight='bold')
window.title("Automation")
window.configure(background=BACKGROUND)

v = IntVar()
w = IntVar()
x = IntVar()

########HEADER OPTIONS#############
head = Label(window, text="Automation Controls",
             anchor='center', bg=BACKGROUND)
head.place(x=375, y=0)
head.config(font=(FONT, 30, "bold"))

#########LIGHT ON/OFF CONFIG WITH BUTTONS########
lightLabel = Label(window, text="Lights:", bg=BACKGROUND)
lightLabel.place(x=475, y=50)
lightLabel.config(font=(FONT, 20, "bold"))

lights_on = Radiobutton(window, text="ON", command=lightClickOn,
                        padx=20, pady=10, indicatoron=0, variable=w, value=1, activebackground="blue")
lights_on.place(x=250, y=100)

lights_off = Radiobutton(window, text="OFF", command=lightClickOff,
                         padx=20, pady=10, indicatoron=0, variable=w, value=2, activebackground="blue")
lights_off.place(x=700, y=100)

##########RGB SLIDER SETTINGS###########
rgb = Label(window, text="Select RGB grading:", bg=BACKGROUND)
rgb.place(x=420, y=150)
rgb.config(font=(FONT, 18, "bold"))

# red
rLabel = Label(window, text="R:", bg=BACKGROUND)
rLabel.place(x=120, y=200)
rLabel.config(font=(FONT, 15))
r = Scale(window, from_=0, to=1024, orient=HORIZONTAL, bg=BACKGROUND)
r.place(x=150, y=200)

# green
gLabel = Label(window, text="G:", bg=BACKGROUND)
gLabel.place(x=440, y=200)
gLabel.config(font=(FONT, 15))
g = Scale(window, from_=0, to=1024, orient=HORIZONTAL, bg=BACKGROUND)
g.place(x=470, y=200)

# blue
bLabel = Label(window, text="B:", bg=BACKGROUND)
bLabel.place(x=760, y=200)
bLabel.config(font=(FONT, 15))
b = Scale(window, from_=0, to=1024, orient=HORIZONTAL, bg=BACKGROUND)
b.place(x=800, y=200)

# change to new values
change = Button(window, text="CHANGE", command=change_rgb, padx=20, pady=10)
change.place(x=470, y=250)


##########Cooler settings#############
coolerLabel = Label(window, text="Cooler:", bg=BACKGROUND)
coolerLabel.place(x=475, y=325)
coolerLabel.config(font=(FONT, 20, "bold"))

cooler_off = Radiobutton(window, text="OFF", command=coolerClickOff, indicatoron=0,
                         padx=10, pady=5, variable=x, value=2, activebackground="blue")
cooler_off.place(x=600, y=325)

cooler_on = Radiobutton(window, text="ON", command=coolerClickOn, indicatoron=0,
                        padx=10, pady=5, variable=x, value=1, activebackground="blue")
cooler_on.place(x=375, y=325)

# slider for speed
speedLabel = Label(window, text="Speed:", bg=BACKGROUND)
speedLabel.place(x=180, y=375)
speedLabel.config(font=(FONT, 16, "bold"))
speed = Scale(window, from_=0, to=3, orient=HORIZONTAL,
              bg=BACKGROUND)
speed.place(x=250, y=375)
speedChange = Button(window, text="CHANGE",
                     command=coolerSpeed, bg="black", padx=8, pady=5)
speedChange.place(x=360, y=390)

# radio button for type of cooling
cool = Radiobutton(window, text="cool", padx=20, variable=v,
                   command=coolType, value=1, bg=BACKGROUND, fg="black", font="helvetica 16 bold").place(x=550, y=390)
cool_swing = Radiobutton(window, text="cool+swing", padx=20, variable=v, command=coolSwingType,
                         value=2, bg=BACKGROUND, fg="black", font="helvetica 16 bold").place(x=670, y=390)
swing = Radiobutton(window, text="swing", padx=20, variable=v, command=swingType,
                    value=3, bg=BACKGROUND, fg="black", font="helvetica 16 bold").place(x=850, y=390)


##############Encryption#################
#cipher_key = Fernet.generate_key()
# print(cipher_key)


################windowLoop################
window.mainloop()
