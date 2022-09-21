class Punto():

    def __init__(self, name, x1,y1):

        self.name= name
        self.x1 = x1
        self.y1 = y1
        if x1==None:
            x1=0
        if y1==None:
            y1=0

    def  __str__(self):
        cadena = self.name+'('+self.x1+','+self.y1+')'
        return cadena

    def cuadrante(self):
        if self.x1>0 and self.y1 >0:
            cuadrante = 1
        if self.x1<0 and self.y1>0:
            cuadrante = 2
        if self.x1<0 and self.y1<0:
            cuadrante = 3
        if self.x1>0 and self.y1<0:
            cuadrante = 4

        return cuadrante

    def vector(self, punto2):
        vector = (self.name+punto2.name,(punto2.x1-self.x1),(punto2.y1-self.y1))
        return vector
        
        
            

