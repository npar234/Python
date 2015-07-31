#!/usr/bin/python

import model
import view

class Controller(object):
  def __init__(self):
    self.model = model.Model()
    self.view = view.View(self)
    self.view.startGui()
    self.files =[]

  def generate(self):
    dirName = self.view.generate()
    if not dirName:
      self.view.genError()
      return
    error = self.model.generate(dirName)
    self.view.genResults(dirName, error)

  def compare(self):
    directories = self.view.compare()
    if not str(directories[0]) or not str(directories[1]):
      self.view.compError()
      return
    self.model.compare(directories)
    self.view.compResults(self.model.numSame, self.model.sameFiles, \
                          self.model.files1, self.model.files2, \
                          self.model.size1, self.model.size2, \
                          self.model.tree1, self.model.tree2, \
                          self.model.pos1, self.model.pos2)

  def clear(self):
    self.model.clear()
    self.view.clear()

if __name__ == "__main__":
  controller = Controller()
