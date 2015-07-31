import Tkinter as tk
import tkFileDialog as tkfd
import sys


class View(object):
  def __init__(self, controller):
    self.directories = ["",""]

    self.controller = controller
    root = tk.Tk()
    root.title("Project 2")

    scrollbar = tk.Scrollbar(root)
    scrollbar.grid(row=0, column=20, sticky="nsw")
    hscrollbar = tk.Scrollbar(root, orient='horizontal')
    hscrollbar.grid(row=1, column=0, columnspan=19, sticky="ew")

    self.dir1 = ""
    self.dir2 = ""

    self.mylist = tk.Listbox(root, yscrollcommand = scrollbar.set)
    self.mylist.config(bg='white', bd=5)
    self.mylist.config(width=75, height=40)
    self.mylist.bind('<Double-1>', self.display)
    self.mylist.grid(row=0, column=0, sticky="nesw", columnspan=19)

    scrollbar.config(command=self.mylist.yview)
    hscrollbar.config(command=self.mylist.xview)

    generate = tk.Button(root, text="Generate", width=10)
    generate.configure(command=self.controller.generate, bg='lime green')
    generate.grid(row=2, column=2)
    compare = tk.Button(root, text="Compare", width=10)
    compare.configure(command=self.controller.compare, bg='lime green')
    compare.grid(row=2, column=4)
    clear = tk.Button(root, text="Clear", width=10)
    clear.configure(command=self.controller.clear, bg='yellow')
    clear.grid(row=2, column=16)
    quit = tk.Button(root, text="Quit", width=10)
    quit.configure(command=sys.exit, bg='red')
    quit.grid(row=2, column=18)

  # uses tkFileDialog to ask user for a directory name
  def generate(self):
    dirName = tkfd.askdirectory(title="Directory Name")
    return dirName

  # prints out whether a directory was created or not
  def genResults(self, dirName, error):
    if error==1:
      self.mylist.insert(tk.END, "Failed to create directory")
      return
    self.mylist.insert(tk.END, "Directory created successfully")

  # genError and compError print an error message if the user does not
  # choose a directory
  def genError(self):
    self.mylist.insert(tk.END, "Please choose a directory to generate")

  # uses tkFileDialog to get names of 2 directories
  def compare(self):
    self.directories[0] = tkfd.askdirectory(title="Choose Directory #1")
    if not self.directories[0]:
      return self.directories
    self.directories[1] = tkfd.askdirectory(title="Choose Directory #2")
    return self.directories

  # The following inserts all the details figured out by the model
  def compResults(self, numSame, sameFiles, files1, files2, size1, size2, \
                  tree1, tree2, pos1, pos2):
    self.mylist.insert(tk.END, "Aliases")
    self.mylist.insert(tk.END, "(This Program refers to directory names")
    self.mylist.insert(tk.END, "by using the following aliases)")
    self.mylist.insert(tk.END, "DIR#1 = "+ str(self.directories[0]))
    self.mylist.insert(tk.END, "DIR#2 = "+ str(self.directories[1]))
    self.mylist.insert(tk.END, "")
    self.mylist.insert(tk.END, "There are "+ str(size1) +" files in DIR#1")
    self.mylist.insert(tk.END, "There are "+ str(size2) +" files in DIR#2")
    self.mylist.insert(tk.END, "")
    self.mylist.insert(tk.END, str(numSame) +" similar file(s) exist between" \
                        +" DIR#1 and DIR#2")
    self.mylist.insert(tk.END, "")
    self.mylist.insert(tk.END, "These file(s) are:")
    for i in range(0,len(sameFiles)):
      self.mylist.insert(tk.END, sameFiles[i])
    self.mylist.insert(tk.END, "")
    self.mylist.insert(tk.END, "")
    self.mylist.insert(tk.END, "The paths for the matching files are:")
    self.mylist.insert(tk.END, "")
    self.mylist.insert(tk.END, "In DIR#1")
    for i in range (0, len(pos1)):
      self.mylist.insert(tk.END, str(files1[pos1[i]]) +"  -  "+ \
                        str(tree1[pos1[i]]))
    self.mylist.insert(tk.END, "")
    self.mylist.insert(tk.END, "In DIR#2")
    for j in range (0, len(pos2)):
      self.mylist.insert(tk.END, str(files2[pos2[j]]) +"  -  "+ \
                        str(tree2[pos2[j]]))
    self.mylist.insert(tk.END, "")
    self.mylist.insert(tk.END, "")
    self.mylist.insert(tk.END, "")
    self.mylist.insert(tk.END, "The following is a list of all files in DIR#1 and DIR#2")
    self.mylist.insert(tk.END, "")
    self.mylist.insert(tk.END, "DIR#1")
    for i in range(0, size1):
      self.mylist.insert(tk.END, files1[i])
    self.mylist.insert(tk.END, "")
    self.mylist.insert(tk.END, "")
    self.mylist.insert(tk.END, "DIR#2")
    for j in range(0, size2):
      self.mylist.insert(tk.END, files2[j])
    self.mylist.insert(tk.END, "")

  def compError(self):
    self.mylist.insert(tk.END, "Please choose 2 directories for comparison")

  # displays a selected line from listbox onto terminal
  def display(self, event):
    index = self.mylist.curselection()
    label = self.mylist.get(index)
    print "You selected:", label

  # clears the listbox
  def clear(self):
    self.mylist.delete(0, tk.END)
    print "Model and View cleared"

  def startGui(self):
    tk.mainloop()  
