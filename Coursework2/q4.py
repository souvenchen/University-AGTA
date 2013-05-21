class Node(object):

  def __init__(self, label):
    self.label = label
    self.outs = set()

  def add_edge(self, other_node):
    self.outs.add(other_node)

  def __eq__(self, other):
    return self.label == other.label

  def __ne__(self, other):
    return not self.__eq__(other)

  def __hash__(self):
    return hash(self.label)


def dfs(current_node, target_node, path_so_far, current_depth, max_depth):
  path_copy = list(path_so_far)
  path_copy.append(current_node.label)

  if current_node == target_node:
    print ' -> '.join(path_copy)
    return

  if current_depth == max_depth:
    return

  for child_node in current_node.outs:
    dfs(child_node, target_node, path_copy, current_depth + 1, max_depth)


def find_paths(from_node, to_node, max_depth):
  dfs(from_node, to_node, [], 0, max_depth)


def main():
  s1 = Node("s1")
  t1 = Node("t1")

  s2 = Node("s2")
  t2 = Node("t2")

  s3 = Node("s3")
  t3 = Node("t3")

  b1 = Node("b1")
  b2 = Node("b2")
  b3 = Node("b3")
  b4 = Node("b4")
  b5 = Node("b5")
  b6 = Node("b6")
  b7 = Node("b7")
  b8 = Node("b8")

  s1.add_edge(t3)
  s1.add_edge(b4)
  s1.add_edge(b5)

  t1.add_edge(s3)
  t1.add_edge(b2)

  s2.add_edge(b6)
  s2.add_edge(b8)

  t2.add_edge(s3)
  t2.add_edge(b1)

  s3.add_edge(t1)
  s3.add_edge(b3)
  s3.add_edge(b4)

  t3.add_edge(s1)
  t3.add_edge(s2)
  t3.add_edge(b1)

  b1.add_edge(b2)
  b1.add_edge(b5)
  
  b2.add_edge(b3)
  b2.add_edge(b4)
  b2.add_edge(b6)
  b2.add_edge(b8)

  b3.add_edge(s3)
  b3.add_edge(t1)
  b3.add_edge(b2)

  b4.add_edge(t2)
  b4.add_edge(b7)

  b5.add_edge(b4)

  b6.add_edge(b3)
  b6.add_edge(s2)

  b7.add_edge(b3)

  b8.add_edge(t3)
  b8.add_edge(b1)

  print "Paths from s1 to t1:"
  find_paths(s1, t1, 6)
  print

  print "Paths from s2 to t2:"
  find_paths(s2, t2, 6)
  print

  print "Paths from s1 to t1:"
  find_paths(s3, t3, 6)
  print


if __name__ == "__main__":
  main()