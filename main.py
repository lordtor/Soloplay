import random
import numpy
import math
class Player:
    def __init__(self, name, race, gender):
        self.name = name
        self.level = 1
        self.health = 1000
        self.skills = {}
        self.race = race
        self.gender = gender

    def add_skill(self, skill):
        self.skills.update(skill)


class Opponent:
    def __init__(self):
        self.race = RACE[random.randint(0, len(RACE)-1)]
        self.skills = RACE_SKILS[self.race]["Skills"]
        self.level = random.randint(0, MAX_LEVELS-1)
        probability = LEVEL_PROBABILITY[self.level]
        for skill in self.skills:
            r_level = random.randint(self.level - 5, self.level + 5)
            r_r = random.random()
            try:
                if probability >= r_r:
                    t_skill = math.fabs((float(self.skills[skill]) * probability) - (
                            float(self.skills[skill]) * (r_level / (float(self.skills[skill]) + 0.1))))
                else:
                    t_skill = math.fabs((float(self.skills[skill]) * r_r) - (
                            float(self.skills[skill]) * (r_level / (float(self.skills[skill]) + 0.1))))
                if format(t_skill, '.0f') == '0':
                    self.skills[skill] = float(RACE_SKILS[self.race]["Skills"][skill])
                else:
                    self.skills[skill] = format(t_skill, '.0f')
            except ZeroDivisionError:
                if probability <= r_r:
                    t_skill = math.fabs((float(self.skills[skill]) * probability) - (
                                float(self.skills[skill]) * (r_level / (float(self.skills[skill]) + 0.1))))
                else:
                    t_skill = math.fabs((float(self.skills[skill]) * r_r) - (
                                float(self.skills[skill]) * (r_level / (float(self.skills[skill]) + 0.1))))
                if format(t_skill, '.0f') == 0:
                    self.skills[skill] = float(RACE_SKILS[self.race]["Skills"][skill])
                else:
                    self.skills[skill] = format(t_skill, '.0f')


MAX_LEVELS = 99
BASE_SKILL = {"Power": 20, "Agility": 20, "Body_type": 20, "Intelligence": 20, "Wisdom": 20, "Charisma": 20}
RACE = ("Human", "Dwarve", "Gnome", "Elve", "Half-Elve", "Halfling", "Half-orc")
RACE_SKILS = {"Human":
                  {"Skills": {
                      "Power": 15, "Agility": 15, "Body_type": 15, "Intelligence": 15, "Wisdom": 15, "Charisma": 15}},
              "Dwarve":
                  {"Skills": {
                      "Power": 10, "Agility": 14, "Body_type": 7, "Intelligence": 15, "Wisdom": 15, "Charisma": 14}},
              "Gnome":
                  {"Skills": {
                      "Power": 12, "Agility": 15, "Body_type": 10, "Intelligence": 12, "Wisdom": 15, "Charisma": 15}},
              "Elve":
                  {"Skills": {
                      "Power": 15, "Agility": 12, "Body_type": 11, "Intelligence": 10, "Wisdom": 15, "Charisma": 10}},
              "Half-Elve":
                  {"Skills": {
                      "Power": 15, "Agility": 12, "Body_type": 12, "Intelligence": 14, "Wisdom": 15, "Charisma": 15}},
              "Halfling":
                  {"Skills": {
                      "Power": 11, "Agility": 11, "Body_type": 8, "Intelligence": 12, "Wisdom": 14, "Charisma": 15}},
              "Half-orc":
                  {"Skills": {
                      "Power": 13, "Agility": 15, "Body_type": 11, "Intelligence": 10, "Wisdom": 15, "Charisma": 15}}
              }
n = numpy.arange(0, MAX_LEVELS, 1)
LEVEL_PROBABILITY = {}
for i in n:
    ver = float(format(((i+1) / float(format(0.84397123, '.8f')))/123, '.2f'))
    LEVEL_PROBABILITY.update({i: ver})




opo = Opponent()
print(opo.race)
print(opo.level)
print(opo.skills)

r = random.randint(1, 9)
i = 0
while i < 1000:
    i += 1
    opo = Opponent()
    print(opo.race)
    print(opo.level)
    print(opo.skills)
    del opo
#     r = random.randint(1, 10-1)
#     f = (10 - (10 * (r / 10)))
#     if f == 0.0:
#         print(">>>>>>>>>>>>>>>>",f)
#     else:
#         print(f)
