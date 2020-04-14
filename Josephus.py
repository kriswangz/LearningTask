# %%
#!/usr/bin/python3
# -*- coding: utf-8 -*-

# The program is used for solving josephus promblem.
# description:
#           Counting from the first person, when count to the step value, he must commit suicide,
#           and then report again from the next, until the last one.
# Author: Chris Wang


class Josephus:
    """
     this class will output the survivor index numbers in rings.

    Attributes:
        rings: An input ring([0,1..n]) for Josephus problem's items.
        step: step value.
        start: start person.

    Returns:
        judge_survivor: return survive people's index in a ring like 0(rings[0]).
    """

    def __init__(self, rings, step, start):
        self.rings = rings
        self.step = step
        self.start = start

    def judge_survivor(self):
        p = self.start       # index point

        for i in range(len(self.rings)):
            if len(self.rings) == 1:
                break

            p = (p + (self.step - 1)) % len(self.rings)
            self.rings.pop(p)

        return self.rings[0]


def create_rings(name):
    """
    convert name items to rings, use numbers instead of complex characters like dictionary.

    Attributes:
        name: people's characters like name, age and gender.

    Return:
        rings: from input items to rings[0..n]
    """
    length = int(len(name))

    if length == 1:
        return [0]

    rings = [i for i in range(length)]

    return rings


if __name__ == '__main__':
    name = {0: ['Chris', '24', 'male'], 1: ['Anna', '18', 'female'],
            3: ["Bob", '30', 'male'], 4: ["David", '21', 'male']}
    step = 2
    start = 0
    name_offset = 0  # offset index in return list ['name', 'age', 'gender']
    age_offset = 1
    gender_offset = 2

    rings = create_rings(name)  # generate rings [0..n] n=len(name)

    joseph = Josephus(rings, step, start)
    # return index value in rings, ['name', 'age',  'gender'] included.
    survivor = joseph.judge_survivor()
    print("Survivor's name is %s, age is %s, gender is %s"
          % (name[survivor][name_offset], name[survivor][age_offset], name[survivor][gender_offset]))
