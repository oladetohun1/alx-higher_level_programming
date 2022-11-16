#!/usr/bin/python3

"""Defines a square model from rectangle
The rectangle class is also the super class
of square"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square model: rectangle equal sides"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes instance variables"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Defines getter for size"""
        return self.width

    @size.setter
    def size(self, val):
        """Defines setter for size"""
        self.width = val
        self.height = val

    def __str__(self):
        """Overrides str behaviour"""
        tmp = super().__str__()
        return tmp[:tmp.rfind('/')]

    def update(self, *args, **kwargs):
        """resets the attributes of self"""

        L = len(args)
        if L:
            if L > 1:
                args = list(args)
                args.insert(1, args[1])
            return super().update(*args)
        if kwargs != {}:
            if 'size' in kwargs:
                _w = kwargs['size']
                del kwargs['size']
                kwargs['width'] = _w
                kwargs['height'] = _w
            super().update(**kwargs)

    def to_dictionary(self):
        """Converts self to a dictionary"""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x, "y": self.y
        }

    def to_csv_str(self):
        """returns a csv string of self"""
        fmt = "{},{},{},{}"
        return fmt.format(*(
            self.id, self.size,
            self.x, self.y
        ))
