from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk, ImageOps
from tkinter import messagebox


root = Tk()
root.geometry("500x500")
root.title("Gas Station")
root.state("zoomed")

screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()

girisFrame = Frame(root, width=screenWidth, height=screenHeight)
girisFrame.pack(fill="both", expand=True)



image = Image.open("GasStation\\bg.jpg")
image = image.resize((screenWidth, screenHeight))
bgPhoto = ImageTk.PhotoImage(image)

bgFrame = Frame(girisFrame)
bgFrame.place(x=0, y=0, relwidth=1, relheight=1)

bgLabel = Label(bgFrame, image=bgPhoto)
bgLabel.pack(fill="both", expand=True)




def startGame():
    for widget in girisFrame.winfo_children():  # winfo_children() ekrandaki butun widgetleri verir.
       if widget != bgFrame:
            widget.destroy()
    root.after(3000, game) 
#    game()   #-----------------
    Label(girisFrame, text="Yüklənir...", font=("Verdana Bold", 44, "bold"), width=screenWidth, height= 2, fg="red", bg="#8dc79d").pack(pady=300)

def showStartScreen():
    for widget in girisFrame.winfo_children():
        if widget != bgFrame:
            widget.destroy()

    basLabel = Label(girisFrame, text="⛽ GAS STATION ⛽", font=("Verdana Bold", 54, "bold"), width=screenWidth, height= 2, fg="#f4f4f4", bg="#8dc79d")
    basLabel.pack(pady=(0, 150))
    Button(girisFrame, text="Start", font=("Georgia", 40, "bold"), command=startGame, bg="green", fg="#f4f4f4", width=15).pack(pady=(50, 0))
    Button(girisFrame, text="Quit", font=("Georgia", 40, "bold"), command=root.quit, bg="red", fg="#f4f4f4", width=15).pack(pady=30)


def game():
    global screenHeight, screenWidth, bgPhoto1, carImg, masin, gameFrame, pump_x, pump_y, klavis, x, y
    girisFrame.forget()

    gameFrame = Canvas(root, width=screenWidth, height=screenHeight)
    gameFrame.pack(fill="both", expand=True)

    image1 = Image.open("GasStation\\gas.jpg")
    image1 = image1.resize((screenWidth, screenHeight))
    bgPhoto1 = ImageTk.PhotoImage(image1)
    gameFrame.create_image(0, 0, image=bgPhoto1, anchor="nw")


    pump_x = 400  #}
    pump_y = 600  #}   Dayanmaq istediyimiz kordinatin x ve y kordinatlari

    root.bind("<KeyPress>", moveCar)    #keypress kodunu yazib klaviatura ile hereket etdirmeyi aktiv edirik.

    gameFrame.create_text(350, 795, text="", font=("Arial", 60), fill="red")   #Ox yaradiriq ki hara getmeli oldugumuzu bildirsin
    klavis = gameFrame.create_text(750, 100, text=" 'A' ve 'D' klavişlərindən istifadə edərək AĞ BENZİN POMPASIna yaxınlaşın", fill="red", font=("Comic Sans Ms", 30, "bold"))


    image2 = Image.open("GasStation\\car.png")
    image2 = image2.resize((500, 370))  # kiçiltmək üçün
    carImg = ImageTk.PhotoImage(image2)
    masin = gameFrame.create_image(screenWidth, screenHeight, image=carImg, anchor="se")   #canvasla yaradiriq ki backgroundu olmasin


    x, y = gameFrame.coords(masin)   #masinin kordinatlarini goturur


