
import pandas as pd
import numpy as np
from faker import Faker

def generateGaussianData(mu: float, sigma: float, low: int, high: int, num_responses: int)-> np.array:
    # Generate numbers from a Gaussian distribution
    data = np.random.normal(mu, sigma, num_responses)
    data = np.round(np.clip(data, low, high)).astype(int)  # ensure values are between 1 and 5
    return data

fake = Faker()

# Define the number of responses = n_attendees * 0.4
eventbrite_df = pd.read_csv("data/pseudo_eventbrite_data.csv")
n_attendees = eventbrite_df.checked_in.sum()
num_responses = int(n_attendees*0.4)

impact_category_options = ["Job search", "Networking", "Career progression", "Upskilling"]

data = {
    'impact_score_attendee': generateGaussianData(3.5, 0.5, 1, 5, num_responses),
    'impact_category_attendee': np.random.choice(impact_category_options, num_responses),
}

df = pd.DataFrame(data)
df.to_csv('data/pseudo_survey_data.csv', index=False)