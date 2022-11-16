#!/usr/bin/python3

"""Defines The Rectangle Model
Its base off of Base class"""

from models.base import Base


class Rectangle(Base):
    """Rectangle Model has four variables
    width, height x and y"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes instance variables"""
        super().__init__(id)
        self.validate_size("width", width)
        self.validate_size("height", height)
        self.validate_size("x", x, 0)
        self.validate_size("y", y, 0)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """defines getter for __width"""
        return self.__width

    @property
    def height(self):
        """defines getter for __height"""
        return self.__height

    @property
    def x(self):
        """defines getter for __x"""
        return self.__x

    @property
    def y(self):
        """defines getter for __y"""
        return self.__y

    @width.setter
    def width(self, val):
        """defines setter for __width"""
        self.validate_size("width", val)
        self.__width = val

    @height.setter
    def height(self, val):
        """defines setter for __height"""
        self.validate_size("height", val)
        self.__height = val

    @x.setter
    def x(self, val):
        """defines setter for __x"""
        self.validate_size("x", val, 0)
        self.__x = val

    @y.setter
    def y(self, val):
        """defines setter for __y"""
        self.validate_size("y", val, 0)
        self.__y = val

    def area(self):
        """get the area of the rectangle"""
        return self.width * self.height

    def display(self):
        """Prints self using #"""
        y_offset = "\n" * self.y
        x_offset = " " * self.x
        print(y_offset, end='')
        for i in range(self.height):
            print(x_offset, "#" * self.width, sep='')

    def __str__(self):
        """print a formatted form of self"""
        name = type(self).__name__
        rep = f"[{name}] ({self.id}) {self.x}/{self.y}"\
            f" - {self.width}/{self.height}"
        return rep

    def update(self, *args, **kwargs):
        """resets the attributes of self"""

        L = len(args)
        if L > 0:
            self.id = args[0]
        if L > 1:
            self.width = args[1]
        if L > 2:
            self.height = args[2]
        if L > 3:
            self.x = args[3]
        if L > 4:
            self.y = args[4]

        if L:
            return

        valids = ("id", "height", "width", "x", "y")
        for key, val in kwargs.items():
            if key in valids:
                self.__setattr__(key, val)

    def to_dictionary(self):
        """Converts self to a dictionary"""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x, "y": self.y
        }

    def to_csv_str(self):
        """returns a csv string of self"""
        fmt = "{},{},{},{},{}"
        return fmt.format(*(
            self.id,
            self.width, self.height,
            self.x, self.y
        ))
