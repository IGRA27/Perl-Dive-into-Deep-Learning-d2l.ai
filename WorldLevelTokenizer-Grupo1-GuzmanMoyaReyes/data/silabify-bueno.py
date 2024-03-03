import re
import pyphen

class TextoLimpio:
    @staticmethod
    def limpiar(texto, idioma):
        texto_limpio = re.sub(r'[.,;]', '', texto.lower())
        texto_limpio = re.sub(r'[^a-záéíóúüñàèéêëîïôöûüçæœ]', ' ', texto_limpio)
        return texto_limpio

class Silabeador:
    def __init__(self, idioma):
        self.idioma = idioma
        self.dic_hyphen = pyphen.Pyphen(lang=idioma)
    
    def silabear(self, palabra):
        silabas = self.dic_hyphen.inserted(palabra).split("-")
        if self.idioma == 'es':
            if palabra == "una":
                silabas = ['u', 'na']
            elif palabra == "era":
                silabas = ['e', 'ra']
        return silabas

class CreadorSilabeador:
    def __init__(self, idioma):
        self.idioma = idioma
        self.silabeador = Silabeador(self._convertir_idioma(idioma))
    
    def _convertir_idioma(self, idioma):
        idiomas = {'es': 'es', 'en': 'en_US', 'fr': 'fr_FR', 'pt': 'pt_PT'}
        return idiomas.get(idioma, 'en_US')
    
    def crear_silabeador(self, input_path, output_path):
        with open(input_path, 'r', encoding='utf-8') as file:
            texto = file.read()
        
        texto_limpio = TextoLimpio.limpiar(texto, self.idioma)
        
        if self.idioma in ['es', 'fr', 'pt']:
            palabras_silabeadas = [' '.join(self.silabeador.silabear(palabra)) for palabra in texto_limpio.split()]
        elif self.idioma == 'en':
            palabras_silabeadas = [' '.join(self.silabeador.silabear(palabra)) for palabra in texto.split()]
        else:
            raise ValueError('Idioma no compatible')
        
        diccionario = '\n'.join(' ##'.join(palabras.split()) for palabras in texto.split('\n'))
        
        with open(output_path, 'w', encoding='utf-8') as file:
            file.write(diccionario)

input_path = './newstrain2014.txt'
output_path = './train-silabificado.txt'
idioma = 'en'

creador = CreadorSilabeador(idioma)
creador.crear_silabeador(input_path, output_path)