def moveCar(event):
    global gameFrame, masin, pump_x, pump_y, fuelSelection, bgPump
    step = 15   #masinin nece pixel-pixel hereket edeceyini yazmisiq           ------------------------------------------------
    x, y = gameFrame.coords(masin)   

    if abs(x - pump_x-170) < 50 and abs(y - pump_y-400) < 50:    #abs kodu deqiq hesablama ucun istifade olunur. 
        return
    
    if event.keysym == "a" or event.keysym == "A":    #keysym kodu klaviaturayla basdigimiz klavisin deyerini goturur.   a ve A yazmagimizin sebebi capslock aciq olduqda da islemesidir
        x -= step
    elif event.keysym == "d" or event.keysym == "D":
        x += step

    gameFrame.coords(masin, x, y)    #Son oldugu yerin kordinatlarini gotururuk

    if abs(x - pump_x-170) < 50 and abs(y - pump_y-400) < 50:    #abs kodu deqiq hesablama ucun istifade olunur. 
        root.after(1500, openFuelSelection())
        gameFrame.forget()


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
    global fuelSelection, bgPump, a92But, a95But, dieselBut, doldurBut
    fuelSelection = Canvas(root, width=screenWidth, height=screenHeight)
    fuelSelection.pack(fill=BOTH, expand=True)

    pumpImg = Image.open("GasStation\\pumps.jpg")
    pumpImg = pumpImg.resize((screenWidth, screenHeight))
    bgPump = ImageTk.PhotoImage(pumpImg)
    fuelSelection.create_image(0, 0, image=bgPump, anchor="nw")


    
    def doldur():
        global fuelTotal
        doldurBut.config(state=DISABLED)
        a92But.config(state=DISABLED)
        a95But.config(state=DISABLED)
        dieselBut.config(state=DISABLED)

        if selectedFuel is None:
            messagebox.showwarning("Warning", "Hec bir yanacaq secilmeyib")
            doldurBut.config(state=NORMAL)
            a92But.config(state=NORMAL)
            a95But.config(state=NORMAL)
            dieselBut.config(state=NORMAL)
            return
        fuelTotal = litr.get() * litrPrice  
        
        #Progress Bar
        prBar = ttk.Progressbar(fuelSelection, orient=HORIZONTAL, length=500, maximum=100)
        prBar.place(x=50, y=50)

        def updateBar(value=0):
            if value <= 100:
                prBar["value"] = value
                root.after(200, updateBar, value+5)     
            else:
                fuelSelection.create_text(1200, 70, text="Benzin doldu", font=("Georgia", 40, "bold"), fill="red")
                root.after(2000, switchToGame)

        def switchToGame():
            fuelSelection.forget()
            gameFrame.pack(fill=BOTH, expand=True)
            gameFrame.delete(klavis)
            goToMarket()
        updateBar()



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


    a92But = Button(fuelSelection, text="A92", font=("Comic Sans Ms", 25), width=5, bg="yellow", command=a92)
    a92But.place(x=320, y=730)
    a95But = Button(fuelSelection, text="A95", font=("Comic Sans Ms", 25), width=5, bg="red", fg="white", command=a95)
    a95But.place(x=730, y=730)
    dieselBut = Button(fuelSelection, text="Diesel", font=("Comic Sans Msa", 25), width=5, bg="blue", fg="white", command=diesel)
    dieselBut.place(x=1140, y=730)
    doldurBut = Button(fuelSelection, text="Doldur", font=("Arial", 30), width=13, bg="green", fg="white", command=doldur)
    doldurBut.place(x=635, y=30)


adam = None
adamId = None
adam_x, adam_y = 310, 740   #baslangic kordinatlari
symbol_x, symbol_y = 1200, 800
ox = None
yazi1 = None

