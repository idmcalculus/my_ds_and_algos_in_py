class Node:
  def __init__(self, value):
    self.value = value
    self.next_node = None
    
  def get_value(self):
    return self.value
  
  def get_next_node(self):
    return self.next_node
  
  def set_next_node(self, next_node):
    self.next_node = next_node

class LinkedList:
  def __init__(self, head_node=None):
    self.head_node = head_node
  
  def insert(self, new_node):
    current_node = self.head_node

    if not current_node:
      self.head_node = new_node

    while(current_node):
      next_node = current_node.get_next_node()
      if not next_node:
        current_node.set_next_node(new_node)
      current_node = next_node

  def __iter__(self):
    current_node = self.head_node
    while(current_node):
      yield current_node.get_value()
      current_node = current_node.get_next_node()

  def insert_beginning(self, new_value):
    new_node = Node(new_value)
    new_node.set_next_node(self.head_node)
    self.head_node = new_node
    
  def stringify_list(self):
    string_list = ""
    current_node = self.get_head_node()
    while current_node:
      next_node = current_node.get_next_node()
      if current_node.get_value() != None:
        arrow = "" if next_node.get_value() is None else " -> "
        string_list += str(current_node.get_value()) + arrow
      current_node = next_node
    return "No nodes in Linked list" if len(string_list) == 0 else string_list
  
  def remove_node(self, value_to_remove):
    current_node = self.get_head_node()
    if current_node.get_value() == value_to_remove:
      self.head_node = current_node.get_next_node()
    else:
      while current_node:
        next_node = current_node.get_next_node()
        if next_node != None and next_node.get_value() == value_to_remove:
          current_node.set_next_node(next_node.get_next_node())
          current_node = None
        elif next_node == None:
          break
        else:
          current_node = next_node

  def remove_all_nodes(self, value_to_remove):
    head_node = self.get_head_node()
    current_node = self.get_head_node()
    prev_node = self.get_head_node()
    while current_node:
      if current_node.get_value() == value_to_remove:
        if head_node == current_node:
          self.head_node = current_node.get_next_node()
          current_node = current_node.get_next_node()
          prev_node = current_node
        else:
          if current_node == prev_node:
            self.head_node = current_node.get_next_node()
            current_node = current_node.get_next_node()
            prev_node = current_node
          else:
            prev_node.set_next_node(current_node.get_next_node())
            current_node = current_node.get_next_node()
      else:
        next_node = current_node.get_next_node()
        if next_node != None and next_node.get_value() == value_to_remove:
          current_node.set_next_node(next_node.get_next_node())
          prev_node = current_node
          current_node = next_node.get_next_node()
        elif next_node == None:
          break
        else:
          prev_node = current_node
          current_node = next_node

  def count_nodes(self):
    count = 0
    current_node = self.get_head_node()
    while current_node != None:
      count += 1
      current_node = current_node.get_next_node()
    
    return count
  
  def remove_all(self, value_to_remove):
    count = self.count_nodes()
    for _ in range(0, count):
      self.remove_node(value_to_remove)
      
  def swap_nodes(self, val1, val2):
    print(f'Swapping {val1} with {val2}')

    node1_prev = None
    node2_prev = None
    node1 = self.head_node
    node2 = self.head_node

    if val1 == val2:
      print("Elements are the same - no swap needed")
      return

    while node1 is not None:
      if node1.get_value() == val1:
        break
      node1_prev = node1
      node1 = node1.get_next_node()

    while node2 is not None:
      if node2.get_value() == val2:
        break
      node2_prev = node2
      node2 = node2.get_next_node()

    if (node1 is None or node2 is None):
      print("Swap not possible - one or more element is not in the list")
      return

    if node1_prev is None:
      self.head_node = node2
    else:
      node1_prev.set_next_node(node2)

    if node2_prev is None:
      self.head_node = node1
    else:
      node2_prev.set_next_node(node1)

    temp = node1.get_next_node()
    node1.set_next_node(node2.get_next_node())
    node2.set_next_node(temp)
  
  def nth_last_node(self, n):
    current = None
    tail_seeker = self.head_node
    count = 1
    while tail_seeker:
      tail_seeker = tail_seeker.get_next_node()
      count += 1
      if count >= n + 1:
        if current == None:
          current = self.head_node
        else:
          current = current.get_next_node()
    return current
    
  def find_middle(self):
    fast = self.head_node
    slow = self.head_node
    while fast:
      fast = fast.get_next_node()
      if fast:
        fast = fast.get_next_node()
        slow = slow.get_next_node()
    return slow
    
  def find_middle_alt(self):
    count = 0
    fast = self.head_node
    slow = self.head_node
    while fast:
      fast = fast.get_next_node()
      if count % 2 != 0:
        slow = slow.get_next_node()
      count += 1
    return slow