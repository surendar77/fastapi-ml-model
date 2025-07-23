import random

# Define the original dataset structure
original_data = {
    'math': [78, 65, 78, 45, 30, 60, 80, 40, 20, 50],
    'science': [20, 68, 45, 82, 63, 81, 20, 40, 60, 90],
    'English': [30, 70, 45, 65, 98, 42, 30, 30, 60, 60],
    'Result': ['Fail', 'Pass', 'Fail', 'Fail', 'Fail', 'Pass', 'Fail', 'Fail', 'Fail', 'Pass']
}

# Generate 50 new records based on the structure
random.seed(42)  # For reproducibility

data = {
    'math': [random.choice(original_data['math']) for _ in range(50)],
    'science': [random.choice(original_data['science']) for _ in range(50)],
    'English': [random.choice(original_data['English']) for _ in range(50)],
    'Result': [random.choice(original_data['Result']) for _ in range(50)],
}

# Display the first few records to verify
print(data)
