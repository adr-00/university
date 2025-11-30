import string

class Correccion:
    def __init__(self, W = set()):
        self._w = W
        if len(self._w) == 0:
            self._w = {'gato', 'coche', 'perro', 'auto', 'banco', 'silla'}

    def check(self, s):
        correcciones = []
        if s in self._w:
            correcciones.append(s)
        else:
            correcciones = self._permuta(s)
            correcciones += self._inserta(s)
            correcciones += self._sustitucion(s)
            correcciones += self._borrado(s)
        conjunto = set(correcciones)
        return list(conjunto)
    def _permuta(self, s):
        correcciones = []
        for palabra in self._w:
            for i in range(len(palabra)-1):
                p_iter = list(palabra)
                p_iter[i], p_iter[i+1] = p_iter[i+1], p_iter[i]
                if s == "".join(p_iter):
                    correcciones.append(palabra)
        return correcciones

    def _inserta(self, s):
        correcciones = []
        for palabra in self._w:
            for i in range(len(palabra)+1):
                for letra in list(string.ascii_lowercase):
                    p_iter = list(palabra)
                    p_iter.insert(i, letra)
                    if s == "".join(p_iter):
                        correcciones.append(palabra)
        return correcciones

    def _borrado(self, s):
        correcciones = []
        for palabra in self._w:
            for i in range(len(palabra)):
                p_iter = list(palabra)
                p_iter.pop(i)
                if s == "".join(p_iter):
                    correcciones.append(palabra)
        return correcciones

    def _sustitucion(self, s):
        correcciones = []
        for palabra in self._w:
            for i in range(len(palabra)):
                for letra in list(string.ascii_lowercase):
                    p_iter = list(palabra)
                    p_iter[i] = letra
                    if s == "".join(p_iter):
                        correcciones.append(palabra)
        return correcciones


def pruebas():
    corrector = Correccion({'gato', 'coche', 'perro', 'auto', 'banco', 'silla'})
    
    print("Pruebas de palabras correctas:")
    palabras_correctas = ['agto', 'cohe', 'perrox', 'auuto', 'bamco', 'sillla']
    for palabra in palabras_correctas:
        print(f"Comprobando '{palabra}': {corrector.check(palabra)}")
pruebas()

                