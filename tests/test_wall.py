#!/usr/bin/env python3

import logging
import unittest

from mcthings.wall import Wall
from tests.base import TestBaseThing


class TestWall(TestBaseThing):
    """Test Wall Thing"""

    def test_build(self):
        self.server.mc.postToChat("Building a wall")

        pos = self.pos

        pos.x += 1

        wall = Wall(pos)
        wall.build()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')
    unittest.main(warnings='ignore')
