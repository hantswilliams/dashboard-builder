import pandas as pd 

########################################################################
# Create a simple DataFrame
df = pd.DataFrame({
    'condition': ['Flu', 'Cold', 'Chickenpox', 'Measles', 'Malaria', 
                'Ebola', 'Dengue', 'Cholera', 'Typhoid', 'Hepatitis', 
                'AIDS', 'Tuberculosis', 'COVID-19', 'Zika', 'Meningitis'],
    'condition_count': [10000, 12000, 3000, 4000, 5000, 200, 
                        2300, 400, 2200, 3000, 5000, 11000, 
                        14000, 800, 2500]
})