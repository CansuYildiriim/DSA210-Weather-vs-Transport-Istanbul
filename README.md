# Understanding the Relationship Between Weather, Major Events, and Public Transportation Usage in Istanbul

## Motivation
I chose this project because I live in Istanbul, and I’ve always noticed how weather and big events can change the way people travel.  
Sometimes on rainy days, buses and metros get extremely crowded, and on football match days it becomes almost impossible to move around the city.  

So, in this project I want to understand **how weather conditions (like temperature, rain, humidity)** and **major events (especially football match days)** affect public transportation usage in Istanbul.  
My goal is to see if there are clear patterns and to visualize them with graphs.

## Research Questions
- How do weather conditions affect how many people use public transport each day?  
- What happens on match days? Do more people use buses and metros, or fewer?  
- Do weather and match days together create an even bigger effect?  
- Are there differences between weekdays and weekends?

## Data Sources
- **Weather Data:** Daily temperature, rainfall, and humidity values from the Turkish State Meteorological Service (MGM).  
- **Transportation Data:** Daily passenger counts from the IETT Open Data Portal.  
- **Major Events Data:** Dates of big football matches in Istanbul from the Turkish Football Federation (TFF).  
  - For each date, I will mark 1 if there is a match and 0 if not.

## Data Columns
| Column | Meaning |
|--------|----------|
| `date` | Date of observation |
| `temperature` | Average daily temperature in °C |
| `rain` | Total rainfall in mm |
| `passenger_count` | Number of passengers (from IETT) |
| `is_match_day` | 1 if there was a football match that day, 0 otherwise |

## Method
1. Collect and clean the data (fix missing or strange values).  
2. Add the match-day column.  
3. Use graphs to show how passenger numbers change with rain or temperature.  
4. Compare match days vs non-match days.  
5. Try to see combined effects, like rainy match days.

## What I Expect to Find
I think rainy days and match days will both increase the number of people using public transport.  
I also expect that on sunny match days, people might prefer walking or driving, so the pattern could change.  
By the end, I want to have some simple graphs showing these relationships clearly.

## Tools I Plan to Use
- Python  
- pandas, numpy  
- matplotlib, seaborn  
- maybe scikit-learn later for a simple prediction test

