import os.path
from tkinter import END, Menu, Text, BOTH, messagebox, filedialog, Tk
from tkinter.ttk import Frame
import encodeDecode


# def getTextFromClipboard():
#     txt = pyperclip.paste()
#     f = open("temp.txt", "w", encoding="utf-8")
#     print(txt)
#     f.write(txt)
#     return os.path.abspath("temp.txt")


class MainWin(Frame):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.master.title("Vigenere")
        self.pack()

        menubar = Menu(self.master)
        self.master.config(menu=menubar)

        mainMenu = Menu(menubar)
        mainMenu.add_command(label="Encode", command=self.encode)
        mainMenu.add_command(label="Decode", command=self.decode)
        menubar.add_cascade(label="File", menu=mainMenu)

        self.txt = Text(self)
        self.txt.pack(fill=BOTH, expand=1)

    def openFile(self):
        # answer = messagebox.askyesno(title="Notification", message="Take TEXT from clipboard?")
        # if answer:
        #     return getTextFromClipboard()
        ftypes = [("Text", "*.txt"), ("All Files", "*")]
        dlg = filedialog.Open(self, filetypes=ftypes)
        fl = dlg.show()
        return fl

    def encode(self):
        f = self.openFile()
        if f != '':
            path = os.path.abspath(f)
            fl = open(path, 'r')
            txt = fl.read()
            print(txt)
            key = self.txt.get("1.0", END)
            text = encodeDecode.full_encode(txt, key)
            self.txt.delete("1.0", "end")
            self.txt.insert(END, text)

    def decode(self):
        f = self.openFile()
        if f != '':
            path = os.path.abspath(f)
            fl = open(path, 'r')
            txt = fl.read()
            print(txt)
            key = self.txt.get("1.0", END)
            text = encodeDecode.full_decode(txt, key)
            self.txt.delete("1.0", "end")
            self.txt.insert(END, text)


if __name__ == "__main__":
    root = Tk()
    fr = MainWin()
    root.mainloop()

