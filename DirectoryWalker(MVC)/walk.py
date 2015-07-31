import sys, os
import stack

class Walk(object):
  def __init__(self, dir):
    self.startDir = dir
    self.files = []
    self.dirs = []
    self.walk()

  def printFiles(self):
    print "The", len(self.files), "are", self.files

  def walk(self):
    stk = stack.stack()
    stk.push(self.startDir)
    while not stk.empty():
      directory = stk.top()
      stk.pop()
      files = os.listdir(directory)
      for thisFile in files:
        name = os.path.join(directory, thisFile)
        if os.path.isdir(name):
          stk.push( name )
        else:
          self.files.append( thisFile )
          self.dirs.append( name )

if __name__ == "__main__":
  if len(sys.argv) != 2:
    print "usage:", sys.argv[0], "<dir>"
    sys.exit()
  walker = Walk(sys.argv[1])
  walker.printFiles()
