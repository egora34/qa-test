class Locator:
    def __init__(self, _using, _selector, _label=None):
        self._using = _using
        self._selector = _selector
        self._label = _label

    @property
    def using(self):
        return self._using

    @property
    def selector(self):
        return self._selector
