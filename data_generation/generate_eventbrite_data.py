import pandas as pd
import numpy as np
from faker import Faker

fake = Faker('de_CH')

# Define the number of responses
num_responses = 200 

# Define a list of technical job titles
tech_jobs = ['Software Engineer', 'Data Scientist', 'IT Consultant', 'Systems Analyst', 'Network Administrator', 'Full Stack Developer', 'UX/UI Designer', 'Front End Developer', 'Marketing and Communications Expert', 'Post Doctoral Researcher']

# Generate pseudo data
data = {
    # 'profile': [fake.simple_profile() for _ in range(num_responses)],
    # 'profile_name': [fake.name() for _ in range(num_responses)],
    # 'profile_email': [fake.email() for _ in range(num_responses)],
    'job_title': np.random.choice(tech_jobs, num_responses),
    'age': np.random.choice(tech_jobs, num_responses),
    'checked_in': np.random.choice([True, False], num_responses, p=[0.8, 0.2]),
    'cancelled': np.random.choice([True, False], num_responses, p=[0.8, 0.2]),
    'refunded': np.random.choice([True, False], num_responses, p=[0.8, 0.2]),
    'affiliate': [fake.company() for _ in range(num_responses)],
    # 'event_id': [fake.random_int(min=1000, max=9999) for _ in range(num_responses)],
    # 'order_id': [fake.random_int(min=1000, max=9999) for _ in range(num_responses)]
}

df = pd.DataFrame(data)
df.to_csv('data/pseudo_eventbrite_data.csv', index=False)