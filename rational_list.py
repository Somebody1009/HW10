class RationalList:
    def __init__(self):
        self.items = []

    def add(self, rational):
        self.items.append(rational)

    def __iter__(self):
        self.items.sort(key=lambda r: (-r.value.denominator, -r.value.numerator))
        return iter(self.items)
