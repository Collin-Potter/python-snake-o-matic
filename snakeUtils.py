class SnakeUtils:

  def __init__(self, data):
        self.data = data

  def determine_state(self):
    print("Head..")
    print("X: {}".format(self.data.you.head.x))
    print("Y: {}".format(self.data.you.head.y))
    print("Body piece positions..")
    for i in range(1, len(self.data.you.body)):
      print("{} - X: {}".format(i, self.data.you.body[i].x))
      print("{} - Y: {}".format(i, self.data.you.body[i].y))
