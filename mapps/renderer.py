import matplotlib.pyplot as plt
import numpy as np


def grid_renderer(grid: np.ndarray):
  """Renders a grid."""
  plt.imshow(grid)
