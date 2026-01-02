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

├── notebooks/
│   └── EDA_Submission.ipynb
├── data/
│   ├── cleaned_data/
│   │   └── transport_clean_full.csv
│   ├── open-meteo-41.00N28.94E32m.csv
│   └── Book1.xlsx
├── src/
├── requirements.txt
└── README.md




# DSA 210: Understanding the Relationship Between Weather, Major Events, and Public Transportation Usage in Istanbul

## Motivation
I chose this project because I live in Istanbul, and I’ve always noticed how weather and big events can change the way people travel.
Sometimes on rainy days, buses and metros get extremely crowded, and on football match days it becomes almost impossible to move around the city.
So, in this project I want to understand how weather conditions (like temperature, rain, humidity) and major events (especially football match days) affect public transportation usage in Istanbul.
My goal is to see if there are clear patterns and to visualize them with graphs.

## Research Questions
How do weather conditions affect how many people use public transport each day?
What happens on match days? Do more people use buses and metros, or fewer?
Do weather and match days together create an even bigger effect?
Are there differences between weekdays and weekends?

## Data Sources
Weather Data: Daily temperature, rainfall, and humidity values from the Turkish State Meteorological Service (MGM).
Transportation Data: Daily passenger counts from the IETT Open Data Portal.
Major Events Data: Dates of big football matches in Istanbul from the Turkish Football Federation (TFF). For each date, I will mark 1 if there is a match and 0 if not.
## 📊 Data Sources

This project uses three different datasets to analyze the relationship between **weather conditions**, **public transportation usage**, and **football match days** in Istanbul.  
Below are the official sources where the datasets were obtained:

---

### 🌦️ Weather Data  
**Source:** Open-Meteo API  
- Website: https://open-meteo.com/en  
- Format: JSON → converted to CSV  
- Parameters used: daily & hourly temperature, humidity, precipitation, wind speed, etc.

---

### 🚌 Public Transportation Data  
**Source:** İBB Açık Veri Portalı (Istanbul Metropolitan Municipality Open Data Platform)  
- Website: https://data.ibb.gov.tr/  
- Dataset: “İETT Yolcu Geçiş Verisi (Saatlik)”  
- Description: Hourly passenger transitions for bus, metrobus, tram, and other transportation lines across Istanbul.

---

### ⚽ Match Day Data  
**Source:** Manually curated fixture list (official match dates)  
- Primary information reference:  
  - Turkish Football Federation (TFF): https://www.tff.org  
  - Karşılaşma tarihleri manually transferred into `matches.csv`.

---


---

### Methodology and Data Structure 

#### 1. Data Structure and Cleaning Methods
| Dataset | Structure | Initial Processing Challenges |
| :--- | :--- | :--- |
| **Transportation** | High Granularity (15M+ transaction rows per year); includes detailed time and passenger counts. | **Memory Management:** Required **chunk-wise reading and aggregation** to process large volume. Data types required explicit conversion to numeric. |
| **Weather** | Hourly/Daily records; includes `temperature_2m (°C)` and `precipitation (mm)`. | **Aggregation:** Hourly data required aggregation (averaging/summing) to match daily time series. |
| **Major Events** | Event dates and times. | **Feature Engineering:** Converted to a **binary (0/1) categorical indicator** (`Match_Day`). |

#### 2. Data Preparation and Normalization
To address the clarity of combining and normalizing methods:
* **Aggregation Method:** A **chunk-wise reading** approach was implemented to aggregate the raw transportation data into a uniform daily time series (`Total_Passengers`).
* **Normalization:** All final time-series dataframes (Transport, Weather, Match Day) were **normalized to a uniform daily date (`YYYY-MM-DD`) granularity** before being merged using the common date key.
* **Missing Value Imputation:** Missing values resulting from the merge (e.g., non-match days) were imputed with zero.

#### 3. Statistical Methods (Clarification)
To clearly define the statistical methods used:
* **Exploratory Analysis:** **Pearson's Correlation Coefficient** will be used to measure the linear strength and direction between continuous variables (e.g., Temperature vs. Ridership).
* **Hypothesis Testing:** A **Two-Sample T-Test** was executed to determine if the difference between the mean ridership of two categorical groups (Cold vs. Hot Days) is statistically significant.
    * **Tested Hypothesis:** $H_0$: There is no statistically significant difference in the average daily ridership between Cold Days ($\le 20^\circ C$) and Hot Days ($> 20^\circ C$).

---

### Initial Findings (Completed 28 Nov Deliverable)

#### 1. Temperature Effect (Statistically Confirmed)
The analysis yielded clear evidence of the temperature's significant impact:
* **T-Test Result:** The Two-Sample T-Test resulted in a **P-value of $0.0000$**, which is highly significant. This led to the **rejection of the Null Hypothesis** ($H_0$), proving that the difference in ridership between hot and cold days is **statistically significant**.
* **Ridership Gap:** Ridership is substantially lower on hot days (Avg. 1.9M) compared to cold days (Avg. 3.6M).
* **Correlation:** Ridership exhibited a **moderate negative correlation** ($r \approx -0.32$) with average daily temperature. 

#### 2. Precipitation and Events
* **Precipitation:** Precipitation showed a negligible correlation ($r \approx -0.02$), suggesting little linear impact on total daily ridership in this dataset.
* **Match Days:** The effect of Match Days could not be statistically tested due to insufficient data points within the current time frame.

---

## What I Expect to Find
I think rainy days and match days will both increase the number of people using public transport.
I also expect that on sunny match days, people might prefer walking or driving, so the pattern could change.
By the end, I want to have some simple graphs showing these relationships clearly.

### Next Step (02 Jan Deliverable)
The prepared and validated `df_final` dataset will be used to apply **Machine Learning methods** for forecasting future ridership based on environmental conditions.

