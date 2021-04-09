from mesa import Agent
from params import *

class Pasto(Agent):
    def __init__(self, unique_id, pos, model, crecido, contador_crecimiento):
        super().__init__(unique_id, model)
        self.pos = pos
        self.crecido = crecido
        self.contador_crecimiento = contador_crecimiento
        
    def step(self):
        if not self.crecido:
            # Si ya pasó tiempo de crecimiento, reiniciamos estado inicial pasto
            if self.contador_crecimiento <= 0:
                self.crecido = True
                self.contador_crecimiento = CONTADOR_CRECIMIENTO_INICIAL
            # Si no, disminuimos el contador
            else:
                self.contador_crecimiento -= 1  