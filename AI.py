import matplotlib.pyplot as plt
import numpy as np

print("Loading the Smart Health Bot. Please wait...")


num_cases = 100


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

health_risk_score = np.round(np.random.uniform(0, 100, num_cases), 2)

def normalize(data):
    return (data - data.min()) / (data.max() - data.min())

age_norm = normalize(age)
gender_norm = normalize(gender)
bp_systolic_norm = normalize(bp_systolic)
bp_diastolic_norm = normalize(bp_diastolic)
heart_rate_norm = normalize(heart_rate)
cholesterol_norm = normalize(cholesterol)
glucose_level_norm = normalize(glucose_level)
BMI_norm = normalize(BMI)
physical_activity_norm = normalize(physical_activity)
oxygen_saturation_norm = normalize(oxygen_saturation)
symptoms_norm = normalize(symptoms)
health_risk_norm = normalize(health_risk_score)


weights = np.random.rand(11)
bias = np.random.rand(1)
learning_rate = 0.01
num_epochs = 500

def predict(features, weights, bias):
    return np.dot(features, weights) + bias


def cost_function(predicted, actual):
    return np.mean((predicted - actual) ** 2)


def train_model(features, target, weights, bias, learning_rate, epochs):
    for epoch in range(epochs):
      
        predictions = predict(features, weights, bias)

       
        error = predictions - target
        cost = cost_function(predictions, target)

        
        weights_gradient = 2 * np.dot(features.T, error) / len(target)
        bias_gradient = 2 * np.mean(error)

       
        weights -= learning_rate * weights_gradient
        bias -= learning_rate * bias_gradient

        if epoch % 50 == 0:
            print(f"Epoch {epoch} | Cost: {cost:.4f}")
    
    return weights, bias


features = np.column_stack((age_norm, gender_norm, bp_systolic_norm, bp_diastolic_norm, 
                            heart_rate_norm, cholesterol_norm, glucose_level_norm, 
                            BMI_norm, physical_activity_norm, oxygen_saturation_norm, 
                            symptoms_norm))

weights, bias = train_model(features, health_risk_norm, weights, bias, learning_rate, num_epochs)
print("\nModel training completed.\n")

user_features = None

def assess_health():
    global user_features
    print("Enter details for a new health assessment:\n")
    user_age = int(input("Enter Age: "))
    user_gender = int(input("Enter Gender (1 for Male, 2 for Female, 3 for Other): "))
    user_bp_sys = int(input("Enter Systolic Blood Pressure: "))
    user_bp_dia = int(input("Enter Diastolic Blood Pressure: "))
    user_heart_rate = int(input("Enter Heart Rate: "))
    user_cholesterol = int(input("Enter Cholesterol Level: "))
    user_glucose = int(input("Enter Glucose Level: "))
    user_BMI = float(input("Enter BMI: "))
    user_activity = int(input("Rate Physical Activity (1-10): "))
    user_oxygen = int(input("Enter Oxygen Saturation: "))
    user_symptoms = int(input("Enter Symptoms Code (1-7): "))

    user_features = np.array([
        (user_age - age.min()) / (age.max() - age.min()),
        (user_gender - gender.min()) / (gender.max() - gender.min()),
        (user_bp_sys - bp_systolic.min()) / (bp_systolic.max() - bp_systolic.min()),
        (user_bp_dia - bp_diastolic.min()) / (bp_diastolic.max() - bp_diastolic.min()),
        (user_heart_rate - heart_rate.min()) / (heart_rate.max() - heart_rate.min()),
        (user_cholesterol - cholesterol.min()) / (cholesterol.max() - cholesterol.min()),
        (user_glucose - glucose_level.min()) / (glucose_level.max() - glucose_level.min()),
        (user_BMI - BMI.min()) / (BMI.max() - BMI.min()),
        (user_activity - physical_activity.min()) / (physical_activity.max() - physical_activity.min()),
        (user_oxygen - oxygen_saturation.min()) / (oxygen_saturation.max() - oxygen_saturation.min()),
        (user_symptoms - symptoms.min()) / (symptoms.max() - symptoms.min())
    ])

    
    health_score = predict(user_features, weights, bias) * 100
    print(f"\nEstimated Health Risk Score: {health_score:.2f}%")


assess_health()


def recommendations(health_score):
    if health_score < 30:
        print("Low risk detected. Maintain a balanced lifestyle!")
    elif 30 <= health_score < 70:
        print("Moderate risk detected. Consider consulting a healthcare professional.")
    else:
        print("High risk detected! Immediate medical attention recommended.")


user_health_score = predict(user_features, weights, bias) * 100
recommendations(user_health_score)