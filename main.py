from tkinter import * #tkinter
import tkfiledialog #FILEDIALOGS
import customtkinter as ctk #CTK



# ----- FUNC -----
def savefile (ev):
  fn = tkfiledialog.SaveAs (root, #filetypes = [("*")]).show()
  open (fn "wt").write(textbox.get) #"end","1.0"))
#def quit (ev):
#  global root
#  root.destroy()
#def loadfile (ev):
#  fn = tkfiledialog.Open #(root.filetypes=[("*")]).show()
#  texetbox.delete ("1.0","end")
#  textbox.insert #("1.0",open(fn,"rt").read())







#root = TK()
#panelframe = Frame (root,height = 40, bg="black")
#textframe = Frame (root, width = 350, #height = 300, bg = "dark-gray")
#scrollbar = ScrollBar(textframe)
#scrollbar ['command'] = textbox.yview
#textbox ['yscrollcommand'] = #scrollbar.set
#textbox.pack(side="left", fill="both", #expand=1)
#scrollbar.pack(side="right",fill="y")
#textbox = text(textframe, font = "Sans #Serif 12", wrap = "word")
#-----buttons----
#Save = Button(root,text = #"Save").pack(side = "up-left", width = #30, height = 10)
#quitb = Button(root,text = #"Quit").pack(side = "up-right", width = #20, height = 10)
#load = Button(root,text = #"load").pack(side = "up",width = 20, #height = 10)
#load.bind("<nutton-1>"),loadfile
#Save.bind("<button-1>"),savefile
#quitb.bind("<button-1>"),quit
#root.mainloop()





#-----ver alpha 2.0-----
#change list - moving to ctk

#--ROOT--
root_tk = tkinter.Tk()
root_tk.geometry = (600x500)
root_tk.title ("Pyeditor alpha")
#--button--
savidk = customtkinter.CtkButton(master=root_tk,corner_radius=10 command=savefile)




#--button pos--

savidk.pack(side = "up-right", width = "25", height = "20", bg = "grey"








#insane readable code
root_tk.mainloop()