def goToMarket():   
    global magazaSual, beliBut, xeyrBut

    def beli():
        global masin, masindanDus, geriGet
        root.after(1000)
        gameFrame.delete(magazaSual)
        beliBut.destroy()
        xeyrBut.destroy()
        masindanDus = Button(gameFrame, text="Maşından Düş", font=("Georgia", 30, "bold"), width=15, fg="white", bg="green", command=masindanDusmekFunc)
        masindanDus.place(x=400, y=250)

        def back():
            global geriGet, ox, yazi1
            goToMarket()
            masindanDus.destroy()
            geriGet.destroy()
            gameFrame.delete(adamId)
            gameFrame.delete(ox)
            gameFrame.delete(yazi1)
        geriGet = Button(gameFrame, text="Geri", font=("Georgia", 30, "bold"), width=15, fg="white", bg="red", command=back)
        geriGet.place(x=850, y=250)
        

    def xeyr():
        gameFrame.delete(magazaSual)
        beliBut.destroy()
        xeyrBut.destroy()

        def odemek():
            def destroyAndGo():
                odeFrame.destroy()
                animateLeft()
                
            def yeniden():
                gameFrame.forget()
                girisFrame.pack(fill=BOTH, expand=True)
                showStartScreen()

            def animateLeft(steps=105, delay=30):
                if steps > 0:
                    gameFrame.move(masin, -5, 0)
                    root.after(delay, lambda: animateLeft(steps-1, delay))
                else:
                    butRestart = Button(gameFrame, text="Yenidən oyna", fg="white", bg="green", font=("Comic Sans Ms", 45), command=yeniden)
                    butRestart.place(x=550, y=40)

            def ode2():
                odeBut2.destroy()
                Label(odeFrame, text="Ödəniş edildi", font=("Comic Sans Ms", 20), bg="#fff", fg="green").place(x=210, y=235)
                ode.destroy()
                root.after(2000, destroyAndGo)

            odeFrame = Frame(gameFrame, width=550, height=300, bg="#fff")
            odeFrame.place(x=20, y=50)
            Label(odeFrame, text=f"\n\nYanacaq üçün ödənilməli məbləğ:\n  {round(fuelTotal, 1)} Azn\n", font=("Comic Sans Ms", 23), bg="#fff").place(x=40, y=0)
            odeBut2 = Button(odeFrame, text="Ödə", font=("Georgia", 23, "bold"), width=7, fg="white", bg="green", command=ode2)
            odeBut2.place(x=200, y=230)
        ode = Button(gameFrame, text="Ödə", font=("Georgia", 30, "bold"), width=15, fg="white", bg="green", command=odemek)
        ode.place(x=600, y=250)
    
    def masindanDusmekFunc():
        global adam, adamId, adam_x, adam_y, symbol_x, symbol_y, ox, yazi1, adamFlip, firstCordinate_x, firstCordinate_y, imageFlipped
        adam_x, adam_y = 310, 740
        masindanDus.destroy()
        geriGet.place(x=600, y=250)
        ox = gameFrame.create_text(symbol_x, symbol_y, text=" ", font=("Arial", 60), fill="red")

        adamImg = Image.open("GasStation\\adam.png")
        adamImg = adamImg.resize((250,250))

        imageFlipped = ImageOps.mirror(adamImg)

        adam = ImageTk.PhotoImage(adamImg)
        adamFlip = ImageTk.PhotoImage(imageFlipped)
        adamId = gameFrame.create_image(adam_x, adam_y, image=adam)     #310-760
        
        firstCordinate_x, firstCordinate_y = 310, 760

        yazi1 = gameFrame.create_text(550, 100, text="Ox klavişlərindən istifadə edərək QAPIya yaxınlaşın", font=("Comic Sans Ms", 30), fill="red")

    def move(event):
        global adam_x, adam_y, adam, adamFlip, adamId
        step1 = 10

        if abs(adam_x - symbol_x-10) < 50 and abs(adam_y - symbol_y+100) < 50:   
            return

        if event.keysym == "Left":
            adam_x -= step1
            if adamId is not None:
                gameFrame.itemconfig(adamId, image=adamFlip)
        elif event.keysym == "Right":
            adam_x += step1
            if adamId is not None:
                gameFrame.itemconfig(adamId, image=adam)

        gameFrame.coords(adamId, adam_x, adam_y)
        
        if abs(adam_x - symbol_x-10) < 50 and abs(adam_y - symbol_y+100) < 50:   
            root.after(1000, market())
            gameFrame.forget()

    # Klavisleri aktiv edirik
    root.bind("<Left>", move)
    root.bind("<Right>", move)


    magazaSual = gameFrame.create_text(800, 150, text="Mağazaya getmək istəyirsiniz?", font=("Georgia", 40, "bold"), fill="red")
    beliBut = Button(gameFrame, text="Bəli", font=("Georgia", 30, "bold"), width=8, fg="white", bg="green", command=beli)
    beliBut.place(x=550, y=250)
    xeyrBut = Button(gameFrame, text="Xeyr", font=("Georgia", 30, "bold"), width=8, fg="white", bg="red", command=xeyr)
    xeyrBut.place(x=850, y=250)


burgerCount = IntVar(value=0)
pizzaCount = IntVar(value=0)
cheesyCount = IntVar(value=0)
hotdogCount = IntVar(value=0)

