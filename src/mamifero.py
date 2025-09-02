from random import choice, seed


class mamifero(): 
    # Atributos de clase
    vertebrado = True
    amamanta = True
        
    # Atributos de instancia
    alimentacion= '' # Carnivoro, omnívoro, etc
    altura=0
    peso=0
    progenie= 0
    # Cuántos puede tener y cuántos van a sobrevivir    
    def reproducirse(self, max_progenie):
        self.progenie +=  choice(range( max_progenie))
    
    def crecer(self, crecimiento):
        self.altura += crecimiento
        self.peso += crecimiento * 0.4

#Y provemos nuestros metódos:
perro=mamifero()
perro.reproducirse(6)
print("El tipo de alimentación de nuestro perro es: ", perro.alimentacion, "mide",perro.altura,"pesa",perro.peso, "su descendencia asciende a",perro.progenie)