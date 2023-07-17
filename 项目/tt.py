from mesa import Agent, Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from mesa.datacollection import DataCollector
import random

class Employee(Agent):
    def __init__(self, unique_id, model, employee_type):
        super().__init__(unique_id, model)
        self.type = employee_type
        self.cultural_acceptance = random.random()
        self.interaction_degree = random.randint(1, 10)

    def step(self):
        self.move()
        other_agent = self.random.choice(self.model.schedule.agents)
        if other_agent.unique_id != self.unique_id:
            self.interact(other_agent)

    def move(self):
        possible_steps = self.model.grid.get_neighborhood(
            self.pos,
            moore=True,
            include_center=False)
        new_position = self.random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)

    def interact(self, other):
        if self.type != other.type:
            self.cultural_acceptance += 0.01 * self.interaction_degree


class EmploymentModel(Model):
    def __init__(self, N, width, height):
        self.num_agents = N
        self.grid = MultiGrid(width, height, True)
        self.schedule = RandomActivation(self)
        self.datacollector = DataCollector(
            model_reporters={"AvgAcceptance": lambda m: sum(
                agent.cultural_acceptance for agent in m.schedule.agents) / m.schedule.get_agent_count()},
            agent_reporters={"CulturalAcceptance": "cultural_acceptance"})

        for i in range(self.num_agents):
            employee_type = "local" if i < self.num_agents / 2 else "foreign"
            a = Employee(i, self, employee_type)
            self.schedule.add(a)

            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(a, (x, y))

    def step(self):
        self.datacollector.collect(self)
        self.schedule.step()

from mesa.visualization.modules import CanvasGrid, ChartModule
from mesa.visualization.ModularVisualization import ModularServer

def agent_portrayal(agent):
    portrayal = {"Shape": "circle",
                 "Filled": "true",
                 "r": 0.5}

    if agent.type == "local":
        portrayal["Color"] = "red"
    else:
        portrayal["Color"] = "blue"
    return portrayal

grid = CanvasGrid(agent_portrayal, 10, 10, 500, 500)
chart = ChartModule([{"Label": "AvgAcceptance",
                      "Color": "Black"}])

server = ModularServer(EmploymentModel,
                       [grid, chart],
                       "Employment Model",
                       {"N":100, "width":10, "height":10})
server.launch()
