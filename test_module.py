import unittest
import shape_calculator


class UnitTests(unittest.TestCase):

  def setUp(self):
    self.rect = shape_calculator.Rectangle(4, 8)
    self.sq = shape_calculator.Square(4)

  def test_subclass(self):
    actual = issubclass(shape_calculator.Square, shape_calculator.Rectangle)
    expected = True
    self.assertEqual(
      actual, expected,
      'Expected Square class to be a subclass of the Rectangle class.')

  def test_distinct_classes(self):
    actual = shape_calculator.Square is not shape_calculator.Rectangle
    expected = True
    self.assertEqual(
      actual, expected,
      'Expected Square class to be a distinct class from the Rectangle class.')

  def test_square_is_square_and_rectangle(self):
    actual = isinstance(self.sq, shape_calculator.Square) and isinstance(
      self.sq, shape_calculator.Rectangle)
    expected = True
    self.assertEqual(
      actual, expected,
      'Expected square object to be an instance of the Square class and the Rectangle class.'
    )

  def test_rectangle_string(self):
    actual = str(self.rect)
    expected = "Rectangle(width=4, height=8)"
    self.assertEqual(
      actual, expected,
      'Expected string representation of rectangle to be "Rectangle(width=4, height=8)"'
    )

  def test_square_string(self):
    actual = str(self.sq)
    expected = "Square(side=4)"
    self.assertEqual(
      actual, expected,
      'Expected string representation of square to be "Square(side=4)"')

  def test_area(self):
    actual = self.rect.get_area()
    expected = 32
    self.assertEqual(actual, expected, 'Expected area of rectangle to be 32')
    actual = self.sq.get_area()
    expected = 16
    self.assertEqual(actual, expected, 'Expected area of square to be 16')

  def test_perimeter(self):
    actual = self.rect.get_perimeter()
    expected = 24
    self.assertEqual(actual, expected,
                     'Expected perimeter of rectangle to be 24')
    actual = self.sq.get_perimeter()
    expected = 16
    self.assertEqual(actual, expected, 'Expected perimeter of square to be 16')

  def test_diagonal(self):
    actual = self.rect.get_diagonal()
    expected = 8.94427190999916
    self.assertEqual(actual, expected,
                     'Expected diagonal of rectangle to be 8.94427190999916')
    actual = self.sq.get_diagonal()
    expected = 5.656854249492381
    self.assertEqual(actual, expected,
                     'Expected diagonal of square to be 5.656854249492381')

  def test_set_atributes(self):
    self.rect.set_width(5)
    self.rect.set_height(10)
    self.sq.set_side(4)
    actual = str(self.rect)
    expected = "Rectangle(width=5, height=10)"
    self.assertEqual(
      actual, expected,
      'Expected string representation of rectangle after setting new values to be "Rectangle(width=5, height=10)"'
    )
    actual = str(self.sq)
    expected = "Square(side=4)"
    self.assertEqual(
      actual, expected,
      'Expected string representation of square after setting new values to be "Square(side=4)"'
    )
    self.sq.set_width(5)
    actual = str(self.sq)
    expected = "Square(side=5)"
    self.assertEqual(
      actual, expected,
      'Expected string representation of square after setting width to be "Square(side=5)"'
    )

  def test_rectangle_picture(self):
    self.rect.set_width(5)
    self.rect.set_height(10)
    actual = self.rect.get_picture()
    expected = "*****\n*****\n*****\n*****\n*****\n*****\n*****\n*****\n*****\n*****\n"
    self.assertEqual(actual, expected,
                     'Expected rectangle picture to be different.')

  def test_squaree_picture(self):
    self.sq.set_side(4)
    actual = self.sq.get_picture()
    expected = "****\n****\n****\n****\n"
    self.assertEqual(actual, expected,
                     'Expected square picture to be different.')

  def test_big_picture(self):
    self.rect.set_width(51)
    self.rect.set_height(5)
    actual = self.rect.get_picture()
    expected = "Too big for picture."
    self.assertEqual(actual, expected,
                     'Expected message: "Too big for picture."')

  def test_get_amount_inside(self):
    self.rect.set_height(4)
    self.rect.set_width(8)
    actual = self.rect.get_amount_inside(self.sq)
    expected = 2
    self.assertEqual(actual, expected,
                     'Expected `get_amount_inside` to return 2.')

  def test_get_amount_inside_two_rectangles(self):
    rect2 = shape_calculator.Rectangle(8, 8)
    actual = rect2.get_amount_inside(self.rect)
    expected = 2
    self.assertEqual(actual, expected,
                     'Expected `get_amount_inside` to return 2.')

  def test_get_amount_inside_none(self):
    rect2 = shape_calculator.Rectangle(2, 3)
    actual = rect2.get_amount_inside(self.rect)
    expected = 0
    self.assertEqual(actual, expected,
                     'Expected `get_amount_inside` to return 0.')


if __name__ == "__main__":
  unittest.main()
