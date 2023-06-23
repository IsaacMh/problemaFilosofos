import time
class Tenedor:
    def __init__(self):
        self.ocupado = False  
    def dejar(self):
        self.ocupado = False 
    def tomar(self):
        if self.ocupado == False:
            self.ocupado = True
        else:
            self.ocupado = False
    def estado(self):
        return self.ocupado
    
class Filosofos:    
    def __init__(self,filosofo,tenedor_derecho,tenedor_izquierdo):
        self.comio = False      
        self.filosofo = filosofo
        self.tenedor_derecho = tenedor_derecho
        self.tenedor_izquierdo = tenedor_izquierdo
    def pensar(self):
        print(f'{self.filosofo} esta pensando')
    def comer(self):        
        if self.tenedor_derecho == False and self.tenedor_izquierdo== False:
            self.comio = True
            print(f'{self.filosofo} esta comiendo')            
        else:
            self.pensar()
    def parar(self):
        return self.comio
    
def principal():
    tenedor_1 = Tenedor()
    tenedor_2 = Tenedor()
    tenedor_3 = Tenedor()
    tenedor_4 = Tenedor()
    tenedor_5 = Tenedor()
    conjTenedores = [tenedor_1,tenedor_2,tenedor_3,tenedor_4,tenedor_5]

    filosofo_1 = Filosofos('Filosofo 1', tenedor_1.estado(),tenedor_2.estado())
    filosofo_2 = Filosofos('Filosofo 2', tenedor_2.estado(),tenedor_3.estado())
    filosofo_3 = Filosofos('Filosofo 3', tenedor_3.estado(),tenedor_4.estado())
    filosofo_4 = Filosofos('Filosofo 4', tenedor_4.estado(),tenedor_5.estado())
    filosofo_5 = Filosofos('Filosofo 5', tenedor_5.estado(),tenedor_1.estado())
    conjFilosofos = [filosofo_1,filosofo_2,filosofo_3,filosofo_4,filosofo_5]

    contador=0
    while (filosofo_1.parar() and filosofo_2.parar() and filosofo_3.parar() and filosofo_4.parar() and filosofo_5.parar() ) == False:  
        contador %= 5
        f = conjFilosofos[contador]
        t_d = conjTenedores[contador]
        t_i = conjTenedores[(contador+1)%5]
        if f.parar() == False:
            if t_d.estado() == False and t_i.estado() == False:
                f.comer()
                t_d.tomar()
                t_i.tomar()
            else:
                f.pensar()
        else:
            print(f'{f.filosofo} ya comio')
            time.sleep(.5)
            t_d.dejar()
            t_i.dejar()
        contador += 1

if __name__ == "__main__":
    principal()