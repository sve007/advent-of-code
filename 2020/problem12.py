import numpy as np
import math

with open("input_data/input_problem12", "r") as file:
    instructions = file.read().split("\n")


class Boaty:

    def __init__(self, waypoint=np.array([-10, 1])):
        self.north = np.array([0., 1.])
        self.east = np.array([-1., 0.])
        self.south = np.array([0., -1.])
        self.west = np.array([1., 0.])
        self.pos = np.array([0., 0.])
        self.waypoint = waypoint
        self.dir = self.east

    def process_instruction_waypoint(self, instruction):
        if i[0] == "F":
            self.pos += self.waypoint*float(instruction[1:])
        if i[0] == "N":
            self.waypoint += self.north*float(instruction[1:])
        if i[0] == "E":
            self.waypoint += self.east*float(instruction[1:])
        if i[0] == "S":
            self.waypoint += self.south*float(instruction[1:])
        if i[0] == "W":
            self.waypoint += self.west*float(instruction[1:])
        if i[0] == "R":
            angle = int(instruction[1:])/360*2*math.pi
            rotation_matrix = np.array([[math.cos(angle), -math.sin(angle)], [math.sin(angle), math.cos(angle)]])
            self.waypoint = rotation_matrix @ self.waypoint
        elif i[0] == "L":
            angle = int(instruction[1:])/360*2*math.pi
            rotation_matrix = np.array([[math.cos(angle), math.sin(angle)], [-math.sin(angle), math.cos(angle)]])
            self.waypoint = rotation_matrix @ self.waypoint

        return

    def process_instruction(self, instruction):
        if i[0] == "F":
            self.pos += self.dir*float(instruction[1:])
        if i[0] == "N":
            self.pos += self.north*float(instruction[1:])
        if i[0] == "E":
            self.pos += self.east*float(instruction[1:])
        if i[0] == "S":
            self.pos += self.south*float(instruction[1:])
        if i[0] == "W":
            self.pos += self.west*float(instruction[1:])
        if i[0] == "R":
            angle = int(instruction[1:])/360*2*math.pi
            rotation_matrix = np.array([[math.cos(angle), -math.sin(angle)], [math.sin(angle), math.cos(angle)]])
            self.dir = rotation_matrix @ self.dir
        elif i[0] == "L":
            angle = int(instruction[1:])/360*2*math.pi
            rotation_matrix = np.array([[math.cos(angle), math.sin(angle)], [-math.sin(angle), math.cos(angle)]])
            self.dir = rotation_matrix @ self.dir

        return


boatymcboatface1 = Boaty()
boatymcboatface2 = Boaty()
for i in instructions:
    boatymcboatface1.process_instruction(i)
    boatymcboatface2.process_instruction_waypoint(i)
answer1 = int(abs(boatymcboatface1.pos[0]) + abs(boatymcboatface1.pos[1]))
answer2 = int(abs(boatymcboatface2.pos[0]) + abs(boatymcboatface2.pos[1]))
print(f"Answer to problem 12 part 1: {answer1}")
print(f"Answer to problem 12 part 2: {answer2}")
