# Understanding the Relationship Between Weather and Public Transportation Usage in Istanbul

## Motivation
This project aims to explore how daily weather conditions such as temperature, precipitation, and humidity affect public transportation usage in Istanbul. Understanding this relationship can help city planners and transportation authorities design more efficient and sustainable systems, especially under changing climate conditions.

## Data Sources
- **IETT Open Data Portal (İstanbul Büyükşehir Belediyesi)**  
  [https://data.ibb.gov.tr](https://data.ibb.gov.tr)  
  Datasets: Daily passenger counts, bus line statistics.

- **Meteorological General Directorate (MGM)**  
  [https://mgm.gov.tr/veridegerlendirme/il-ve-ilceler-istatistik.aspx](https://mgm.gov.tr/veridegerlendirme/il-ve-ilceler-istatistik.aspx)  
  Datasets: Daily temperature, rainfall, humidity data.

- **Additional Enrichment**  
  - Weekend/Weekday flag (from Python datetime)  
  - Holiday information (optional)

## Data Collection Plan
1. Download or access daily passenger count data from IETT’s open data portal.  
2. Collect daily weather information for the same time period from MGM.  
3. Merge both datasets using the “date” column.  
4. Clean and preprocess the data (handle missing values, convert data types).  
5. Add weekday/weekend labels for further analysis.

## Planned Analysis
- Perform **Exploratory Data Analysis (EDA)** to visualize trends.  
- Conduct **correlation analysis** between weather variables and passenger count.  
- Build a **regression model** to predict passenger count based on weather conditions.  
- Visualize findings using Matplotlib and Seaborn.

## Expected Findings
- Increase in public transport usage on rainy days.  
- Decrease during hot or humid weather.  
- Lower passenger counts on weekends compared to weekdays.

## Limitations & Future Work
This analysis is limited to available open data from IETT and MGM.  
Future extensions may include integrating air quality or metro data for a more comprehensive understanding of mobility behavior.

## Reproducibility
Install dependencies:
