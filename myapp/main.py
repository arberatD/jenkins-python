import requests
import numpy as np

def calculate_mean(data):
    return np.mean(data)

if __name__ == "__main__":
    response = requests.get('https://api.exchangeratesapi.io/latest')
    rates = response.json()['rates']
    mean_rate = calculate_mean(list(rates.values()))
    print(f"Der durchschnittliche Wechselkurs ist: {mean_rate}")
