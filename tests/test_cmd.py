"""
Test Command.
"""

import unittest


class CommandUnitTest(unittest.TestCase):
    def test_unsupported_command(self):
        pass

    # MOVE/LEFT/RIGHT/REPORT commands, no argument required,
    def test_command_extra_arguments(self):
        pass

    # PLACE commands, 3 arguments required.
    # Format: PLACE x, y, facing. Spaces between arguments can be handled flexibly
    # The values of x and y are in the range of [0,4]
    # the value of facing can be "NORTH", "SOUTH", "EAST", "WEST", Case insensitive
    def test_command_place_arguments(self):
        pass

    # all commands are case insensitive
    def test_command_lowercase_command(self):
        pass

    # discard all commands in the sequence until a valid PLACE command has been executed.
    def test_command_order(self):
        pass



if __name__ == '__main__':
    unittest.main()
