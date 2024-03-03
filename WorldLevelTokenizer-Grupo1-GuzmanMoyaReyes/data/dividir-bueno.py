import os

class DivisorDeArchivo:
    def __init__(self, input_path, num_partes=15):
        self.input_path = input_path
        self.num_partes = num_partes
        self.output_dir = 'output_files'
    
    def leer_archivo(self):
        with open(self.input_path, 'r', encoding='utf-8') as file:
            return file.readlines()
    
    def dividir_texto(self, texto):
        parte_size = len(texto) // self.num_partes
        return [texto[i:i+parte_size] for i in range(0, len(texto), parte_size)]
    
    def escribir_partes(self, partes):
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
        
        for i, parte in enumerate(partes):
            output_path = os.path.join(self.output_dir, f'train{i+1}.txt')
            with open(output_path, 'w', encoding='utf-8') as file:
                file.writelines(parte)
    
    def ejecutar(self):
        texto = self.leer_archivo()
        partes = self.dividir_texto(texto)
        self.escribir_partes(partes)

input_path = 'train-silabificado.txt'
divisor = DivisorDeArchivo(input_path)
divisor.ejecutar()
