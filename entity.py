from typing import Tuple
class Entity:
    """A generic object to represent any one thing"""
    def __init__(self, x: int, y: int, char: str, color: Tuple[int, int, int]):
        self.x = x
        self.y = y
        self.char = char
        self.color = color

    def move(self, dx: int, dy: int) -> None:
        """move the entity by x,y amount"""
        self.x += dx
        self.y += dy

        