import random


class PickRandom:
    @staticmethod
    def rand(v1=None, v2=None, v3=None, v4=None):
        if v4 is not None:
            return PickRandom.rand4(v1, v2, v3, v4)
        elif v3 is not None:
            return PickRandom.rand3(v1, v2, v3)
        elif v2 is not None:
            return PickRandom.rand2(v1, v2)
        elif v1 is not None:
            return v1

    @staticmethod
    def rand2(v1, v2):
        return v1 if random.random() <= 0.5 else v2

    @staticmethod
    def rand3(v1, v2, v3):
        rnd = random.random()
        return v1 if rnd <= 0.33 else v2 if rnd <= 0.66 else v3

    @staticmethod
    def rand4(v1, v2, v3, v4):
        rnd = random.random()
        return v1 if rnd <= 0.25 else v2 if rnd <= 0.5 else v3 if rnd <= 0.75 else v4
