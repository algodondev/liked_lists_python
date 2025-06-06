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
            if(currentIndex == index): return current
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

    # # Insert at a specific position
    def insert_at(self, value, pos):
        aux = Node(value)
        if self.is_empty(): 
            self.first = aux
            self.last = aux
            return
        
        if pos <= 0:
            self.add_to_start(value)
            return
        
        # Si la lista no esta vacia
        n1 = self.find_at(pos - 1)
        if n1 == None:
            self.add(value)
            return
        
        n2 = n1.get_next()
        aux.set_next(n2)
        n1.set_next(aux)

    #devuelve el indice de la primera ocurrencia de un valor
    def find(self, value):
        if self.is_empty():
            return -1
        
        current = self.get_first()
        index = 0

        while True:
            if current.get_data() == value: return index
            current = current.get_next()
            index +=1 
            if current == None: break
        
        return -1
    
    #Longitud de la lista
    def length(self):
        if self.is_empty(): return 0
        counter = 0
        current = self.get_first()

        while True:
            counter+=1
            current = current.get_next()
            if current == None: break

        return counter

    #Eliminar primer dato
    def delete_first(self):
        if self.is_empty(): return
        aux = self.get_first()
        self.set_first(self.get_first().get_next()) 

        aux.set_next(None)

    #Eliminar el ultimo dato
    def delete_last(self):
        if self.is_empty(): return 
        if self.length() == 1:
            self.delete_first()
            return
        
        self.set_last(self.find_at(self.length() - 2))
        self.get_last().set_next(None)
                      
    # eliminar en una posicion especifica
    def delete_at(self, pos):
        if self.is_empty(): return
        if pos < 0 or pos >= self.length(): return
        if pos == 0:
            self.delete_first()
            return
        
        aux = self.find_at(pos)
        nxt = aux.get_next()
        prev = self.find_at(pos - 1)
        prev.set_next(nxt)
        aux.set_next(None)

    def delete_by(self, value):
        if self.is_empty(): return

        if self.find(value) >= 0:
            self.delete_at(self.find(value))
        else:
            return


    # Mostrar la lista
    def show(self):
        if(self.is_empty()):
            print("la lista esta vacia")
            return

        current = self.get_first()

        message = ''
        while True:
            message = message + f"-> {current.get_data()} "
            current = current.get_next()
            if current == None: break

        print(message)
    