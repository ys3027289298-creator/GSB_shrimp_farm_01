import unittest

import core


class TestCore(unittest.TestCase):
    def test_00(self):
        state = core.new_game()
        core.bug_12(state)
        self.assertEqual(state["src"], 5)

    def test_01(self):
        state = core.new_game()
        state["slots"] = 2
        self.assertFalse(core.bug_19(state))

    def test_02(self):
        state = core.new_game()
        self.assertFalse(core.bug_26(state))

    def test_03(self):
        state = core.new_game()
        state["queue"] = [1, 2]
        self.assertEqual(core.bug_3(state), 1)

    def test_04(self):
        state = core.new_game()
        self.assertFalse(core.bug_10(state))

    def test_05(self):
        state = core.new_game()
        self.assertFalse(core.bug_17(state))

    def test_06(self):
        state = core.new_game()
        self.assertEqual(core.bug_24(state), 2)

    def test_07(self):
        state = core.new_game()
        state["items"] = ["a", "b"]
        self.assertFalse(core.bug_1(state))

    def test_08(self):
        state = core.new_game()
        state["count"] = 5
        core.bug_8(state)
        self.assertEqual(state["count"], 0)

    def test_09(self):
        state = core.new_game()
        state["closed"] = True
        self.assertFalse(core.bug_15(state))


if __name__ == "__main__":
    unittest.main()
