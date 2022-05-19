#modules
import json
import tkinter as tk
from PIL import ImageTk, Image





def jsonReader():

    with open("characterData.json", "r") as readFile:
        return json.load(readFile)





def main():

    characterData = jsonReader()



    window = tk.Toplevel()
    window.title("Worker Display")
    window.resizable(False,True)
    window.geometry("650x850")
    window.configure(bg="white")



    #all the code for the full window scrollbar
    mainFrame = tk.Frame(window)
    mainFrame.pack(fill=tk.BOTH, expand=1)

    mainCanvas = tk.Canvas(mainFrame, bg=window["bg"])
    mainCanvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

    scrollbar = tk.Scrollbar(mainFrame, orient="vertical", command=mainCanvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    mainCanvas.configure(yscrollcommand=scrollbar.set)
    mainCanvas.bind("<Configure>", lambda e: mainCanvas.configure(scrollregion=mainCanvas.bbox("all")))

    displayFrame = tk.Frame(window)
    displayFrame.rowconfigure([r for r in range(len(characterData))], minsize=175)
    displayFrame.columnconfigure(0, minsize=630)

    mainCanvas.create_window((0,0), window=displayFrame, anchor="nw")


    #creates the elements to display all the character information
    for r in range(len(characterData)):

        #creates an element where the character info will be placed into
        characterFrame = tk.Frame(displayFrame, borderwidth=1, relief="sunken", bg=window["bg"])
        characterFrame.columnconfigure(0, minsize=450)
        characterFrame.grid(row=r, column=0, sticky="nesw")


        nameLbl = tk.Label(characterFrame, text=f"{characterData[r]['firstName']} {characterData[r]['lastName']}", font=("Arial",20), bg=window["bg"])
        nameLbl.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        ageJobLbl = tk.Label(characterFrame, text=f"{characterData[r]['age']}  -  {characterData[r]['occupation']}", font=("Arial",15), bg=window["bg"])
        ageJobLbl.grid(row=1, column=0, padx=10, sticky="w")

        locationLbl = tk.Label(characterFrame, text=f"Based in {characterData[r]['location']}", font=("Arial",13), bg=window["bg"])
        locationLbl.grid(row=2, column=0, padx=10, pady=30, sticky="w")


        characterImage = Image.open(characterData[r]["imgAdr"]).resize((150,150))
        characterImage = ImageTk.PhotoImage(characterImage)
        imgLbl = tk.Label(characterFrame, image=characterImage, width=150, height=150)
        #i found this line of code on stack overflow, it stops tkinter from displaying only the last image in the loop
        imgLbl.photo = characterImage
        imgLbl.grid(row=0, column=1, rowspan=3, sticky="ew")
    


    window.mainloop()





if __name__ == "__main__":

    main()