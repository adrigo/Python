from Vehiculo import Vehiculo

class Moto(Vehiculo):

    def __init__(self, tipo, marca, color, ruedas, velocidad, cilindrada):
        Vehiculo.__init__(self, tipo, marca, color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return "{} {}cc {}, que alcanza {}km/h de color {}".format(self.get_tipo(), self.cilindrada, self.get_marca(), self.velocidad, self.get_color())
