class Vehiculo():

    def __init__(self, tipo, marca, color, ruedas):
        self.tipo = tipo
        self.marca = marca
        self.color = color
        self.ruedas = ruedas
        
    def get_tipo(self):
        return self.tipo;
        
    def get_marca(self):
        return self.marca;

    def get_color(self):
        return self.color;

    def get_ruedas(self):
        return self.ruedas;
