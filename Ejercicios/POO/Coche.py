from Vehiculo import Vehiculo

class Coche(Vehiculo):

    def __init__(self, tipo, marca, color, ruedas, velocidad, cilindrada):
        Vehiculo.__init__(self, tipo, marca, color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return "{} {} de {}cc y que llega a {}km/h de color {}".format(self.get_tipo(), self.get_marca(),  self.cilindrada, self.velocidad, self.get_color())
