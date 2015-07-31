import generate, walk

class Model(object):
  def __init__(self):
    # list of files in each of the directories
    self.files1=[]
    self.files2=[]

    # number of files in each of the directories
    self.size1 = 0
    self.size2 = 0

    # list of the paths of all files in both directories
    self.paths1=[]
    self.paths2=[]

    # list of position of similar files in each directory
    self.pos1 = []
    self.pos2 = []

    # number of same files in both directories
    self.numSame = 0

    # list of the names of same files in both directories
    self.sameFiles = []

  # generates specified directory
  # returns an error if directory already exists
  def generate(self, dirName):
    generator = generate.Generator(dirName)
    generator.generate()
    return generator.error

  # compares the two directories using walk.py and holds the
  # gathered information in global variables
  def compare(self, directories):
    walker1 = walk.Walk(directories[0])
    walker2 = walk.Walk(directories[1])
    self.files1 = walker1.files
    self.files2 = walker2.files
    self.size1 = len(self.files1)
    self.size2 = len(self.files2)
    self.tree1 = walker1.dirs
    self.tree2 = walker2.dirs
    for i in range(0, self.size1):
      for j in range(0, self.size2):
        if self.files1[i] == self.files2[j]:
          self.sameFiles.append(self.files2[j])
          self.numSame += 1
          self.pos1.append(i)
          self.pos2.append(j)

  # clears (resets) all the variables in the model
  def clear(self):
    self.files1=[]
    self.files2=[]
    self.size1 = 0
    self.size2 = 0
    self.paths1=[]
    self.paths2=[]
    self.pos1 = []
    self.pos2 = []
    self.numSame = 0
    self.sameFiles = []
