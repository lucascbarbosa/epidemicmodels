
import json

from constants import *

class EpiScenario:
	def __init__(self, configfile):
		with open(configfile, 'r') as cf:
			self.parameters = json.load(cf)
		self.totalpop = self.parameters['totalpop']
		if 'maxdays' in self.parameters:
			self.maxdays = self.parameters['maxdays']
		else:
			self.maxdays = 160

		if 'incubation_period' in self.parameters:
			self.incubation_period = self.parameters['incubation_period']
		else:
			self.incubation_period = 3

		if 'prediagnosis_period' in self.parameters:
			self.prediagnosis = self.parameters['prediagnosis_period']
		else:
			self.prediagnosis = 3.8


		self.susceptible = self.parameters['initial_values']['susceptible']
		self.infected = self.parameters['initial_values']['infected']
		self.infectious = self.parameters['initial_values']['infectious']

		self.r0_date_offsets = self.parameters['R0_set']['date_offsets']
		self.r0_values = self.parameters['R0_set']['r0_values']
		self.age_distribution = self.parameters['age_distribution']
		self.age_projection = self.parameters['age_projection']
		print(f"Age projection: ageproj {self.age_projection[AGE8x]}")
		self.subgrouprates = {
			AGE0x: SubgroupRates(self.age_projection[AGE0x], self.age_distribution[AGE0x]),
			AGE1x: SubgroupRates(self.age_projection[AGE1x], self.age_distribution[AGE1x]),
			AGE2x: SubgroupRates(self.age_projection[AGE2x], self.age_distribution[AGE2x]),
			AGE3x: SubgroupRates(self.age_projection[AGE3x], self.age_distribution[AGE3x]),
			AGE4x: SubgroupRates(self.age_projection[AGE4x], self.age_distribution[AGE4x]),
			AGE5x: SubgroupRates(self.age_projection[AGE5x], self.age_distribution[AGE5x]),
			AGE6x: SubgroupRates(self.age_projection[AGE6x], self.age_distribution[AGE6x]),
			AGE7x: SubgroupRates(self.age_projection[AGE7x], self.age_distribution[AGE7x]),
			AGE8x: SubgroupRates(self.age_projection[AGE8x], self.age_distribution[AGE8x])
		}





