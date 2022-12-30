from absl.testing import absltest

import base


class RectTest(absltest.TestCase):

  def setUp(self):
    self.r1 = base.Rect(x=0., y=0., width=10, height=20)
    self.r2 = base.Rect(x=8., y=9., width=10, height=20)

  def test_corners(self):
    self.assertEqual(self.r1.left, 0.)
    self.assertEqual(self.r1.bottom, 0.)
    self.assertEqual(self.r1.right, 10.)
    self.assertEqual(self.r1.top, 20.)

    self.assertEqual(self.r2.left, 8.)
    self.assertEqual(self.r2.bottom, 9.)
    self.assertEqual(self.r2.right, 18.)
    self.assertEqual(self.r2.top, 29.)

class MapTest(absltest.TestCase):

  def setUp(self):
    self.big_empty_map = base.make_map(100, 100, base.EMPTY_FILL)
    self.big_full_map = base.make_map(100, 100, base.ROOM_FILL)
    self.big_half_full_map = base.make_map(100, 100, base.EMPTY_FILL)
    self.big_half_full_map.grid[:50, :50] = base.ROOM_FILL
    self.small_room = base.Room(5, 5)

  def test_is_empty(self):
    self.assertTrue(base.is_empty(0., 0., self.big_empty_map, self.small_room))

    self.assertFalse(base.is_empty(0., 0., self.big_full_map, self.small_room))

    # Can't place on full half.
    self.assertFalse(base.is_empty(49., 49., self.big_half_full_map,
                                   self.small_room),
                     'Cannot place on full half.')

    self.assertTrue(base.is_empty(50., 50., self.big_half_full_map,
                                  self.small_room),
                    'Can place on empty half near border.')

    self.assertFalse(base.is_empty(50., 50., self.big_half_full_map,
                                  self.small_room, include_border=True),
                     'Cannot place at border of empty half if include_border.')

    # Can't place off edge of map.
    self.assertFalse(base.is_empty(99., 99., self.big_half_full_map,
                                  self.small_room))

    # Can place right up to edge of map.
    self.assertTrue(base.is_empty(94., 94., self.big_half_full_map,
                                  self.small_room))

if __name__ == '__main__':
  absltest.main()
