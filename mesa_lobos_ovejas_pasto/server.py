from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import CanvasGrid, ChartModule
from mesa.visualization.UserParam import UserSettableParameter

from agent_lobo import Lobo
from agent_oveja import Oveja
from agent_pasto import Pasto
from model import LobosOvejasPastoModelo


def wolf_sheep_portrayal(agent):
    if agent is None:
        return

    portrayal = {}

    if type(agent) is Oveja:
        portrayal["Shape"] = "resources/sheep.png"
        # https://icons8.com/web-app/433/sheep
        portrayal["scale"] = 0.9
        portrayal["Layer"] = 1

    elif type(agent) is Lobo:
        portrayal["Shape"] = "resources/wolf.png"
        # https://icons8.com/web-app/36821/German-Shepherd
        portrayal["scale"] = 2.5
        portrayal["Layer"] = 2
        portrayal["text"] = round(agent.energia, 1)
        portrayal["text_color"] = "#000000"

    elif type(agent) is Pasto:
        if agent.crecido:
            portrayal["Color"] = ["#c0df89", "#c0df89", "#c0df89"]
        else:
            portrayal["Color"] = ["#817351", "#817351", "#817351"]
        portrayal["Shape"] = "rect"
        portrayal["Filled"] = "true"
        portrayal["Layer"] = 0
        portrayal["w"] = 1
        portrayal["h"] = 1

    return portrayal


canvas_element = CanvasGrid(wolf_sheep_portrayal, 50, 50, 500, 500)
chart_element = ChartModule(
    [{"Label": "Wolves", "Color": "#AA0000"}, 
    {"Label": "Sheep", "Color": "#666666"}
    ]
)

server = ModularServer(
    LobosOvejasPastoModelo, [canvas_element, chart_element], "Wolf Sheep Predation"
)
server.port = 8521
