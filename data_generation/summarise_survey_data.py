import numpy as np
import pandas as pd

def generateGaussianData(mu: float, sigma: float, low: int, high: int)-> int:
    # Generate numbers from a Gaussian distribution
    data = np.random.normal(mu, sigma)
    data = np.round(np.clip(data, low, high)).astype(int)  # ensure values are between 1 and 5
    return data 

survey_df = pd.read_csv("data/pseudo_survey_data.csv")
eventbrite_df = pd.read_csv("data/pseudo_eventbrite_data.csv")
n_attendees = eventbrite_df.checked_in.sum()
n_companies = generateGaussianData(5, 2, 1, 10) # To be input by NPO --> sponsoring/partnering/both?
resources_hours = generateGaussianData(50, 20, 10, 200) # To be input by NPO
cost = generateGaussianData(25000, 10000, 1000, 50000) # To be input by NPO
categories_dict = survey_df.impact_category_attendee.value_counts().to_dict()
impact_score = round(survey_df.impact_score_attendee.mean(), 1)

print(f"Resource hours: {resources_hours}")
print(f"Event cost (CHF): {cost}")
print(f"Number of attendees: {n_attendees}")
print(f"Number of companies sponsoring: {n_companies}")
print(categories_dict)
print(f"Impact score: {impact_score}")
