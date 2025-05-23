class Node:
    def __init__(self, data):
        self._data = data     
        self._next = None      

    # Getter y setter del valor del nodo
    def get_data(self):
        return self._data
    def set_data(self, value):
        self._data = value

    # Getter y seter del valor del nodo
    def get_next(self):
        return self._next
    def set_next(self, value):
        self._next = value
