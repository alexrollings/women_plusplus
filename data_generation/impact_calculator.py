import numpy as np

# Company data
# Outputs
applicants = 300
spaces = 120
mentors = 20
sponsors = 5
community_partners = 10
# Inputs 
cost = 10000 # (funding expenditure - income, e.g. from tickets)
resource_hours = 200
# Often workers are volunteers, but we multiple by the average hourly rate in Switzerland to get a sense of the value of the work
average_hourly_rate = int(round(10400 / (40 * (52/12)))) # average monthly salary / (working hours per week * average weeks per month)  
resource_cost = resource_hours * average_hourly_rate 

# Eventbrite data
# Outputs 
participants = 500
female_participants = 400
nationalities = 30

# Survey data
# Outputs 
survey_score = 4.5

# "Ideal" scores --> these will normalise the individual components of the impact score 
applicants_per_space = 2
participants_per_space = 0.95
participants_per_mentor = 10
perc_women = 0.8
spaces_div_sponsors = 20
spaces_div_community_partners = 10
ideal_survey_score = 5
cost_per_participant = 200

n_KPIs = 8

# Now that the numbers are on a similar scale (such that none individually biases the score),
# Take an average and multiple by 10, so that if you meet all your targets, you get a score of 10
impact_score = (spaces/applicants * applicants_per_space \
    + spaces/participants * participants_per_space \
    + participants/female_participants * perc_women \
    + mentors/participants * participants_per_mentor \
    + sponsors/spaces * spaces_div_sponsors \
    + community_partners/spaces * spaces_div_community_partners \
    + survey_score/ideal_survey_score \
    + (participants/(cost+resource_cost)) * cost_per_participant)/n_KPIs * 10
 
print(impact_score)

