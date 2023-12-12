class Node:
    def __init__(self, data):
        self.data = data
        self.next = None



class Linked_list:
    def __init__(self):
        self.header = None
        self._size = 0

    def append(self, elem):
        # Adicionar elementos na lista
        if self.header == None:
            self.header = Node(elem)
        else:
            proximo = self.header
            while (proximo.next):
                proximo = proximo.next
            proximo.next = Node(elem)
        self._size += 1

    def _getnode(self, index):
        proximo = self.header
        for i in range(index):
            if proximo:
                proximo = proximo.next
            else:
                raise IndexError("Valor não encontrado!")
        return proximo

    def __getitem__(self, index):
        # Ver um indice pela posição da lista
        proximo = self._getnode(index)
        if proximo:
            return proximo.data
        else:
            raise IndexError("Valor não encontrado!")

    def __setitem__(self, index, elem):
        # Substituir elementos na lista!
        proximo = self._getnode(index)
        if proximo:
            proximo.data = elem
        else:
            raise IndexError("Valor não encontrado!")

    def insert(self, index, elem):
        # Inserir elemento na lista
        node = Node(elem)
        if self.header == None:
            self.header = elem
        elif index == 0:
            node.next = self.header
            self.header = node
        else:
            proximo = self._getnode(index - 1)
            node.next = proximo.next
            proximo.next = node
        self._size += 1

    def remove(self, elem):
        # Remover indice na lista
        self._size -= 1
        if self.header == None:
            raise ValueError("A lista se encontra vazia!")
        elif self.header.data == elem:
            self.header = self.header.next
            return True
        else:
            ancessor = self.header
            proximo = self.header.next
            while (proximo):
                if proximo.data == elem:
                    ancessor.next = proximo.next
                    proximo.next = None
                ancessor = proximo
                proximo = proximo.next
            return True

    def __len__(self):
        # retorna tamanho na lista
        return self._size

    def see_list(self):
        # Ver lista inteira
        r = ""
        proximo = self.header
        while (proximo):
            r = r + str(proximo.data) + " -> "
            proximo = proximo.next
        return r


# Testando lista
lista = Linked_list()
lista.append(22)
lista.append(33)
lista.insert(0, 1)
lista.remove(22)
lista.__setitem__(1, 2)
#Ver lista conpleta
print(lista.see_list())
#ver tamanho da lista
print(len(lista))
# ver o elemento pela posição
print(lista.__getitem__(1))



# Testes Unitarios.

lista = Linked_list()

def test_ny_fuction_append():
    lista.append(22)
    assert len(lista) == 1

def test_my_fuction_getitem():
    assert lista.__getitem__(0) == 22

def test_my_fuction_setitem():
    lista.__setitem__(0, 10)
    assert lista.__getitem__(0) == 10

def test_my_fuction_insert():
    lista.insert(1, 20)
    assert lista.__getitem__(1) == 20

def test_my_fuction_remove():
    lista.remove(20)
    lista.remove(10)
    assert len(lista) == 0

def test_my_fuction_see_list():
    lista.append(190)
    lista.append(30)
    lista.append(50)
    lista.append(25)
    print(lista.see_list())
    assert len(lista) == 4

