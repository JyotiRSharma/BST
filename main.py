class Node:
  def __init__(self, data):
    self.left = None
    self.right = None
    self.data = data

class BST:
  def __init__(self):
    self.root = None
    
  def insert(self, data):
    new_node = Node(data)

    if self.root == None:
      self.root = new_node
      # print(f"root inserted {new_node.data}")
    else:
      current_node = self.root
      while True:
        # print(f"current_node value {current_node.data}")
        if new_node.data < current_node.data:
          #left          
          if current_node.left == None:
            # print(f"left - inserting {new_node.data}")
            current_node.left = new_node
            return
          else:
            current_node = current_node.left
            # print(f"left - traversing {current_node.data}")
        else:
          #right
          if current_node.right == None:
            # print(f"right - inserting {new_node.data}")
            current_node.right = new_node
            return
          else:
            current_node = current_node.right
            # print(f"right - traversing {current_node.data}")

  def lookup(self, data):
    curr_node = self.root
    if curr_node == None:
      return False
    while curr_node:
      if data < curr_node.data:
        curr_node = curr_node.left
      elif data > curr_node.data:
        curr_node = curr_node.right
      elif curr_node.data == data:
        return True
    return False
    
  def print_tree(self):
      if self.root != None:
          self.print_nodes(self.root)
          
  def print_nodes(self, curr_node):
      if curr_node != None:
          self.print_nodes(curr_node.left)
          print(str(curr_node.data))
          self.print_nodes(curr_node.right)

myBST = BST()
myBST.insert(9)
myBST.insert(4)
myBST.insert(6)
myBST.insert(20)
myBST.insert(170)
myBST.insert(15)
myBST.insert(1)
print(myBST.lookup(15))
myBST.print_tree()