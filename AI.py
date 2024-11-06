import matplotlib.pyplot as plt
import numpy as np

print("Loading the Smart Health Bot. Please wait...")


num_cases = 100

# Generate synthetic health data
age = np.random.randint(18, 100, num_cases)                     
gender = np.random.randint(1, 4, num_cases)                     
bp_systolic = np.random.randint(90, 180, num_cases)             
bp_diastolic = np.random.randint(60, 120, num_cases)            
heart_rate = np.random.randint(50, 120, num_cases)              
cholesterol = np.random.randint(150, 300, num_cases)         
glucose_level = np.random.randint(70, 200, num_cases)           
BMI = np.round(np.random.uniform(18, 40, num_cases), 2)        
physical_activity = np.random.randint(1, 11, num_cases)         
oxygen_saturation = np.random.randint(90, 100, num_cases)       
symptoms = np.random.randint(1, 8, num_cases)

