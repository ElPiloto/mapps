from typing import Optional

import numpy as np


EMPTY_FILL = 0
ROOM_FILL = 1


class Rect():
  x: float
  y: float
  width: float
  height: float


  def __init__(self, x: float, y: float, width: int, height: int,
               fill_value: Optional[int] = None):
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    if fill_value is None:
      self._grid = None
    else:
      self._grid = np.full(shape=(width, height),
                           fill_value=fill_value,
                           dtype=np.int32)

  @property
  def grid(self):
    if self._grid is None:
      self._grid = np.full(shape=(self.width, self.height),
                           fill_value=EMPTY_FILL,
                           dtype=np.int32)
    return self._grid

  @property
  def top(self):
    return self.y + self.height

  @property
  def bottom(self):
    return self.y

  @property
  def left(self):
    return self.x

  @property
  def right(self):
    return self.x + self.width


class Room(Rect):

  def __init__(self, width: int, height: int):
    super().__init__(-1000., -1000., width, height, ROOM_FILL)


def make_map(width: int, height: int, fill_value: int = 0):
  """Makes an empty map."""
  return Rect(0, 0, width, height, fill_value)


def make_random_room(map: Rect,
                     min_width: int = 5,
                     min_height: int = 5,
                     max_width_percent: float = 0.1,
                     max_height_percent: float = 0.2):
  """."""
  map_width, map_height = map.grid.shape
  max_width = int(max_width_percent * map_width)
  max_height = int(max_height_percent * map_height)
  width = np.random.randint(min_width, max_width)
  height = np.random.randint(min_height, max_height)
  return Room(width, height)


def can_fit(x, y, map, room):
  """Checks if room can fit into location in map."""
  if x < 0 or y < 0:
    return False

  if room.width + x > map.width:
    return False

  if room.height + y > map.height:
    return False
  
  return True


def is_empty(x, y, map, room, include_border = False):
  if not can_fit(x, y, map, room):
    return False

  if include_border:
    x_min = int(max(x-1, 0))
    x_max = int(min(map.width, x+room.width+1))
    y_min = int(max(y-1, 0))
    y_max = int(min(map.height, y+room.height+1))
  else:
    x_min = int(x)
    x_max = int(x + room.width)
    y_min = int(y)
    y_max = int(y + room.height)
  return np.all(map.grid[x_min:x_max, y_min:y_max] == EMPTY_FILL)


def place_room(x: int, y: int, map: Rect, room: Room):
  """."""
  x_coords = slice(x, x+room.width)
  y_coords = slice(y, y+room.height)
  map.grid[x_coords, y_coords] = ROOM_FILL


def place_room_randomly(map: Rect, room: Room):
  max_x = map.width - room.width
  max_y = map.height - room.height
  succeeded = False
  failures = 0
  while not succeeded:
    x = np.random.randint(0, max_x)
    y = np.random.randint(0, max_y)
    if is_empty(x, y, map, room, include_border=True):
      place_room(x, y, map, room)
      succeeded = True
    else:
      failures += 1
    if failures > 10:
      print(f'Number of failures: {failures}')
  return x, y



# def place_rectangle(map: Rect, rect: Rect):