burgerPrice = 2.5
pizzaPrice = 10
cheesyPrice = 5
hotdogPrice = 2

selectedFood = []

burgerFrame = pizzaFrame = cheesyFrame = hotdogFrame = None


def market():
    global marketFrame, orderLabel, totalLabel
    global burgerFrame, pizzaFrame, cheesyFrame, hotdogFrame
    global burgerSay, pizzaSay, cheesySay, hotdogSay
    global burgerAzn, pizzaAzn, cheesyAzn, hotdogAzn

    marketFrame = Canvas(root)
    marketFrame.pack(fill=BOTH, expand=True)


    img = Image.open("GasStation\\yemekler.jpg")
    img = img.resize((screenWidth, screenHeight))
    mrktBg = ImageTk.PhotoImage(img)
    marketFrame.bg = mrktBg
    marketFrame.create_image(0, 0, image=mrktBg, anchor="nw")


    orderLabel = Label(marketFrame, text="Sifariş: ", font=("Georgia", 20))
    orderLabel.place(x=600, y=0)

    def updateOrder():
        sifaris = []
        if "Burger" in selectedFood:
            sifaris.append(f"Burger x{burgerCount.get()} = {round(burgerCount.get()*burgerPrice,1)} Azn")
        if "Pizza" in selectedFood:
            sifaris.append(f"Pizza x{pizzaCount.get()} = {round(pizzaCount.get()*pizzaPrice,1)} Azn")
        if "Cheesy" in selectedFood:
            sifaris.append(f"Cheesy x{cheesyCount.get()} = {round(cheesyCount.get()*cheesyPrice,1)} Azn")
        if "Hotdog" in selectedFood:
            sifaris.append(f"Hotdog x{hotdogCount.get()} = {round(hotdogCount.get()*hotdogPrice,1)} Azn")

        orderLabel.config(text="Sifariş:\n" + "\n".join(sifaris))


    def burger():
        global burgerFrame, burgerSay, burgerAzn

        if "Burger" not in selectedFood:
            selectedFood.append("Burger")
        updateOrder()

        if burgerFrame:  # Frame varsa sadece qabaga getir
            burgerFrame.lift()
            return

        burgerFrame = Frame(marketFrame, bg="#fff", width=250, height=100)
        burgerFrame.place(x=200, y=200)

        def updateLabels():
            burgerSay.config(text=f"{burgerCount.get()} ədəd")
            burgerAzn.config(text=f"{round(burgerCount.get()*burgerPrice,1)} Azn")
            updateOrder()

        def decrease():
            if burgerCount.get() > 1:
                burgerCount.set(burgerCount.get() - 1)
                updateLabels()
        def increase():
            burgerCount.set(burgerCount.get() + 1)
            updateLabels()

        Button(burgerFrame, text="-", font=("Arial", 25), width=2, height=2, command=decrease).place(x=0, y=0)
        burgerSay = Label(burgerFrame, text=f"{burgerCount.get()} ədəd", font=("Arial", 25), bg="#fff")
        burgerSay.place(x=55, y=0)
        burgerAzn = Label(burgerFrame, text=f"{burgerPrice} Azn", font=("Arial", 25, "bold"), bg="#fff")
        burgerAzn.place(x=55, y=50)
        Button(burgerFrame, text="+", font=("Arial", 25), width=2, height=2, command=increase).place(x=205, y=0)

    def pizza():
        global pizzaFrame, pizzaSay, pizzaAzn
        if "Pizza" not in selectedFood:
            selectedFood.append("Pizza")
        updateOrder()

        if pizzaFrame:
            pizzaFrame.lift()
            return

        pizzaFrame = Frame(marketFrame, bg="#fff", width=250, height=100)
        pizzaFrame.place(x=480, y=200)

        def updateLabels():
            pizzaSay.config(text=f"{pizzaCount.get()} ədəd")
            pizzaAzn.config(text=f"{round(pizzaCount.get()*pizzaPrice,1)} Azn")
            updateOrder()

        def decrease():
            if pizzaCount.get() > 1:
                pizzaCount.set(pizzaCount.get() - 1)
                updateLabels()
        def increase():
            pizzaCount.set(pizzaCount.get() + 1)
            updateLabels()

        Button(pizzaFrame, text="-", font=("Arial", 25), width=2, height=2, command=decrease).place(x=0, y=0)
        pizzaSay = Label(pizzaFrame, text=f"{pizzaCount.get()} ədəd", font=("Arial", 25), bg="#fff")
        pizzaSay.place(x=55, y=0)
        pizzaAzn = Label(pizzaFrame, text=f"{pizzaPrice} Azn", font=("Arial", 25, "bold"), bg="#fff")
        pizzaAzn.place(x=55, y=50)
        Button(pizzaFrame, text="+", font=("Arial", 25), width=2, height=2, command=increase).place(x=205, y=0)

    def cheesy():
        global cheesyFrame, cheesySay, cheesyAzn
        if "Cheesy" not in selectedFood:
            selectedFood.append("Cheesy")
        updateOrder()

        if cheesyFrame:
            cheesyFrame.lift()
            return

        cheesyFrame = Frame(marketFrame, bg="#fff", width=250, height=100)
        cheesyFrame.place(x=750, y=200)

        def updateLabels():
            cheesySay.config(text=f"{cheesyCount.get()} ədəd")
            cheesyAzn.config(text=f"{round(cheesyCount.get()*cheesyPrice,1)} Azn")
            updateOrder()

        def decrease():
            if cheesyCount.get() > 1:
                cheesyCount.set(cheesyCount.get() - 1)
                updateLabels()
        def increase():
            cheesyCount.set(cheesyCount.get() + 1)
            updateLabels()

        Button(cheesyFrame, text="-", font=("Arial", 25), width=2, height=2, command=decrease).place(x=0, y=0)
        cheesySay = Label(cheesyFrame, text=f"{cheesyCount.get()} ədəd", font=("Arial", 25), bg="#fff")
        cheesySay.place(x=55, y=0)
        cheesyAzn = Label(cheesyFrame, text=f"{cheesyPrice} Azn", font=("Arial", 25, "bold"), bg="#fff")
        cheesyAzn.place(x=55, y=50)
        Button(cheesyFrame, text="+", font=("Arial", 25), width=2, height=2, command=increase).place(x=205, y=0)

    def hotdog():
        global hotdogFrame, hotdogSay, hotdogAzn
        if "Hotdog" not in selectedFood:
            selectedFood.append("Hotdog")
        updateOrder()

        if hotdogFrame:
            hotdogFrame.lift()
            return

        hotdogFrame = Frame(marketFrame, bg="#fff", width=250, height=100)
        hotdogFrame.place(x=1050, y=200)

        def updateLabels():
            hotdogSay.config(text=f"{hotdogCount.get()} ədəd")
            hotdogAzn.config(text=f"{round(hotdogCount.get()*hotdogPrice,1)} Azn")
            updateOrder()

        def decrease():
            if hotdogCount.get() > 1:
                hotdogCount.set(hotdogCount.get() - 1)
                updateLabels()
        def increase():
            hotdogCount.set(hotdogCount.get() + 1)
            updateLabels()

        Button(hotdogFrame, text="-", font=("Arial", 25), width=2, height=2, command=decrease).place(x=0, y=0)
        hotdogSay = Label(hotdogFrame, text=f"{hotdogCount.get()} ədəd", font=("Arial", 25), bg="#fff")
        hotdogSay.place(x=55, y=0)
        hotdogAzn = Label(hotdogFrame, text=f"{hotdogPrice} Azn", font=("Arial", 25, "bold"), bg="#fff")
        hotdogAzn.place(x=55, y=50)
        Button(hotdogFrame, text="+", font=("Arial", 25), width=2, height=2, command=increase).place(x=205, y=0)

    def updateTotal():
        global totalFood
        totalfd = burgerCount.get()*burgerPrice + pizzaCount.get()*pizzaPrice + cheesyCount.get()*cheesyPrice + hotdogCount.get()*hotdogPrice
        totalFood = round(totalfd, 1)
        totalLabel.config(text=f"Total: {totalFood} Azn")
        if totalFood == 0:
            messagebox.showwarning("Warning", "Yemək almalısınız")
        else:
            root.after(1500, switchToGame)

    def switchToGame():
        global yazi2
        yazi2 = gameFrame.create_text(450, 100, text="Maşına qayıdın", font=("Comic Sans Ms", 40), fill="red")
        marketFrame.forget()
        gameFrame.pack(fill=BOTH, expand=True)
        gameFrame.delete(magazaSual, ox, yazi1)
        beliBut.destroy()
        xeyrBut.destroy()
        masindanDus.destroy()
        geriGet.destroy()

        def move(event):
            global adam_x, adam_y, adam, adamFlip, adamId, minButton
            step1 = 10
            

            if abs(adam_x - firstCordinate_x) < 50 and abs(adam_y - firstCordinate_y) < 50:   
                return
        
            if event.keysym == "Left":
                adam_x -= step1
                gameFrame.itemconfig(adamId, image=adamFlip)
            elif event.keysym == "Right":
                adam_x += step1
                gameFrame.itemconfig(adamId, image=adam)

            gameFrame.coords(adamId, adam_x, adam_y)

            if abs(adam_x - firstCordinate_x) < 50 and abs(adam_y - firstCordinate_y) < 50:  

                def minBut():
                    global adamId
                    if adamId:
                        gameFrame.delete(adamId)
                        adamId = None
                    minButton.destroy()
                    gameFrame.delete(yazi2)


                    def odemek():

                        def dest():
                            odeFrame.destroy()

                        def ode2():
                            odeBut2.destroy()
                            Label(odeFrame, text="Ödəniş edildi", font=("Comic Sans Ms", 20), bg="#fff", fg="green").place(x=190, y=235)
                            root.after(2000, dest)
                            root.after(1000, animateLeft)

                        def yeniden():
                            gameFrame.forget()
                            girisFrame.pack(fill=BOTH, expand=True)
                            showStartScreen()

                        def animateLeft(steps=105, delay=30):
                            if steps > 0:
                                gameFrame.move(masin, -5, 0)
                                root.after(delay, lambda: animateLeft(steps-1, delay))

                            else:
                                butRestart = Button(gameFrame, text="Yenidən oyna", fg="white", bg="green", font=("Comic Sans Ms", 45), command=yeniden)
                                butRestart.place(x=550, y=40)


                        odeFrame = Frame(gameFrame, width=550, height=300, bg="#fff")
                        odeFrame.place(x=20, y=50)
                        Label(odeFrame, text=f"Yanacaq üçün ödənilməli məbləğ: {round(fuelTotal, 1)}\n\nYemək üçün ödənilməli məbləğ: {round(totalFood, 1)}\n\nÜmumi məbləğ: {fuelTotal+totalFood}\n", font=("Comic Sans Ms", 23), bg="#fff").place(x=0, y=0)
                        odeBut2 = Button(odeFrame, text="Ödə", font=("Georgia", 23, "bold"), width=7, fg="white", bg="green", command=ode2)
                        odeBut2.place(x=180, y=230)
                        ode.destroy()
                    ode = Button(gameFrame, text="Ödə", font=("Georgia", 30, "bold"), width=15, fg="white", bg="green", command=odemek)
                    ode.place(x=600, y=250)



                minButton = Button(gameFrame, text="Min", fg="white", bg="green", font=("Georgia", 20), command=minBut)
                minButton.place(x=325, y=840)
            
        root.bind("<Left>", move)
        root.bind("<Right>", move)



    totalLabel = Label(marketFrame, text="Total: 0 Azn", font=("Arial", 20))
    totalLabel.place(x=100, y=100)


    Button(marketFrame, text="Burger", font=("Comic Sans Ms", 25), width=5, bg="yellow", command=burger).place(x=310, y=650)
    Button(marketFrame, text="Pizza", font=("Comic Sans Ms", 25), width=5, bg="yellow", command=pizza).place(x=580, y=650)
    Button(marketFrame, text="Cheesy", font=("Comic Sans Ms", 25), width=5, bg="yellow", command=cheesy).place(x=840, y=650)
    Button(marketFrame, text="Hotdog", font=("Comic Sans Ms", 25), width=5, bg="yellow", command=hotdog).place(x=1110, y=650)
    Button(marketFrame, text="Total", font=("Comic Sans Ms", 25), width=5, bg="yellow", command=updateTotal).place(x=100, y=10)
    
showStartScreen()

root.mainloop() 