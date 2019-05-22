import threading


class Singleton(object):
    _instance = None

    def __new__(self):
        self.lock.acquire()
        if not self._instance:
            self._instance = super(Singleton, self).__new__(self)
        return self._instance

        self.lock.release()

    def Accion(accion):
        for vuelta in range(5):
            print("Accion: " + accion + "\n")

#mientras A este en funcionamiento,  B no puede acceder al metodo y asi por el mumero de peticiones
A = threading.Thread(target=Singleton.Accion("camina"))
B = threading.Thread(target=Singleton.Accion("salta"))
C = threading.Thread(target=Singleton.Accion("descansa"))
A.start()
B.start()
C.start()