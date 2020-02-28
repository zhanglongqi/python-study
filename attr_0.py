#!/usr/bin/env python3
from dataclasses import dataclass

import attr

j = [1, 2, 3]


@attr.s
class Point(object):
    x = attr.ib()
    y = attr.ib()
    a = 3

    @classmethod
    def from_row(cls, row):
        return cls(row.x, row.y)


@dataclass
class ROW:
    x: str
    y: str


row1 = ROW("hello", "world")
p1 = Point.from_row(row1)
print(row1)
print(p1)
