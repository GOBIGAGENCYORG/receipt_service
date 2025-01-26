# TODO: Refactor

class ReceiptCounter:
    counter: int = 0

    def __init__(self):
        self._counter: int = self._get_saved_counter()

    def _get_saved_counter(self) -> int:
        saved_counter: int = ReceiptCounter.counter  # TODO: Load saved counter
        if not saved_counter:
            return 0
        return saved_counter

    def _save_counter(self):
        global counter
        ReceiptCounter.counter = self._counter  # TODO: Save counter
        pass

    def _update_counter(self):
        self._counter += 1
        self._save_counter()

    def get(self, with_update: bool = True):
        if with_update:
            self._update_counter()
        return self._counter
