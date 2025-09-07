# NYC Transportation Demand Prediction

This project aims to develop a fully functional data pipeline using Airflow which informs fleet management in New York City. By the end of this project, it should include an ML model which predicts transportation demands in New York City based on geographic zones, displayed within a dashboard using Streamlit. Transportation includes **taxis**, **for-hire vehicles** (FHV) (i.e., Uber, Lyft, etc.), **buses** and **subways**. By analysing factors such as weather conditions, traffic disruptions, and events, the model aims to provide accurate forecasts to improve transportation efficiency.

## Project Details
### Problem Statement

The demand for taxi and ride-hailing services is influenced by various ever-changing factors such as weather, road-related incidents and conditions (including route alternatives), and nearby events (Liu et al., 2020). According to Lepage and Morency (2020), weather, activities and service disruptions deeply impact demands of these modes of transportation. In order to support commuters in using these services and maximise profits, taxi and ride-hailing companies must be strategic in allocating vehicles and anticipate demand fluctuations. With proper forecasting, prediction and planning, commuters are more likely to opt for taxis and ride-hailing as they become more reliable and convenient for them.

### Objectives
- To build a predictive system which forecasts zone-based taxi and ride-hailing demand in New York City, leveraging real-time data on weather conditions, traffic disruptions, and local events.
- To develop interactive dashboards which provides actionable insights on current and upcoming high-demand zones, enabling better fleet allocation and operational planning for transportation providers.

### Tech Stack
- **Languages & Libraries**: Python, Pandas, NumPy, Scikit-learn, XGBoost
- **Data Sources**: NYC TLC, Open-Meteo API, NYC OpenData, NYS 511 (traffic & events)
- **Visualisation & Dashboarding**: Tableau, (Streamlit)
- **Pipeline & Automation**: Jupyter, Python Scripts, Airflow

 # Data Pipeline Design 
 Updated: 16/6/2025

![image](https://github.com/user-attachments/assets/011fc3a7-4716-4126-aace-37d4899cd55a)

# Dashboards
### [Subway Demands in NYC (Tableau)](https://public.tableau.com/app/profile/muhamad.ikmal.arif.ahmad.basirun/viz/TransportDemandSeparateDatasets_17534557826470/SubwayDashboard)
<img width="2394" height="1236" alt="image" src="https://github.com/user-attachments/assets/5ebbd9c5-1401-490e-8902-f51a7eaaece9" />

The dashboard above highlights demand hotspots across multiple time periods (weekly, daily, and hourly), supporting more effective scheduling and resource allocation. Users can interactively explore hourly and daily demand patterns for each subway station, compare across modes of transport, and filter by location or timeframe to uncover actionable insights. To explore, visit this [link](https://public.tableau.com/app/profile/muhamad.ikmal.arif.ahmad.basirun/viz/TransportDemandSeparateDatasets_17534557826470/SubwayDashboard) on my public Tableau page.

### [Taxi & For-hire Vehicles (FHV) Demands in NYC](https://public.tableau.com/app/profile/muhamad.ikmal.arif.ahmad.basirun/viz/TaxiFHVDemandsinNYC/TaxiFHVDashboard)
<img width="1597" height="810" alt="image" src="https://github.com/user-attachments/assets/89bbb006-4978-46c2-9444-b7de64c6b197" />

This dashboard visualises demand trends for NYC taxis and for-hire vehicles (e.g., Uber, Lyft) across different boroughs, zones and time periods (weekly, daily, and hourly). It enables users to identify high-demand zones, analyse peak periods, and compare demand between service types, supporting more efficient fleet allocation and operational planning. To explore, visit this [link](https://public.tableau.com/app/profile/muhamad.ikmal.arif.ahmad.basirun/viz/TaxiFHVDemandsinNYC/TaxiFHVDashboard) on my public Tableau page.





