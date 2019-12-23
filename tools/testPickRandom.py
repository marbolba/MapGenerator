import unittest
from tools.pickRandom import PickRandom


class TestPickRandom(unittest.TestCase):
    def testRand2(self):
        samples = 1000
        zeros = ones = 0
        for i in range(0, samples):
            if PickRandom.rand2(0, 1) == 0:
                zeros += 1
            else:
                ones += 1
        self.assertEqual(zeros + ones, samples)
        self.assertGreater(zeros, samples / 2 - 0.1 * samples)
        self.assertGreater(ones, samples / 2 - 0.1 * samples)

    def testRand3(self):
        samples = 1000
        zeros = ones = twos = 0
        for i in range(0, samples):
            result = PickRandom.rand3(0, 1, 2)
            if result == 0:
                zeros += 1
            elif result == 1:
                ones += 1
            else:
                twos += 1
        self.assertEqual(zeros + ones + twos, samples)
        self.assertGreater(zeros, samples / 3 - 0.1 * samples)
        self.assertGreater(ones, samples / 3 - 0.1 * samples)
        self.assertGreater(twos, samples / 3 - 0.1 * samples)

    def testRand4(self):
        samples = 1000
        zeros = ones = twos = tres = 0
        for i in range(0, samples):
            result = PickRandom.rand4(0, 1, 2, 3)
            if result == 0:
                zeros += 1
            elif result == 1:
                ones += 1
            elif result == 2:
                twos += 1
            else:
                tres += 1
        self.assertEqual(zeros + ones + twos + tres, samples)
        self.assertGreater(zeros, samples / 3 - 0.1 * samples)
        self.assertGreater(ones, samples / 3 - 0.1 * samples)
        self.assertGreater(twos, samples / 3 - 0.1 * samples)
        self.assertGreater(tres, samples / 3 - 0.1 * samples)


if __name__ == '__main__':
    unittest.main()
