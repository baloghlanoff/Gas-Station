from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

root = Tk()
root.geometry("500x500")
root.title("Gas Station")
root.state("zoomed")

screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()

# girisFrame = Frame(root, width=screenWidth, height=screenHeight)
# girisFrame.pack(fill="both", expand=True)



# image = Image.open("C:\\Users\\balog\\Desktop\\Gas Station\\GasStation\\gas-station-with-oil-pump-and-market-on-road-free-vector.jpg")
# image = image.resize((screenWidth, screenHeight))
# bgPhoto = ImageTk.PhotoImage(image)

# bgFrame = Frame(girisFrame)
# bgFrame.place(x=0, y=0, relwidth=1, relheight=1)

# bgLabel = Label(bgFrame, image=bgPhoto)
# bgLabel.pack(fill="both", expand=True)




# def startGame():
#     for widget in girisFrame.winfo_children():  # winfo_children() ekrandaki butun widgetleri verir.
#        if widget != bgFrame:
#             widget.destroy()
#     root.after(3000, game)
#     # game()   #-----------------
#     Label(girisFrame, text="Yüklənir...", font=("Verdana Bold", 44, "bold"), width=screenWidth, height= 2, fg="red", bg="#8dc79d").pack(pady=300)

# def showStartScreen():
#     for widget in girisFrame.winfo_children():
#         if widget != bgFrame:
#             widget.destroy()

#     basLabel = Label(girisFrame, text="⛽ GAS STATION ⛽", font=("Verdana Bold", 54, "bold"), width=screenWidth, height= 2, fg="#f4f4f4", bg="#8dc79d")
#     basLabel.pack(pady=(0, 150))
#     Button(girisFrame, text="Start", font=("Georgia", 40, "bold"), command=startGame, bg="green", fg="#f4f4f4", width=15).pack(pady=(50, 0))
#     Button(girisFrame, text="Quit", font=("Georgia", 40, "bold"), command=root.quit, bg="red", fg="#f4f4f4", width=15).pack(pady=30)


# def game():
#     global screenHeight, screenWidth, bgPhoto1, carImg, masin, gameFrame, pump_x, pump_y
#     girisFrame.forget()

#     gameFrame = Canvas(root, width=screenWidth, height=screenHeight)
#     gameFrame.pack(fill="both", expand=True)

#     image1 = Image.open("C:\\Users\\balog\\Desktop\\Gas Station\\GasStation\\A whimsical cartoon illustration of an empty gas station and a bustling market, viewed from the front, both buildings occupying the full frame. The photo should look lie this.jpg")
#     image1 = image1.resize((screenWidth, screenHeight))
#     bgPhoto1 = ImageTk.PhotoImage(image1)
#     gameFrame.create_image(0, 0, image=bgPhoto1, anchor="nw")


#     pump_x = 400  #}
#     pump_y = 600  #}   Dayanmaq istediyimiz kordinatin x ve y kordinatlari

#     root.bind("<KeyPress>", moveCar)    #keypress kodunu yazib klaviatura ile hereket etdirmeyi aktiv edirik.

#     gameFrame.create_text(pump_x-50, pump_y+195, text="➡", font=("Arial", 60), fill="red")   #Ox yaradiriq ki hara getmeli oldugumuzu bildirsin
#     gameFrame.create_text(pump_x-120, pump_y-500, text="Ox simvoluna gedin.", fill="red", font=("Comic Sans Ms", 40, "bold"))


#     image2 = Image.open("C:\\Users\\balog\\Desktop\\Gas Station\\GasStation\\Adobe Express - file (16).png")
#     image2 = image2.resize((500, 370))  # kiçiltmək üçün
#     carImg = ImageTk.PhotoImage(image2)
#     masin = gameFrame.create_image(screenWidth, screenHeight, image=carImg, anchor="se")   #canvasla yaradiriq ki backgroundu olmasin


#     x, y = gameFrame.coords(masin)   #masinin kordinatlarini goturur


# def moveCar(event):
#     global gameFrame, masin, pump_x, pump_y, fuelSelection, bgPump
#     step = 15   #masinin nece pixel-pixel hereket edeceyini yazmisiq
#     x, y = gameFrame.coords(masin)   

#     if abs(x - pump_x-170) < 50 and abs(y - pump_y-400) < 50:    #abs kodu deqiq hesablama ucun istifade olunur. 
#         return
    
#     if event.keysym == "a":    #keysym kodu klaviaturayla basdigimiz klavisin deyerini goturur.
#         x -= step
#     elif event.keysym == "d":
#         x += step

#     gameFrame.coords(masin, x, y)    #Son oldugu yerin kordinatlarini gotururuk

#     if abs(x - pump_x-170) < 50 and abs(y - pump_y-400) < 50:    #abs kodu deqiq hesablama ucun istifade olunur. 
#         root.after(1500)
#         gameFrame.forget()
#         openFuelSelection()


a92Frame = None
a95Frame = None
dieselFrame = None
selectedFuel = None
fuelTotal = 0

def hideAllFrames():
    global a92Frame, a95Frame, dieselFrame
    if a92Frame:
        a92Frame.place_forget()   #Her seyi place ile yerlesdirmdiyimize gore place_forget veririk
    if a95Frame: 
        a95Frame.place_forget()
    if dieselFrame: 
        dieselFrame.place_forget()


