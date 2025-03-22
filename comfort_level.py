import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz
from skfuzzy import control as ctrl

Temperature = ctrl.Antecedent(np.arange(0, 36, 1), 'Temperature')
Humidity = ctrl.Antecedent(np.arange(0, 81, 1), 'Humidity')
Comfort_level = ctrl.Consequent(np.arange(0, 41, 1), 'Comfort Level')

Temperature['low'] = fuzz.trimf(Temperature.universe, [0, 0, 20])
Temperature['medium'] = fuzz.trimf(Temperature.universe, [15, 25, 35])
Temperature['high'] = fuzz.trimf(Temperature.universe, [20, 35, 35])

Humidity['low'] = fuzz.trimf(Humidity.universe, [0, 0, 40])
Humidity['medium'] = fuzz.trimf(Humidity.universe, [30, 60, 80])
Humidity['high'] = fuzz.trimf(Humidity.universe, [50, 80, 80])

Comfort_level['uncomfortable'] = fuzz.trimf(Comfort_level.universe, [0, 0, 4])
Comfort_level['neutral'] = fuzz.trimf(Comfort_level.universe, [3, 7, 10])
Comfort_level['comfortable'] = fuzz.trimf(Comfort_level.universe, [6, 10, 10])

rule1 = ctrl.Rule(Temperature['low'] & Humidity['low'], Comfort_level['uncomfortable'])
rule2 = ctrl.Rule(Temperature['low'] & Humidity['high'], Comfort_level['uncomfortable'])
rule3 = ctrl.Rule(Temperature['high'] & Humidity['high'], Comfort_level['uncomfortable'])
rule4 = ctrl.Rule(Temperature['high'] & Humidity['medium'], Comfort_level['uncomfortable'])

rule5 = ctrl.Rule(Temperature['low'] & Humidity['medium'], Comfort_level['neutral'])
rule6 = ctrl.Rule(Temperature['medium'] & Humidity['low'], Comfort_level['neutral'])
rule7 = ctrl.Rule(Temperature['medium'] & Humidity['high'], Comfort_level['neutral'])
rule8 = ctrl.Rule(Temperature['high'] & Humidity['low'], Comfort_level['neutral'])

rule9 = ctrl.Rule(Temperature['medium'] & Humidity['medium'], Comfort_level['comfortable'])

comfort_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9])
comfort_sim = ctrl.ControlSystemSimulation(comfort_ctrl)

comfort_sim.input['Temperature'] = int(input("Temperature: "))
comfort_sim.input['Humidity'] = int(input("Humidity: "))

comfort_sim.compute()

print("Comfort Level: ",comfort_sim.output['Comfort Level'])

Comfort_level.view(sim=comfort_sim)
plt.show()

