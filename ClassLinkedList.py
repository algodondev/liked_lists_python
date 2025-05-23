from ClassNode import Node

class LinkedList:
    def __init__(self):
        self._first = None
        self._last = None  

    # First node getter y setter
    def get_first(self):
        return self._first
    def set_first(self, node):
        self._first = node

    # Last node getter y setter
    def get_last(self):
        return self._last
    def set_last(self, node):
        self._last = node

    # Retorna falso si el primer nodo no existe
    def is_empty(self):
        return self._first == None
    
    # Encontrar 
    def find_at(self, index):
        currentIndex = 0
        current = self.get_first()

        while(current != None):
            if(currentIndex == index): return current.get_data()
            currentIndex += 1
            current = current.get_next()
        
        return None

    # Agregar un nodo al final de la lista
    def add(self, value):
        aux = Node(value)

        # Si la lista esta vacia
        if(self.is_empty()):
            self.set_first(aux)
            self.set_last(aux)
            return

        # si no
        self.get_last().set_next(aux)
        self.set_last(aux)

    # Agregar un nodo al final de la lista
    def add_to_start(self, value):
        aux = Node(value)

        # Si la lista esta vacia
        if self.is_empty():
            self.set_first(aux)
            self.set_last(aux)
            return

        # si no
        aux.set_next(self.get_first())
        self.set_first(aux)

    # Insert at a specific position
    def insert_at(self, value, pos):
        aux = Node(value)
        # Si la lista esta vacia
        if self.is_empty():
            self.set_first(aux)
            self.set_last(aux)
            return
        
        if pos <= 0:
            self.add_to_start(value)
            return
        
        n1 = self.find_at(pos -1)
        if n1 == None:
            self.add(value)
            return
        
        n2 = n1.get_next()
        aux.get_next() = n2
        n1.get_next() = aux

    # Mostrar la lista
    def show(self):
        if(self.is_empty()):
            print("la lista esta vacia")
            return

        current = self.get_first()

        while True:
            print(f"{current.get_data()}")
            current = current.get_next()
            if current == None: break
    