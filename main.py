import numpy as np
import matplotlib.pyplot as plt
from music21 import converter

song = 'bwv565'

piece = converter.parse(song + '.mid')
notes = piece.flatten().notes
pitch_classes = [n.pitches[0].pitchClass for n in notes]
initial = np.bincount(pitch_classes, minlength=12).astype(float)
total_initial = initial.sum()

def interval_effect(distance):
	if distance == 0:
		return 0.1
	elif distance == 1:
		return -0.5
	elif distance == 2:
		return -0.2
	elif distance == 3:
		return 0.3
	elif distance == 4:
		return 0.4
	elif distance == 5:
		return 0.2
	elif distance == 6:
		return -0.4
	elif distance == 7:
		return 0.5
	elif distance == 8:
		return 0.2
	elif distance == 9:
		return 0.3
	elif distance == 10:
		return -0.2
	elif distance == 11:
		return -0.3
	else:
		return 0

competition = np.zeros((12, 12))
for i in range(12):
	for j in range(12):
		distance = min(abs(i - j), 12 - abs(i - j))
		competition[i][j] = interval_effect(distance)

population = initial.copy()
birth_rate = 0.02
generations = 1000

for gen in range(generations):
	new_population = population.copy()
	for i in range(12):
		growth = birth_rate * population[i]
		competition_effect = sum(competition[j][i] * population[j] for j in range(12))
		change = growth + competition_effect * 0.0001 * population[i]
		new_population[i] = population[i] + change
		if new_population[i] < 0:
			new_population[i] = 0
	total_now = new_population.sum()
	if total_now > 0:
		new_population = new_population / total_now * total_initial
	population = new_population

note_names = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
x = np.arange(12)

plt.figure(figsize=(12, 5))
plt.bar(x - 0.2, initial, width=0.4, label='Bach original', color='steelblue')
plt.bar(x + 0.2, np.round(population), width=0.4, label='After 1000 generations', color='orange')
plt.xticks(x, note_names)
plt.xlabel('Pitch class')
plt.ylabel('Count')
plt.title('Bach original vs Ecosystem simulation (BWV 565)')
plt.legend()
plt.tight_layout()
plt.savefig('result.png')
plt.show()
