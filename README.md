# NYC Transportation Demand Prediction

This project aims to develop a machine learning model to predict transportation demands in New York City based on geographic zones. The transportation includes **taxis**, **for-hire vehicles** (FHV) (i.e., Uber, Lyft, etc.), **buses** and **subways**. By analysing factors such as weather conditions, traffic disruptions, and events, the model aims to provide accurate forecasts to improve transportation efficiency.

## Project Details
### Problem Statement

The demand for taxi and ride-hailing services is influenced by various ever-changing factors such as weather, road-related incidents and conditions (including route alternatives), and nearby events (Liu et al., 2020). According to Lepage and Morency (2020), weather, activities and service disruptions deeply impact demands of these modes of transportation. In order to support commuters in using these services and maximise profits, taxi and ride-hailing companies must be strategic in allocating vehicles and anticipate demand fluctuations. With proper forecasting, prediction and planning, commuters are more likely to opt for taxis and ride-hailing as they become more reliable and convenient for them.

### Objectives
- To build a predictive system which forecasts zone-based taxi and ride-hailing demand in New York City, leveraging real-time data on weather conditions, traffic disruptions, and local events.
- To develop (and deploy) an interactive dashboard that provides actionable insights on current and upcoming high-demand zones, enabling better fleet allocation and operational planning for transportation providers.

### Tech Stack
- **Languages & Libraries**: Python, Pandas, NumPy, Scikit-learn, XGBoost, Statsmodels
- **Data Sources**: NYC TLC, Open-Meteo API, NYC OpenData, Eventbrite API, NYS 511 (traffic & events)
- **Visualisation & Dashboarding**: Streamlit
- **Pipeline & Automation**: Jupyter, Python Scripts, (optionally) Airflow or Prefect
- **Deployment (Optional)**: AWS


 # Data Pipeline Design 
 Updated: 16/6/2025

![image](https://github.com/user-attachments/assets/011fc3a7-4716-4126-aace-37d4899cd55a)



