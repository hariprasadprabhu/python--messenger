from Tkinter import *
from ttk import *
import socket
import thread
import webbrowser
import tkMessageBox




class ChatClient(Frame):
  
  def __init__(self, root):
    Frame.__init__(self, root)
    self.root = root
    self.UserInterface()
    self.serverSoc = None
    self.serverStatus = 0
    self.buffsize = 1024
    self.allClients = {}
    self.counter = 0

    menu=Menu(root)
    self.root.config(menu=menu)
    filemenu=Menu(menu)
    menu.add_cascade(label="File",menu=filemenu)
    filemenu.add_command(label="new",command=self.callback)
    filemenu.add_command(label="Open",command=self.callback)
    filemenu.add_command(label="Open Recent Chats",command=self.callback)
    filemenu.add_command(label="Pair with bluetooth devices.",command=self.callback)
    filemenu.add_command(label="Change app theme",command=self.callback)
    filemenu.add_command(label="On/Off End to end encryption",command=self.callback)
    filemenu.add_separator()
    filemenu.add_command(label="Exit",command=self.exit)

    toolsmenu=Menu(menu)
    menu.add_cascade(label="Tools",menu=toolsmenu)
    toolsmenu.add_command(label="Developer Mod",command=self.Developer)

    helpmenu=Menu(menu)
    menu.add_cascade(label="Help",menu=helpmenu)
    helpmenu.add_command(label="TypeWriter_Today Help",command=self.Thelp)
    helpmenu.add_command(label="Check for updates...",command=self.updates)
    helpmenu.add_separator()
    helpmenu.add_command(label="About TypeWriter_Today",command=self.about)


    accountmenu=Menu(menu)
    menu.add_cascade(label="Account",menu=accountmenu)
    accountmenu.add_command(label="Login..",command=self.login)
    accountmenu.add_command(label="TypeWriter_Today Webside",command=self.webpage)


  def callback(self):
  	tkMessageBox.showerror("Error!!","This feature is not available for this version for TypeWriter_Today")
    


  def login(self):
    top=Toplevel()
    top.title("Login...")
    msg = Message(top,text="Welcome to the login window")
    msg.pack()
    link = Button(top, text="Click to Login!", cursor="hand2")
    link.pack()
    link.bind("<Button-1>",self.linkadd)

  def linkadd(self,open_new):
    webbrowser.open_new(r"C:\Users\ARPITH_KUMAR\Desktop\TypeWriter_Today\login\index.html")
  
  
  def webpage(self):
    top=Toplevel()
    top.title("On your way to our website...")
    msg = Message(top,text="Visit our website to discover a whole new world !")
    msg.pack()
    link = Button(top, text="Open WebPage", cursor="hand2")
    link.pack()
    link.bind("<Button-1>",self.webadd) 

  def webadd(self,open_new):
    webbrowser.open_new(r"C:\Users\ARPITH_KUMAR\Desktop\TypeWriter_Today\web_page\Typewriter_today web page\one-page.html")
    




  def Thelp(self):
    top = Toplevel()
    top.title("HELP")
    msg = Message(top, text="WELCOME TO TypeWriter_Today HELP\n\n\nYou can find TypeWriter_Today documentation on TypeWriter_Today wiki website||https://wiki.TypeWriter_Today.org/.\n\nIf you are a newcomer to TypeWriter_Today Messenger, please read the Introduction to TypeWriter_Today Messenger||https://www.TypeWriter_Today.com/Introduction.html.\n\nYou will find some information on how to use the Messenger in the-->How to play files with TypeWriter_Today document.||https://www.TypeWriter_Today.com/dock.html\n\nIf you are unsure about terminology, please consult the-->knowledge base.||https://www.TypeWriter_Today.com/base.html\n\nBefore asking any question, please refer yourself to the--> FAQ.||https://www.TypeWriter_Today.com/FAQ's.htm\n\nCONTRIBUTION TO THE PROJECT:\n\n\nYou can help the TypeWriter_Today project giving some of your time to help the community, to design skins, to translate the documentation, to test and to code. You can also give funds and material to help us. And of course, you can promote TypeWriter_Today Messenger.")
    msg.pack()
    button = Button(top, text="Done!", command=top.destroy)
    button.pack()
  
  def Developer(self):
    tkMessageBox.askquestion(R"Don't Lie >_<     :/      =_=     ^_~","Special Permmision required to access Developer Mod...\n\nAre you a Registered Developer??")
    tkMessageBox.showerror("Error!!","No Developer Permisions were found for your account...")
    tkMessageBox.showwarning("Alert !!","Login as Developer first\n@ https://www.TypeWriter_Today.com/Developer_Patch/Login.html")
    

  def updates(self):
    top = Toplevel(width=15000, relief=GROOVE)
    top.title("TypeWriter_Today Update Widget")
    msg = Message(top, text="YOU ARE CURENTLY USING THE LATEST OF Typewriter_Today(v 1.0.0) \n :) :0 :| :/ :> :< :+) :*) :)")
    msg.pack()
    button = Button(top, text="Ok", command=top.destroy)
    button.pack()

  def about(self):
    top = Toplevel()
    top.title("TypeWriter_Today v_1.0.0")
    msg = Message(top, text="Typewriter_Today is a open source Messenger encoded and developed by Arpith_kumar\n \nCopyright (C) 1989, 1991 Free Software Foundation, Inc.,51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USAEveryone is permitted to copy and distribute verbatim copiesof this license document, but changing it is not allowed.\n CONTACT US:\n arpithmangalore07@gmail.com \n https://t.me/Arpith_Kumar\n \n FOLLOW US:\n Facebook||https://www.facebook.com/arpith.kumar.7549\n Instagram||https://www.instagram.com/arpith.kumar /\n \n  © 2016-2017 TypeWriter_Today Inc.All rights reserved.")
    msg.pack()
    button = Button(top, text="Dismiss", command=top.destroy)
    button.pack()

  def exit(self):
    if tkMessageBox.askyesno("Exiting Typewriter....","Are you sure you are leaving us alone ??   :(  "):
        self.root.destroy()



  def UserInterface(self):
    self.root.title("TypeWriter_Today    version 1.0.0")
    ScreenSizeX = self.root.winfo_screenwidth()
    ScreenSizeY = self.root.winfo_screenheight()
    self.FrameSizeX  = 700
    self.FrameSizeY  = 660
    FramePosX   = (ScreenSizeX - self.FrameSizeX)/2
    FramePosY   = (ScreenSizeY - self.FrameSizeY)/2
    self.root.geometry("%sx%s+%s+%s" % (self.FrameSizeX,self.FrameSizeY,FramePosX,FramePosY))
    self.root.resizable(width=False, height=False)

    padX = 10
    padY = 10
    parentFrame = Frame(self.root )
    parentFrame.grid(padx=padX, pady=padY, stick=E+W+N+S)

    ipGroup = Frame(parentFrame)
    serverLabel = Label(ipGroup, text="	Your info: ")
    self.nameVar = StringVar()
    self.serverIPVar = StringVar()
    self.serverIPVar.set("127.0.0.1")
    serverIPField = Entry(ipGroup, width=15, textvariable=self.serverIPVar)
    self.serverPortVar = StringVar()
    self.serverPortVar.set("8090")
    serverPortField = Entry(ipGroup, width=5, textvariable=self.serverPortVar)
    serverSetButton = Button(ipGroup, text="Set", width=10, command=self.handleSetServer)
    addClientLabel = Label(ipGroup, text="Add New Chat: ")
    self.clientIPVar = StringVar()
    self.clientIPVar.set("127.0.0.1")
    clientIPField = Entry(ipGroup, width=15, textvariable=self.clientIPVar)
    self.clientPortVar = StringVar()
    self.clientPortVar.set("8091")
    clientPortField = Entry(ipGroup, width=5, textvariable=self.clientPortVar)
    clientSetButton = Button(ipGroup, text="Add", width=10, command=self.handleAddClient)

    serverLabel.grid(row=0, column=0)
    serverIPField.grid(row=0, column=2)
    serverPortField.grid(row=0, column=3)
    serverSetButton.grid(row=0, column=4, padx=5)
    addClientLabel.grid(row=0, column=5)
    clientIPField.grid(row=0, column=6)
    clientPortField.grid(row=0, column=7)
    clientSetButton.grid(row=0, column=8, padx=5)
    
    readChatGroup = Frame(parentFrame)
    self.receivedChats = Text(readChatGroup, bg="#cb95e2", width=60, height=30, state=DISABLED)
    self.friends = Listbox(readChatGroup, bg="#cb95e2", width=30, height=30)
    self.receivedChats.grid(row=0, column=0, sticky=W+N+S, padx = (0,10))
    self.friends.grid(row=0, column=1, sticky=E+N+S)

    writeChatGroup = Frame(parentFrame)
    self.chatVar = StringVar()
    self.chatField = Entry(writeChatGroup, width=80, textvariable=self.chatVar)
    sendChatButton = Button(writeChatGroup, text="Send", width=10, command=self.handleSendChat)
    self.chatField.grid(row=0, column=0, sticky=W)
    sendChatButton.grid(row=0, column=1, padx=5)

    self.statusLabel = Label(parentFrame)
    
    ipGroup.grid(row=9, column=0)
    readChatGroup.grid(row=1, column=0)
    writeChatGroup.grid(row=2, column=0, pady=10)
    self.statusLabel.grid(row=0, column=0)
 

  def handleSetServer(self):
    if self.serverSoc != None:
        self.serverSoc.close()
        self.serverSoc = None
        self.serverStatus = 0
    serveraddr = (self.serverIPVar.get().replace(' ',''), int(self.serverPortVar.get().replace(' ','')))
    try:
        self.serverSoc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serverSoc.bind(serveraddr)
        self.serverSoc.listen(5)
        self.setStatus("Your app is all ready to go!\nWant to stay alone do you??\nThen add a friend already!!\n Your connection info--->%s:%s" % serveraddr)
        thread.start_new_thread(self.listenClients,())
        self.serverStatus = 1
        self.name = self.nameVar.get().replace(' ','')
        if self.name == '':
            self.name = "%s:%s" % serveraddr
    except:
        self.setStatus("Error setting up server")
    
  def listenClients(self):
    while 1:
      clientsoc, clientaddr = self.serverSoc.accept()
      self.setStatus("Yippee! friend connected.\nRise and chat sleepy head!!\nYour friend's connectio info---> %s:%s\n\nOh! by the way you can add upto 5 friends at a time    Enjoy :)" % clientaddr)
      self.addClient(clientsoc, clientaddr)
      thread.start_new_thread(self.handleClientMessages, (clientsoc, clientaddr))
    self.serverSoc.close()
  
  def handleAddClient(self):
    if self.serverStatus == 0:
      self.setStatus("Set server address first")
      return
    clientaddr = (self.clientIPVar.get().replace(' ',''), int(self.clientPortVar.get().replace(' ','')))
    try:
        clientsoc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clientsoc.connect(clientaddr)
        self.setStatus("Connected to client on %s:%s" % clientaddr)
        self.addClient(clientsoc, clientaddr)
        thread.start_new_thread(self.handleClientMessages, (clientsoc, clientaddr))
    except:
        self.setStatus("Error connecting to client")

  def handleClientMessages(self, clientsoc, clientaddr):
    while 1:
      try:
        data = clientsoc.recv(self.buffsize)
        if not data:
            break
        self.addChat("%s:%s" % clientaddr, data)
      except:
          break
    self.removeClient(clientsoc, clientaddr)
    clientsoc.close()
    self.setStatus("Client disconnected from %s:%s" % clientaddr)
  
  def handleSendChat(self):
    if self.serverStatus == 0:
      self.setStatus("Set server address first")
      return
    msg = self.chatVar.get().replace(' ','')
    if msg == '':
        return
    self.addChat("me", msg)
    for client in self.allClients.keys():
      client.send(msg)
  
  def addChat(self, client, msg):
    self.receivedChats.config(state=NORMAL)
    self.receivedChats.insert("end",client+": "+msg+"\n")
    self.receivedChats.config(state=DISABLED)
  
  def addClient(self, clientsoc, clientaddr):
    self.allClients[clientsoc]=self.counter
    self.counter += 1
    self.friends.insert(self.counter,"%s:%s" % clientaddr)
  
  def removeClient(self, clientsoc, clientaddr):
      print self.allClients
      self.friends.delete(self.allClients[clientsoc])
      del self.allClients[clientsoc]
      print self.allClients
  
  def setStatus(self, msg):
    self.statusLabel.config(text=msg)
    print msg

     
def main(): 
  root = Tk()
  app = ChatClient(root)
  root.protocol("WM_WINDOW",exit)
  root.mainloop()  

if __name__ == '__main__':
  main()  
