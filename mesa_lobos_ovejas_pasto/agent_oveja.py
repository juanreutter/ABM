from mesa import Agent
from params import *

from agent_pasto import Pasto 

class Oveja(Agent):
    def __init__(self, unique_id, pos, energia, model):
        super().__init__(unique_id, model)
        self.pos = pos
        self.energia = energia

    def move(self):
        possible_steps = self.model.grid.get_neighborhood(
            self.pos,
            moore=False,
            include_center=False)
        new_position = self.random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)
        self.energia -= ENERGIA_PERDIDA_STEP
        
    def step(self):
        self.move()
        
        # Comer Pasto
        celda_actual = self.model.grid.get_cell_list_contents([self.pos])
        pasto = [obj for obj in celda_actual if isinstance(obj, Pasto)][0]
        if pasto.crecido:
            self.energia += ENERGIA_COMIDA_OVEJAS
            pasto.crecido = False
        
        #si no tengo energia, muero 
        if self.energia < 0: 
            self.model.grid._remove_agent(self.pos, self)
            self.model.schedule.remove(self)
            return
        
        # Reproducción
        if self.model.random.random() < PROB_REPRODUCCION_OVEJA: 
            self.energia /= ENERGIA_PERDIDA_REPRODUCCION
            hija = Oveja(self.model.next_id(), self.pos, self.energia, self.model)
            self.model.grid.place_agent(hija, hija.pos)
            self.model.schedule.add(hija)