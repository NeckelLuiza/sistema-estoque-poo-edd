class Fila:

    def __init__(self):
        self._items = []
        print("Fila criada")

    def enqueue(self, item): 
        if item == None:
            raise ValueError("Item nao pode ser None")
        
        if item in self._items:
            raise ValueError("Item ja esta na fila")

        self._items.insert(0, item)

    def dequeue(self): 
        if self.is_empty():
            raise IndexError("Fila está vazia")
        
        return self._items.pop()

    def front(self): 
        if self.is_empty():
            raise IndexError("Fila está vazia")
        
        return self._items[-1]
    
    def is_empty(self):
        return len(self._items) == 0
    
    def size(self): 
        return len(self._items)
    
    def __str__(self):
        return str(self._items)
    
    def get_items(self):
        return self._items