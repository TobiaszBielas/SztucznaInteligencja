import sys
import scipy
import skfuzzy
from skfuzzy import control
import numpy as np
from matplotlib import pyplot as plt

distance = float(sys.argv[1])
angle = float(sys.argv[2])

if (distance <= 0 or distance > 100 or
    angle <= 0 or angle > 90): 
    sys.exit("Error! Incorrect Data.")

distance_level = control.Antecedent(np.arange(1, 100, 0.1), "distance")
angle_level = control.Antecedent(np.arange(1, 90, 0.1), "angle")
velocity_level = control.Consequent(np.arange(1, 50, 0.1), "velocity")

distance_level['v-low'] = skfuzzy.trimf(distance_level.universe, [1, 1, 15])
distance_level['low'] = skfuzzy.trimf(distance_level.universe, [13, 16, 24])
distance_level['avg'] = skfuzzy.trimf(distance_level.universe, [20, 40, 45])
distance_level['high'] = skfuzzy.trimf(distance_level.universe, [43, 60, 90])
distance_level['v-high'] = skfuzzy.trimf(distance_level.universe, [89, 100, 100])


angle_level['low'] = skfuzzy.trimf(angle_level.universe, [1, 1, 35])
angle_level['avg'] = skfuzzy.trimf(angle_level.universe, [38, 45, 52])
angle_level['high'] = skfuzzy.trimf(angle_level.universe, [55, 90, 90])

velocity_level['v-low'] = skfuzzy.trimf(velocity_level.universe, [1, 1, 8])
velocity_level['low'] = skfuzzy.trimf(velocity_level.universe, [7, 12, 18])
velocity_level['avg'] = skfuzzy.trimf(velocity_level.universe, [16, 25, 32])
velocity_level['high'] = skfuzzy.trimf(velocity_level.universe, [30, 40, 47])
velocity_level['v-high'] = skfuzzy.trimf(velocity_level.universe, [46.5, 50, 50])

rules = [None] * 15
rules[0] = control.Rule(distance_level['v-low'] & angle_level['low'], velocity_level['v-low'])
rules[1] = control.Rule(distance_level['v-low'] & angle_level['avg'], velocity_level['v-low'])
rules[2] = control.Rule(distance_level['v-low'] & angle_level['high'], velocity_level['v-low'])

rules[3] = control.Rule(distance_level['low'] & angle_level['low'], velocity_level['low'])
rules[4] = control.Rule(distance_level['low'] & angle_level['avg'], velocity_level['v-low'])
rules[5] = control.Rule(distance_level['low'] & angle_level['high'], velocity_level['low'])

rules[6] = control.Rule(distance_level['avg'] & angle_level['low'], velocity_level['avg'])
rules[7] = control.Rule(distance_level['avg'] & angle_level['avg'], velocity_level['low'])
rules[8] = control.Rule(distance_level['avg'] & angle_level['high'], velocity_level['avg'])

rules[9] = control.Rule(distance_level['high'] & angle_level['low'], velocity_level['high'])
rules[10] = control.Rule(distance_level['high'] & angle_level['avg'], velocity_level['avg'])
rules[11] = control.Rule(distance_level['high'] & angle_level['high'], velocity_level['high'])

rules[12] = control.Rule(distance_level['v-high'] & angle_level['low'], velocity_level['v-high'])
rules[13] = control.Rule(distance_level['v-high'] & angle_level['avg'], velocity_level['high'])
rules[14] = control.Rule(distance_level['v-high'] & angle_level['high'], velocity_level['v-high'])


velocity_calc = control.ControlSystemSimulation(control.ControlSystem(rules))
velocity_calc.input['distance'] = distance
velocity_calc.input['angle'] = angle
velocity_calc.compute()

velocity_level.view(sim=velocity_calc)
plt.show()