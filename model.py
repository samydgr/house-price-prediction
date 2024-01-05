import joblib
from sklearn import preprocessing
import pandas as pd
import numpy as np
file_path = 'housePrice.csv'
df = pd.read_csv(file_path)
df.dropna(inplace=True)
Addresses = df['Address'].unique()
def predict_house(area,room,parking,warehouse, elevator,address):
    model = joblib.load('model.pkl')
    # Replace 'your_file_path.csv' with the actual path to your CSV file
    file_path = 'housePrice.csv'
    scaler = joblib.load('scaler.joblib')
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(file_path)
    df.dropna(inplace=True)
    unique_addresses = df['Address'].unique()
    df.drop(columns=['Price(USD)'], inplace=True)
    address_mapping = {address: 0 for address in unique_addresses}
    user_input_address = address

    # Set the value for the user input address to 1
    address_mapping[user_input_address] = 1
    input_row = np.array([area,room, parking, warehouse,elevator,0] + list(address_mapping.values())).reshape(1, -1)
    input_row = scaler.transform(input_row)
    x = model.predict(input_row) 

    x = np.insert(input_row, 5, x) # Ensure input_row is passed as a list
    x_reshaped = np.array(x).reshape(1, -1)

    # Invert the scaling transformation
    # Invert the scaling transformation
    original_values = scaler.inverse_transform(x_reshaped[:, :-1])

    # Print the original values
    print(original_values[0][5])
    return original_values[0][5]
