import base

from absl import app
import matplotlib.pyplot as plt


def main(argv):
  # plt.ion()
  map = base.make_map(100, 100, 0)
  for i in range(20):
    room = base.make_random_room(map)
    x, y = base.place_room_randomly(map, room)
  plt.imshow(map.grid)
  plt.show()


if __name__ == "__main__":
  app.run(main)
