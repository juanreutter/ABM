from mesa import Model
from mesa.space import MultiGrid
from mesa.datacollection import DataCollector
from mesa.time import RandomActivation

from agent_lobo import Lobo
from agent_oveja import Oveja
from agent_pasto import Pasto

from params import *

class LobosOvejasPastoModelo(Model):

    verbose = False  # Print-monitoring

    description = (
        "A model for simulating wolf and sheep (predator-prey) ecosystem modelling."
    )

    def __init__(
        self, 
        num_lobos=NUM_LOBOS_INICIAL, 
        num_ovejas=NUM_OVEJAS_INICIAL, 
        width=WIDTH_GRID, 
        height=HEIGHT_GRID
        ):

        super().__init__()

        self.num_lobos = num_lobos
        self.num_ovejas = num_ovejas
        self.grid = MultiGrid(width, height, True)
        self.schedule = RandomActivation(self)
        self.current_id = 0

        self.datacollector = DataCollector(
            {
                "Wolves": lambda m: len([lobo for agent in m.schedule.agents if isinstance(agent, Lobo)]),
                "Sheep": lambda m: len([oveja for agent in m.schedule.agents if isinstance(agent, Oveja)]),
            }
        )
        
        

        # Crear lobos
        for i in range(self.num_lobos):
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            lobo = Lobo(self.next_id(), (x,y), self.random.randrange(2 * ENERGIA_COMIDA_LOBOS), self)
            self.schedule.add(lobo)
            # Meto los lobos en un lugar al azar de la grilla
            self.grid.place_agent(lobo, (x, y))
            
        # Crer ovejas
        for i in range(self.num_ovejas):
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            oveja = Oveja(self.next_id(), (x,y) , self.random.randrange(2 * ENERGIA_COMIDA_OVEJAS), self)
            self.schedule.add(oveja)
            # Agrego a un punto al azar de la grilla
            self.grid.place_agent(oveja, (x, y)) 
        
        # Crear pasto
        for agent, x, y in self.grid.coord_iter():
            crecido = self.random.choice([True, False])
            
            contador = CONTADOR_CRECIMIENTO_INICIAL
            if not crecido:
                contador= self.random.randrange(CONTADOR_CRECIMIENTO_INICIAL) 

            pasto = Pasto(self.next_id(), (x,y), self, crecido, contador)
            self.schedule.add(pasto)
            self.grid.place_agent(pasto, (x,y))

        self.running = True
        self.datacollector.collect(self)

    def step(self):
        self.schedule.step()
        self.datacollector.collect(self)
        if self.verbose:
            print(
                [
                    self.schedule.time,
                    len([lobo for agent in self.schedule.agents if isinstance(agent, Lobo)]),
                    len([oveja for agent in self.schedule.agents if isinstance(agent, Oveja)]),
                ]
            )

    def run_model(self, step_count=200):

        if self.verbose:
            print("Initial number wolves: ", len([lobo for agent in self.schedule.agents if isinstance(agent, Lobo)]))
            print("Initial number sheep: ", len([oveja for agent in self.schedule.agents if isinstance(agent, Oveja)]))

        for i in range(step_count):
            self.step()

        if self.verbose:
            print("")
            print("Final number wolves: ", len([lobo for agent in self.schedule.agents if isinstance(agent, Lobo)]))
            print("Final number sheep: ", len([oveja for agent in self.schedule.agents if isinstance(agent, Oveja)]))