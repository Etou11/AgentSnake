class GameField:
    def __init__(self, status, position):
        self.status = status
        self.position = position

    def __str__(self):
        return str(self.value)
