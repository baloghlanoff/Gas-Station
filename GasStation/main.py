from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

root = Tk()
root.geometry("500x500")
root.title("Gas Station")
root.state("zoomed")

screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()

girisFrame = Frame(root, width=screenWidth, height=screenHeight)
girisFrame.pack(fill="both", expand=True)



image = Image.open("C:\\Users\\balog\\Desktop\\Gas Station\\GasStation\\gas-station-with-oil-pump-and-market-on-road-free-vector.jpg")
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
    Label(girisFrame, text="Oyun Başlayır...", font=("Verdana Bold", 44, "bold"), width=screenWidth, height= 2, fg="red", bg="#8dc79d").pack(pady=300)

def showStartScreen():
    for widget in girisFrame.winfo_children():
        if widget != bgFrame:
            widget.destroy()

    basLabel = Label(girisFrame, text="⛽ GAS STATION ⛽", font=("Verdana Bold", 54, "bold"), width=screenWidth, height= 2, fg="#f4f4f4", bg="#8dc79d")
    basLabel.pack(pady=(0, 150))
    Button(girisFrame, text="Start", font=("Georgia", 40, "bold"), command=startGame, bg="green", fg="#f4f4f4", width=15).pack(pady=(50, 0))
    Button(girisFrame, text="Quit", font=("Georgia", 40, "bold"), command=root.quit, bg="red", fg="#f4f4f4", width=15).pack(pady=30)


def game():
    global screenHeight, screenWidth, bgPhoto1, carImg, masin, gameFrame
    girisFrame.forget()

    gameFrame = Canvas(root, width=screenWidth, height=screenHeight)
    gameFrame.pack(fill="both", expand=True)

    image1 = Image.open("C:\\Users\\balog\\Desktop\\Gas Station\\GasStation\\A whimsical cartoon illustration of an empty gas station and a bustling market, viewed from the front, both buildings occupying the full frame. The photo should look lie this.jpg")
    image1 = image1.resize((screenWidth, screenHeight))
    bgPhoto1 = ImageTk.PhotoImage(image1)
    gameFrame.create_image(0, 0, image=bgPhoto1, anchor="nw")

    image2 = Image.open("C:\\Users\\balog\\Desktop\\Gas Station\\GasStation\\Adobe Express - file (16).png")
    image2 = image2.resize((500, 370))
    carImg = ImageTk.PhotoImage(image2)
    masin = gameFrame.create_image(screenWidth, screenHeight, image=carImg, anchor="se")

    root.bind("<KeyPress>", moveCar)

def moveCar(event):
    global gameFrame, masin
    step = 10
    x, y = gameFrame.coords(masin)
    if event.keysym == "a":
        gameFrame.coords(masin, x - step, y)
    elif event.keysym == "d":
        gameFrame.coords(masin, x + step, y)




showStartScreen()

root.mainloop() 