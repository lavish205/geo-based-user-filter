class BetweenRadiusFilterCriteria(object):
    """
    Filter criteria for distance between two radius
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
        distance = distance
        return self.radius1 <= distance <= self.radius2


class FilterCriteria(object):
    """
    Return filter criteria based on the condition
    This is required because if we have more filter criteria we can handle
    that logic here and return the required filter
    """
    @classmethod
    def get_filter(cls, radius1, radius2):
        return BetweenRadiusFilterCriteria(radius1, radius2)
