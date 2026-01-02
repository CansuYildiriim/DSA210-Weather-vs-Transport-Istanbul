# DSA 210: Understanding the Relationship Between Weather, Football Matches, and Public Transportation Usage in Istanbul

## Motivation

I chose this project because I live in Istanbul and experience daily how external factors shape urban mobility. Weather conditions such as temperature and rainfall often change commuting behavior, while major football matches significantly alter traffic patterns around the city. On rainy days, public transportation tends to become more crowded, and on derby match days, mobility in certain districts becomes extremely constrained.

The motivation of this project is to systematically analyze how weather conditions and football match days affect public transportation usage in Istanbul, and to determine whether these factors provide measurable predictive value.

---

## Research Questions

This project focuses on the following research questions:

- How does daily weather (temperature, precipitation, humidity) affect public transport usage in Istanbul?
- Is there a measurable difference in ridership on football match days?
- Do weather conditions and match days jointly amplify or dampen transportation demand?
- Can simple machine learning models improve predictions compared to a naïve baseline?
- Which features appear to be the most influential drivers of daily ridership?

---

## Data Sources

This study integrates three independent datasets:

### Weather Data
- Source: Open-Meteo API  
- Website: https://open-meteo.com  
- Granularity: Hourly data aggregated to daily level  
- Variables: Temperature, precipitation, humidity, wind speed, visibility  

### Public Transportation Data
- Source: Istanbul Metropolitan Municipality Open Data Portal (İBB Açık Veri)  
- Website: https://data.ibb.gov.tr  
- Dataset: İETT Passenger Transitions (Hourly)  
- Description: Hourly passenger transitions across bus, metrobus, tram, and rail systems  
- Scale: Tens of millions of records aggregated into daily totals  

### Football Match Data
- Source: Official match schedules  
- Reference: Turkish Football Federation (TFF) – https://www.tff.org  
- Scope: Major Istanbul derby matches  
- Processing: Match dates converted into a binary match-day indicator  

---

## Data Preparation and Structure

### Transportation Data
- High-frequency transaction data required chunk-wise reading for memory efficiency.
- Passenger counts were aggregated into a single daily total ridership time series.
- Invalid or malformed timestamps were removed.

### Weather Data
- Hourly weather observations were aggregated to daily averages or sums.
- Dates were normalized to align with transportation data.

### Match Data
- Match dates were extracted from an Excel file.
- All match days were encoded as a binary categorical variable.

### Merging Strategy
- All datasets were merged on a common daily date index.
- Missing values introduced during merging were filled with zeros where appropriate.

---

## Exploratory Data Analysis (EDA)

The exploratory analysis focused on:

- Seasonal and monthly ridership trends
- Daily and hourly usage patterns
- Distribution of weather variables
- Correlations between ridership and environmental factors
- Comparisons between match days and non-match days

Key visualizations included time-series plots, distribution plots, correlation analysis, and aggregated comparisons.

---

## Statistical Analysis (28 November Deliverable)

### Temperature Effect
A two-sample t-test was conducted to evaluate differences in ridership between cold and hot days.

Hypothesis:  
H₀: There is no difference in average daily ridership between cold days (≤ 20°C) and hot days (> 20°C)

Results:
- The p-value was approximately 0.0000, indicating a statistically significant difference.
- Ridership was substantially lower on hot days.
- A moderate negative correlation was observed between temperature and ridership (r ≈ −0.32).

### Precipitation and Match Days
- Precipitation exhibited negligible linear correlation with total daily ridership.
- Match day effects could not be statistically tested earlier due to limited sample size, motivating their inclusion in the machine learning stage.

---

## Machine Learning Analysis (02 January Deliverable)

A daily-level dataset was constructed combining transportation usage, weather variables, and match-day indicators.

### Modeling Approach
- Time-aware train/test split was used.
- A baseline model using historical mean ridership was defined.
- Supervised models included:
  - Linear Regression
  - Ridge Regression
  - Random Forest Regression

### Evaluation
- Models were evaluated on a held-out test period.
- Performance was compared against the baseline predictor.
- Predictions were visualized against actual ridership values.

---

## Key Findings

- Machine learning models outperform the baseline predictor.
- Ridge Regression provides stable improvements with low variance.
- Random Forest captures nonlinear patterns but tends to smooth extreme peaks.
- Match-day indicators show limited standalone predictive power due to sparse events.
- Temperature consistently appears as the most influential feature.

---

## Limitations

- Limited number of match days restricts statistical power.
- Holidays, strikes, and special events are not included.
- Lagged behavioral effects are not modeled.
- Results reflect aggregate city-wide behavior rather than line-level dynamics.

---

## Next Steps

Potential future improvements include:
- Expanding match and event datasets
- Adding public holiday indicators
- Incorporating lag features
- Extending the historical time window
- Performing district-level or line-level modeling

---

## Repository Structure

```├── notebooks/
│   └── EDA_Submission.ipynb
├── data/
│   ├── cleaned_data/
│   │   └── transport_clean_full.csv
│   ├── open-meteo-41.00N28.94E32m.csv
│   └── Book1.xlsx
├── src/
├── requirements.txt
└── README.md 






