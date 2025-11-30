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

