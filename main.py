from tkinter import *
import tkfiledialog
def savefile (ev):
  fn = tkfiledialog.SaveAs (root, filetypes = [("*")]).show()
  open (fn "wt").write(textbox.get) "end","1.0"))
def quit (ev):
  global root
  root.destroy()
def loadfile (ev):
  fn = tkfiledialog.Open (root.filetypes=[("*")]).show()
root = TK()
panelframe = Frame (root,height = 40, bg="black")
textframe = Frame (root, width = 350, height = 300, bg = "dark-gray")
scrollbar = ScrollBar(textframe)
scrollbar ['command'] = textbox.yview
textbox ['yscrollcommand'] = scrollbar.set
textbox.pack(side="left", fill="both", expand=1)
scrollbar.pack(side="right",fill="y")
textbox = text(textframe, font = "Sans Serif 12", wrap = "word")
Save = Button(root,text = "Save").pack(side = "up-left", width = 30, height = 10)
quitb = Button(root,text = "Quit").pack(side = "up-right", width 20, height = 10)
Save.bind("<button-1>")savefile
quitb.bind("<button-1>")quit
root.mainloop()
