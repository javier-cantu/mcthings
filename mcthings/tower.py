# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author (©): Alvaro del Castillo
import math

from mcpi.vec3 import Vec3

from .thing import Thing
from .scene import Scene


class Tower(Thing):
    top_size = 4  # square platform at the top
    height = 20  # tower height

    def build(self):
        p = self.position

        # base of the tower
        base_x = p.x + math.floor(self.top_size/2)
        base_z = p.z + math.floor(self.top_size/2)
        Scene.server.setBlocks(base_x, p.y, base_z,
                               base_x, p.y + self.height - 1, base_z,
                               self.block)

        # Top
        Scene.server.setBlocks(p.x, p.y + self.height, p.z,
                               p.x + self.top_size - 1, p.y + self.height, p.z + self.top_size - 1,
                               self.block)

        self._end_position = Vec3(p.x + self.top_size - 1,
                                  p.y + self.height,
                                  p.z + self.top_size - 1)