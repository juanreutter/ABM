from mesa import Agent

from params import *
from agent_oveja import Oveja

class Lobo(Agent):
    # Agentes que se comen a las ovejas.
    def __init__(self, unique_id, pos, e, model):
        # la clase agente guarda los ids y los enlaza con el modelo 
        # unique_id sirve para identificar a un agente
        # pos es una tupla en la grilla
        # e es la energía
        # model es pa usar cosas de la simulación aca adentro
        super().__init__(unique_id,model)
        # lobos tienen energia, y una posicion 
        self.energia = e
        self.pos = pos
    
    def move(self):
        # get_neighbourhood es utilidad de mesa pa devolver los vecinos
        possible_steps = self.model.grid.get_neighborhood(
            self.pos,
            moore=False,
            include_center=False)
        new_position = self.random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)
        self.energia -= ENERGIA_PERDIDA_STEP
        
    def step(self):
        self.move()
         
        # comerse alguna oveja que este en su grilla 
        cellmates = self.model.grid.get_cell_list_contents([self.pos])
        sheep = [obj for obj in cellmates if isinstance(obj, Oveja)]
        if len(sheep) > 0: 
            victima = self.random.choice(sheep)
            self.model.grid._remove_agent(self.pos, victima)
            self.model.schedule.remove(victima)
            self.energia += ENERGIA_COMIDA_LOBOS
            
        #si no tengo energia, muero 
        if self.energia < 0: 
            self.model.grid._remove_agent(self.pos, self)
            self.model.schedule.remove(self)
            return
        
        # tener hijos           
        if self.model.random.random() < PROB_REPRODUCCION_LOBO: 
            self.energia /= ENERGIA_PERDIDA_REPRODUCCION
            hijo = Lobo(self.model.next_id(),self.pos,self.energia,self.model)
            self.model.grid.place_agent(hijo, hijo.pos)
            self.model.schedule.add(hijo)