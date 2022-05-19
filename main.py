import characterRandomiser as characters
import gui
import tkinter as tk





def main():

    window = tk.Tk()
    window.title("Main Menu")
    window.resizable(False,False)
    window.geometry("300x300")
    window.configure(bg="white")



    mainFrame = tk.Frame(bg=window["bg"])
    mainFrame.rowconfigure([0,1], minsize=100)
    mainFrame.columnconfigure(0, minsize=200)
    mainFrame.grid(row=0, column=0, padx=50, pady=50)

    guiBtn = tk.Button(mainFrame, height=3, text="Open GUI", font=("Arial",12), fg="white", bg="grey", activebackground="lightgrey", command=gui.main)
    guiBtn.grid(row=0, column=0, sticky="ew")

    reloadBtn = tk.Button(mainFrame, height=3, text="Create New Characters", font=("Arial",12), fg="white", bg="grey", activebackground="lightgrey", command=characters.main)
    reloadBtn.grid(row=1, column=0, sticky="ew")



    window.mainloop()





if __name__ == "__main__":
    main()