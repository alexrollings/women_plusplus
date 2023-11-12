import numpy as np
import pandas as pd

def calculateImpactScore(applicants: int, spaces: int, participants: int, \
                        female_participants: int, mentors: int, sponsors: int, \
                        community_partners: int, cost: int, resource_cost: int, \
                        survey_score: float) -> float:
    
    # "Ideal" scores --> these will normalise the individual components of the impact score 
    applicants_per_space = 5
    participants_per_space = 0.95
    participants_per_mentor = 10
    perc_women = 0.8
    spaces_div_sponsors = 20
    spaces_div_community_partners = 10
    ideal_survey_score = 5
    cost_per_participant = 50

    n_KPIs = 8

    # Now that the numbers are on a similar scale (such that none individually biases the score),
    # Take an average and multiple by 10, so that if you meet all your targets, you get a score of 10
    impact_score = ((applicants/spaces) / applicants_per_space \
        + (participants/spaces) / participants_per_space \
        + (female_participants/participants) / perc_women \
        + (participants/mentors) / participants_per_mentor \
        + (spaces/sponsors) / spaces_div_sponsors \
        + (spaces/community_partners) / spaces_div_community_partners \
        + survey_score/ideal_survey_score \
        + (participants/(cost+resource_cost)) / cost_per_participant)/n_KPIs * 10

    return impact_score


average_hourly_rate = int(round(10400 / (40 * (52/12)))) # average monthly salary / (working hours per week * average weeks per month)  
impact_scores_dict = {}

# Hackathon

eventbrite_df_h = pd.read_csv("data/Hackathon_EventBrite.csv")

# Company data
applicants_h = 300
spaces_h = 120
mentors_h = 20
sponsors_h = 5
community_partners_h = 10
cost_h = 10000 # (funding expenditure - income, e.g. from tickets)
resource_hours_h = 200

# Often workers are volunteers, but we multiple by the average hourly rate in Switzerland to get a sense of the value of the work
resource_cost_h = resource_hours_h * average_hourly_rate 

# Eventbrite data
participants_h = eventbrite_df_h.checked_in.astype("bool").sum()
female_participants_h = eventbrite_df_h[eventbrite_df_h.gender=='Female'].checked_in.astype("bool").sum()

# Survey data
survey_df_h = pd.read_csv("data/Hackathon_survey.csv")
survey_score_h = round(survey_df_h.impact.mean(), 1)

impact_score_h = calculateImpactScore(applicants_h, spaces_h, participants_h, female_participants_h, mentors_h, sponsors_h, community_partners_h, cost_h, resource_cost_h, survey_score_h)
print(impact_score_h)
impact_scores_dict["Hackathon"] = impact_score_h

# Workshop

eventbrite_df_w = pd.read_csv("data/Workshop_EventBrite.csv")

# Company data
applicants_w = 25
spaces_w = 30
mentors_w = 1
sponsors_w = 1
community_partners_w = 1
cost_w = 5000 # (funding expenditure - income, e.g. from tickets)
resource_hours_w = 20

# Often workers are volunteers, but we multiple by the average hourly rate in Switzerland to get a sense of the value of the work
average_hourly_rate = int(round(10400 / (40 * (52/12)))) # average monthly salary / (working hours per week * average weeks per month)  
resource_cost_w = resource_hours_w * average_hourly_rate 

# Eventbrite data
participants_w = eventbrite_df_w.checked_in.astype("bool").sum()
female_participants_w = eventbrite_df_w[eventbrite_df_w.gender=='Female'].checked_in.astype("bool").sum()

# Survey data
survey_df_w = pd.read_csv("data/Workshop_survey.csv")
survey_score_w = round(survey_df_w.impact.mean(), 1)

impact_score_w = calculateImpactScore(applicants_w, spaces_w, participants_w, female_participants_w, mentors_w, sponsors_w, community_partners_w, cost_w, resource_cost_w, survey_score_w)
print(impact_score_w)
impact_scores_dict["Workshop"] = impact_score_w
 

# Talk 

eventbrite_df_w = pd.read_csv("data/Talk_EventBrite.csv")

# Company data
applicants_w = 56
spaces_w = 100
mentors_w = 1
sponsors_w = 1
community_partners_w = 2
cost_w = 5000 # (funding expenditure - income, e.g. from tickets)
resource_hours_w = 100 

# Often workers are volunteers, but we multiple by the average hourly rate in Switzerland to get a sense of the value of the work
average_hourly_rate = int(round(10400 / (40 * (52/12)))) # average monthly salary / (working hours per week * average weeks per month)  
resource_cost_w = resource_hours_w * average_hourly_rate 

# Eventbrite data
participants_w = eventbrite_df_w.checked_in.astype("bool").sum()
female_participants_w = eventbrite_df_w[eventbrite_df_w.gender=='Female'].checked_in.astype("bool").sum()

# Survey data
survey_df_w = pd.read_csv("data/Talk_survey.csv")
survey_score_w = round(survey_df_w.impact.mean(), 1)

impact_score_w = calculateImpactScore(applicants_w, spaces_w, participants_w, female_participants_w, mentors_w, sponsors_w, community_partners_w, cost_w, resource_cost_w, survey_score_w)
print(impact_score_w)
impact_scores_dict["Talk"] = impact_score_w

import json

# Save the dictionary to a JSON file
with open('data/impact_scores.json', 'w') as f:
    json.dump(impact_scores_dict, f)