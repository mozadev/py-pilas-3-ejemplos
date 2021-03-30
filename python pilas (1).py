class Pilas(object):
    def __init__(self, limit=10):
        self.stack = []
        self.limit = limit

    # implementamos el for para imprimir los datos en el arreglo
    def __str__(self):
        return ' '.join([str(i) for i in self.stack])

    # Para insertar el metodo push en la data
    def push(self, data):
        if len(self.stack) >= self.limit:
            print('Ejemplo de pila')
        else:
            self.stack.append(data)

    # utilizamos el meteodo pop para el elemento superior
    def pop(self):
        if len(self.stack) <= 0:
            return -1
        else:
            return self.stack.pop()

    # Echamos un vistazo al elemento superior de la pila
    def peek(self):
        if len(self.stack) <= 0:
            return -1 #Nos retorna un valor menos que el valor del arreglo de la pila
        else:
            return self.stack[len(self.stack) - 1]


    # para comprobar si la pila está vacía
    def isEmpty(self):
        return self.stack == []


    # para comprobar el tamaño de la pila
    def size(self):
        return len(self.stack)


if __name__ == '__main__':
    myStack = Pilas()
    for i in range(10):
        myStack.push(i) #Aquí insertamos 10 numeros con el comando push
    print(myStack) #imprimimos el resultado
    myStack.pop()  # borramos el elemento del arreglo myStack
    print(myStack) #imprimimos el arreglo Stack sin el elemento
    print(myStack.peek()) #imprime el tamaño del arreglo actualizado
    print(myStack.isEmpty()) #retorna un valor ya sea falso o verdadero
    print(myStack.size()) #tamaño del arreglo pila Stack