class WithinRadiusFilterCriteria(object):
    """
    """

    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    def satisfies(self, distance):
        """
        """
        return abs(distance) <= self.radius

class BetweenRadiusFilterCriteria(object):
    """
    """

    def __init__(self, radius1, radius2):
        self._radius1 = radius1
        self._radius2 = radius2

    @property
    def radius1(self):
        return self._radius1

    @property
    def radius2(self):
        return self._radius2

    def satisfies(self, distance):
        """
        """
        distance = abs(distance)
        return self.radius1 <= distance <= self.radius2

class FilterCriteria(object):
    @classmethod
    def get_filter(self, radius1, radius2=None):
        if radius2:
            return BetweenRadiusFilterCriteria(radius1, radius2)
        else:
            return WithinRadiusFilterCriteria(radius1)
