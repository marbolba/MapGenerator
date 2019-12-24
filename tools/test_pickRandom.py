import unittest
from tools.pickRandom import PickRandom

def test_rand2():
    samples = 1000
    zeros = ones = 0
    for i in range(0, samples):
        if PickRandom.rand2(0, 1) == 0:
            zeros += 1
        else:
            ones += 1
    assert zeros + ones == samples
    assert zeros > samples / 2 - 0.1 * samples
    assert ones > samples / 2 - 0.1 * samples


def test_rand3():
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
    assert zeros + ones + twos  == samples
    assert zeros > samples / 3 - 0.1 * samples
    assert ones > samples / 3 - 0.1 * samples
    assert twos > samples / 3 - 0.1 * samples


def test_rand4():
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
    assert zeros + ones + twos + tres == samples
    assert zeros > samples / 4 - 0.1 * samples
    assert ones > samples / 4 - 0.1 * samples
    assert twos > samples / 4 - 0.1 * samples
    assert tres > samples / 4 - 0.1 * samples


if __name__ == '__main__':
    unittest.main()
