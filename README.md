AQI Analysis of India (2015–2020)

Project Overview

This project focuses on analysing the Air Quality Index (AQI) across different cities in India using Python. It explores air pollution patterns, pollutant levels, city-wise AQI differences and yearly trends through data analysis and visualization.

Objectives

- Analyse AQI levels across Indian cities.
- Study major air pollutants such as PM2.5, PM10, NO2, SO2 and CO.
- Identify cities with higher average AQI.
- Examine yearly AQI trends from 2015 to 2020.
- Detect outliers and understand AQI category distributions.
- Create an interactive dashboard and an India choropleth map.
- Generate an AI-assisted policy brief with recommendations.

Dataset

Source: "Air Quality Data in India (2015–2020) – Kaggle" (https://www.kaggle.com/datasets/rohanrao/air-quality-data-in-india)

- Original dataset: "city_day.csv"
- Cleaned dataset: "cleaned_aqi_data.csv"
- Original dataset contains 29,531 rows and 16 columns.
- Cleaned dataset contains 24,850 records.
- Covers 26 Indian cities.
- Data period: January 2015 to July 2020.

Technologies Used

- Python
- Pandas and NumPy
- Matplotlib and Seaborn
- Plotly
- Dash
- Jupyter Notebook
- Visual Studio Code
- Google Gemini

Project Structure

- "Dashboard/" – Interactive AQI dashboard and choropleth map code.
- "Dataset/" – Original and cleaned CSV datasets.
- "Notebook/" – Data analysis and visualization notebook.
- "Report/" – Detailed project report.
- "India_AQI_Choropleth_Map.html" – Interactive India AQI map.
- "requirements.txt" – Required Python libraries.

Data Analysis and Visualizations

The project includes:

- Top 10 cities with highest average AQI.
- Yearly average AQI trend.
- Pollutant correlation heatmap.
- PM2.5 vs AQI scatter plot.
- AQI outlier detection using the IQR method.
- AQI category distribution.
- Top 5 cities comparison.
- Average pollutant levels.
- AQI distribution histogram.

Interactive Dashboard

A dashboard was developed using Plotly and Dash. It includes:

- City selection dropdown.
- Yearly average AQI trend.
- City-wise average AQI comparison.
- Interactive chart updates based on city selection.

Choropleth Map

An interactive choropleth map of India was created to represent state-wise average AQI levels using geographical visualization.

AI Integration

Google Gemini was used to assist in preparing an AI-generated policy brief based on the project's findings and air pollution analysis.

Key Findings

- Ahmedabad recorded the highest average AQI among the cities in the analysed dataset.
- PM10 showed the highest average concentration among the selected pollutants.
- PM10 and PM2.5 showed strong positive correlations with AQI.
- The yearly average AQI showed a general declining trend from 2015 to 2020. However, 2020 data covers only part of the year.

How to Run the Project

1. Clone or download this repository.
2. Install the required libraries:

pip install -r requirements.txt

3. Run the dashboard from the project root folder:

python Dashboard/app.py

4. Open the local URL displayed in the terminal, usually "http://127.0.0.1:8050/".

5. Open the choropleth HTML file in a web browser to view the interactive map.

Team Members

- Disha Nitran Sundi
- Ankita Pattnayak

Conclusion

This project demonstrates how Python-based data analysis and visualization can help understand air pollution patterns across India. The dashboard and choropleth map provide an interactive way to explore AQI information and support awareness of environmental issues.