def openFuelSelection():
    global fuelSelection, bgPump
    fuelSelection = Canvas(root, width=screenWidth, height=screenHeight)
    fuelSelection.pack(fill=BOTH, expand=True)

    pumpImg = Image.open("C:\\Users\\balog\\Desktop\\Gas Station\\GasStation\\gas pumps. 3 gas pump viewing from front. Like cartoon. a92, a95 and diesel.jpg")
    pumpImg = pumpImg.resize((screenWidth, screenHeight))
    bgPump = ImageTk.PhotoImage(pumpImg)
    fuelSelection.create_image(0, 0, image=bgPump, anchor="nw")

    
    def submit():
        global fuelTotal
        if selectedFuel is None:
            print("Heç bir yanacaq seçilməyib!")
            return
        fuelTotal = litr.get() * litrPrice
        print(f"Seçilən yanacaq: {selectedFuel}, Litr: {litr.get()}, Ödəniş: {round(fuelTotal, 1)} AZN")

    Button(fuelSelection, text="Submit", font=("Arial", 30), width=13, bg="green", fg="white",
           command=submit).place(x=635, y=30)


    def a92():
        global a92Frame, a95Frame, dieselFrame, selectedFuel, litrPrice, litr
        
        hideAllFrames()

        selectedFuel = "A92"

        litr = IntVar(value=1)
        litrPrice = 1.2

        def updateLabels():
            a92Litr.config(text=f"{litr.get()} Litr")
            a92Azn.config(text=f"{round(litr.get() * litrPrice, 1)} Azn")

        def decrease():
            if litr.get() > 1:
                litr.set(litr.get() - 1)
                updateLabels()
        
        def increase():
            litr.set(litr.get() + 1)
            updateLabels()

        a92Frame = Frame(fuelSelection, width=120, height=60)
        a92Frame.place(x=305, y=330)
        
        Button(a92Frame, text="-", font=("Arial", 20), width=1, height=1, command=decrease).place(x=0, y=0)

        a92Litr = Label(a92Frame, text=f"{litr.get()} Litr", font=("Arial", 15))
        a92Litr.place(x=22, y=0)
        a92Azn = Label(a92Frame, text=f"{litrPrice} Azn", font=("Arial", 12, "bold"))
        a92Azn.place(x=22, y=30)

        Button(a92Frame, text="+", font=("Arial", 20), width=1, height=1, command=increase).place(x=90, y=0)



    def a95():
        global a92Frame, a95Frame, dieselFrame, selectedFuel, litrPrice, litr

        hideAllFrames()
            
        selectedFuel = "A95"

        litr = IntVar(value=1)
        litrPrice = 1.6

        def updateLabels():
            a95Litr.config(text=f"{litr.get()} Litr")
            a95Azn.config(text=f"{round(litr.get() * litrPrice, 1)} Azn")

        def decrease():
            if litr.get() > 1:
                litr.set(litr.get() - 1)
                updateLabels()
        
        def increase():
            litr.set(litr.get() + 1)
            updateLabels()

        a95Frame = Frame(fuelSelection, width=120, height=60)
        a95Frame.place(x=720, y=330)
        
        Button(a95Frame, text="-", font=("Arial", 20), width=1, height=1, command=decrease).place(x=0, y=0)

        a95Litr = Label(a95Frame, text=f"{litr.get()} Litr", font=("Arial", 15))
        a95Litr.place(x=22, y=0)
        a95Azn = Label(a95Frame, text=f"{litrPrice} Azn", font=("Arial", 12, "bold"))
        a95Azn.place(x=22, y=30)

        Button(a95Frame, text="+", font=("Arial", 20), width=1, height=1, command=increase).place(x=90, y=0)


    def diesel():
        global a92Frame, a95Frame, dieselFrame, selectedFuel, litrPrice, litr
        
        hideAllFrames()

        selectedFuel = "Diesel"

        litr = IntVar(value=1)
        litrPrice = 1.0

        def updateLabels():
            dieselLitr.config(text=f"{litr.get()} Litr")
            dieselAzn.config(text=f"{round(litr.get() * litrPrice, 1)} Azn")

        def decrease():
            if litr.get() > 1:
                litr.set(litr.get() - 1)
                updateLabels()
        
        def increase():
            litr.set(litr.get() + 1)
            updateLabels()


        dieselFrame = Frame(fuelSelection, width=120, height=60)
        dieselFrame.place(x=1123, y=330)
        
        Button(dieselFrame, text="-", font=("Arial", 20), width=1, height=1, command=decrease).place(x=0, y=0)

        dieselLitr = Label(dieselFrame, text=f"{litr.get()} Litr", font=("Arial", 15))
        dieselLitr.place(x=22, y=0)
        dieselAzn = Label(dieselFrame, text=f"{litrPrice} Azn", font=("Arial", 12, "bold"))
        dieselAzn.place(x=22, y=30)

        Button(dieselFrame, text="+", font=("Arial", 20), width=1, height=1, command=increase).place(x=90, y=0)


    Button(fuelSelection, text="A92", font=("Comic Sans Ms", 25), width=5, bg="yellow", command=a92).place(x=320, y=730)
    Button(fuelSelection, text="A95", font=("Comic Sans Ms", 25), width=5, bg="red", fg="white", command=a95).place(x=730, y=730)
    Button(fuelSelection, text="Diesel", font=("Comic Sans Msa", 25), width=5, bg="blue", fg="white", command=diesel).place(x=1140, y=730)


    

openFuelSelection()


# showStartScreen()

root.mainloop() 