class Rectangle:

  def __init__(self, width, height):
    self.width = width
    self.height = height

  def set_width(self, value):
    self.width = value

  def set_height(self, value):    
    self.height = value

  def get_area(self):
    area = self.width * self.height 
    return area

  def get_perimeter(self):
    perimeter = 2 * self.width + 2 * self.height 
    return perimeter

  def get_diagonal(self):
    diagonal = (self.width ** 2 + self.height ** 2) ** .5
    return diagonal

  def get_picture(self):
    if self.width > 50 or self.height > 50:
      return "Too big for picture."
    shape = []
    for row in range(self.height):
      shape.append("*" * self.width + "\n")
    return "".join(shape) 

  def get_amount_inside(self, shape):
    amountInside=int(self.get_area()/shape.get_area())
    if amountInside < 1:
        return 0
    return amountInside  

  def __str__(self):
    return f"Rectangle(width={self.width}, height={self.height})"

class Square(Rectangle):

  def __init__(self, side_length):
    super().__init__(side_length, side_length)

  def set_side(self, side):
    super().set_height(side)
    super().set_width(side)

  def set_width(self, side):
    super().set_height(side)
    super().set_width(side)

  def set_height(self, side):
    super().set_height(side)
    super().set_width(side)

  def __str__(self):    
    return f"Square(side={self.width})"