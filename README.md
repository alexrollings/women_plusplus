# [Hack n Lead](https://womenplusplus.ch/hacknlead)

## Figma Prototype

Prototype link:  https://www.figma.com/file/t1fVqozFmvs1RQOwPW0JGX/ImpactPulse?type=design&node-id=74%3A465&mode=design&t=GqXwtpQy2mzpS3YU-1

To play prototype: [https://www.figma.com/proto/t1fVqozFmvs1RQOwPW0JGX/ImpactPulse?type=design&node-id=[…]ling=min-zoom&page-id=74%3A465&starting-point-node-id=74%3A466](https://www.figma.com/proto/t1fVqozFmvs1RQOwPW0JGX/ImpactPulse?type=design&node-id=74-466&t=1AlWeOSQdLOzNjJX-0&scaling=min-zoom&page-id=74%3A465&starting-point-node-id=74%3A466)

## Pitch URL

https://docs.google.com/presentation/d/1Dmy3zCvfcVC024HFTLBAfH_hi0lgXUJZLAIr1dLLfFU/edit?usp=sharing

===
### Frontend Built With
Vite.js, React,js, MaterialUI

### Backend Built With
Python, NumPy, Pandas


## Getting Started

### Prerequisites
1 - Clone the repository
```
git clone
```
2 - Install dependencies - Frontend
```
npm install
yarn install
```
3 - Run the project
```
npm run dev
yarn dev
```

## Frontend Description
Our frontend includes the following key features:

-Responsive Design: The app is designed to work seamlessly on a variety of devices and screen sizes, providing a consistent user experience.

-Intuitive Navigation: Users can easily navigate through the app thanks to a clean and intuitive interface. Common actions are easily accessible.

-Real-time Updates: Our app provides real-time updates to ensure users have the latest information without the need for manual refreshing.

-Modular Components: The codebase is organized using a modular component structure, making it easy to understand, extend, and maintain.

## Backend Description

In 'data_generation' directory.

### Data:
* EventBrite: randomly generated. We were not able to connect to the EventBrite API, as our Frontend is not hosted on a URL, but we generated data with the same fields as EventBrite, and the idea would be to pull this data directly from the website.
* Input from NPO: hardcoded.
* Input from post event surveys: randomly generated.
* opendata.swiss for general statistics that help the NPO track wider trends aligned with their goals.

### Analysis:

* We define factors/KPIs that quantify the impact of an event, according to the organisation's goal
* In the case of Women++ these were:
  * Percentage of women attending event
  * Ratio of applicants to spaces (how “popular” your event was)
  * Attendance rate
  * Number of mentors per person
  * Number of community partners, sponsors involved in the event, scaled to the size of the event
  * Cost of the event per participant (cost includes financial and resource cost)
  * Impact score taken from our post-event survey
* We provide impact targets for each of these factors/KPIs (which are customisable, if the NPO wants to set targets themselves)
* The algorithm then gives you single measurement that combines all of these factors/KPIs, by normalising all inputs using the "target" values, then taking an average, and centering the distribution on 10
* If you hit all the targets, you get an impact score of 10!
* You receive a score lower or higher than 10 if you don’t achieve the targets or exceed them, respectively.

## Plan for later stages

-Confiugre API to fetch data from backend/Eventbright API.

-Restructure frontend to include state and state management and to include data mapping and data visualization.

-Include more data points from attendee surverys to better conclude impact of the event.


## Contributors

Alexandra Rollings - Data Scientist - [LinkedIn] (https://www.linkedin.com/in/alex-rollings/)

Angina Herrmann - Product Manager

John Wofford - Full stack Developer - [LinkedIn] (https://www.linkedin.com/in/jonathanbwofford/)

Karina Rojas - Data Scientist - [LinkedIn] (https://www.linkedin.com/in/karina-rojas-olate/)

Rachel Camp - UX/UI Designer
