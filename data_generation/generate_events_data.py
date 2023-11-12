from faker import Faker
import pandas as pd
import numpy as np


#***********************************
#   Mock Data for Hackaton
#***********************************

# Create a Faker instance with the 'en_US' locale for English names
fake = Faker('en_US')

# Set a seed for reproducibility
Faker.seed(0)

# Set the number of responses
num_responses = 200

# Generate fake data for a DataFrame with a bias towards female names
gender_choices = ['Male'] * int(num_responses * 0.15) + ['Female'] * int(num_responses * 0.85)
np.random.shuffle(gender_choices)

# Common domain for emails
common_domain = 'example.com'

# Get a list of nationalities (simplified for illustration purposes)
nationalities = ['American', 'British', 'Canadian', 'Australian', 'French', 'German', 'Italian', 'Japanese', 'Chinese']

df = pd.DataFrame({
    'profile_name': [fake.first_name_male() if gender == 'Male' else fake.first_name_female() for gender in gender_choices],
    'profile_email': [f"{name.lower()}@{common_domain}" for name in df['profile_name']],
    'gender': gender_choices,
    'nationality': np.random.choice(nationalities, num_responses),
    'job_title': np.random.choice(tech_jobs, num_responses),
    'checked_in': np.random.choice([True, False], num_responses, p=[0.95, 0.05]),
})

path='/hacknlead/'
df.to_csv(path+'Hackathon.csv')

#***********************************
#   Mock Data for Workshop
#***********************************

# Create a Faker instance with the 'en_US' locale for English names
fake = Faker('en_US')

# Set a seed for reproducibility
Faker.seed(0)

# Set the number of responses
num_responses = 30

# Generate fake data for a DataFrame with a bias towards female names
gender_choices = ['Male'] * int(num_responses * 0.2) + ['Female'] * int(num_responses * 0.80)
np.random.shuffle(gender_choices)

# Common domain for emails
common_domain = 'example.com'

# Get a list of nationalities (simplified for illustration purposes)
nationalities = ['American', 'British', 'Canadian', 'Australian', 'French', 'German', 'Italian', 'Japanese', 'Chinese']

df = pd.DataFrame({
    'profile_name': [fake.first_name_male() if gender == 'Male' else fake.first_name_female() for gender in gender_choices],
    'profile_email': [f"{name.lower()}@{common_domain}" for name in df['profile_name']],
    'gender': gender_choices,
    'nationality': np.random.choice(nationalities, num_responses),
    'job_title': np.random.choice(tech_jobs, num_responses),
    'checked_in': np.random.choice([True, False], num_responses, p=[0.8, 0.2]),
})

df.to_csv(path+'Workshop.csv')

#***********************************
#   Mock Data for Talk-Networking
#***********************************

# Create a Faker instance with the 'en_US' locale for English names
fake = Faker('en_US')

# Set a seed for reproducibility
Faker.seed(2)

# Set the number of responses
num_responses = 56

# Generate fake data for a DataFrame with a bias towards female names
gender_choices = ['Male'] * int(num_responses * 0.001) + ['Female'] * int(num_responses * 0.99)
num_responses = len(gender_choices)
np.random.shuffle(gender_choices)

# Common domain for emails
common_domain = 'example.com'

# Get a list of nationalities (simplified for illustration purposes)
nationalities = ['Swiss','American', 'British', 'Canadian', 'Australian', 'French', 'German', 'Italian', 'Japanese', 'Chinese']

df = pd.DataFrame({
    'profile_name': [fake.first_name_male() if gender == 'Male' else fake.first_name_female() for gender in gender_choices],
    'profile_email': [f"{name.lower()}@{common_domain}" for name in df['profile_name']],
    'gender': gender_choices,
    'nationality': np.random.choice(nationalities, num_responses),
    'job_title': np.random.choice(tech_jobs, num_responses),
    'checked_in': np.random.choice([True, False], num_responses, p=[0.7, 0.3]),
})

df.to_csv(path+'Talk-networking.csv')

#***********************************
#   Mock Survey Data for Hackathon
#***********************************

hack = pd.read_csv(path+'Hackathon.csv')
hs = hack[hack['checked_in']==True].sample(frac=0.4, random_state=42)

custom_distribution = np.concatenate([np.random.randint(1, 4, size=int(len(hs) * 0.2)),np.random.randint(4, 6, size=int(len(hs) * 0.8))])
custom_distribution=np.append(custom_distribution, 5)
hs['impact'] = custom_distribution # Random integers between 1 and 5
hs['Job search'] = np.random.choice([0, 1], size=len(hs))
hs['networking'] = np.random.choice([0, 1], size=len(hs))
hs['Career Progression'] = np.random.choice([0, 1], size=len(hs))
hs['Upskilling'] = np.random.choice([0, 1], size=len(hs))
hs=hs[['profile_name','impact','Job search','networking','Career Progression','Upskilling']]

hs.to_csv(path+'Hackaton_survey.csv')

#***********************************
#   Mock Survey Data for Workshop
#***********************************

work = pd.read_csv(path+'Workshop.csv')
df = work[work['checked_in']==True].sample(frac=0.7, random_state=42)

custom_distribution = np.concatenate([np.random.randint(1, 4, size=int(len(df) * 0.2)),np.random.randint(4, 6, size=int(len(df) * 0.8))])
custom_distribution=np.append(custom_distribution, 5)
df['impact'] = custom_distribution # Random integers between 1 and 5
df['Job search'] = np.random.choice([0, 1], size=len(df))
df['networking'] = np.random.choice([0, 1], size=len(df))
df['Career Progression'] = np.random.choice([0, 1], size=len(df))
df['Upskilling'] = np.random.choice([0, 1], size=len(df))
df=df[['profile_name','impact','Job search','networking','Career Progression','Upskilling']]

df.to_csv(path+'Workshop_survey.csv')

#******************************************
#   Mock Survey Data for Talk-Networking
#******************************************

work = pd.read_csv(path+'Talk-networking.csv')
df = work[work['checked_in']==True].sample(frac=0.55, random_state=42)
custom_distribution = np.concatenate([np.random.randint(1, 4, size=int(len(df) * 0.2)),np.random.randint(4, 6, size=int(len(df) * 0.8))])
custom_distribution=np.append(custom_distribution, 5)
df['impact'] = custom_distribution # Random integers between 1 and 5
df['Job search'] = np.random.choice([0, 1], size=len(df))
df['networking'] = np.random.choice([0, 1], size=len(df))
df['Career Progression'] = np.random.choice([0, 1], size=len(df))
df['Upskilling'] = np.random.choice([0, 1], size=len(df))
df=df[['profile_name','impact','Job search','networking','Career Progression','Upskilling']]
df.to_csv(path+'Talk_survey.csv')
