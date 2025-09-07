# NYC Transportation Demand Analysis and Forecasting Project

This project aims to develop a fully functional data pipeline using Airflow which informs fleet management in New York City. By the end of this project, it should include ML models which predict transportation demands in New York City based on geographic zones, displayed within a dashboard using Streamlit. Transportation includes **taxis**, **for-hire vehicles** (FHV) (i.e., Uber, Lyft, etc.), **buses** and **subways**. By analysing factors such as weather conditions, traffic disruptions, and events, the model aims to provide accurate forecasts to improve transportation efficiency.

## Current Progress Summary (7/9/2025)
- Pipeline Development: Built a modular Python pipeline to clean, transform, and aggregate large datasets (Yellow Taxi, High-Volume FHV, and subway ridership).
Exploratory Analysis: Conducted demand exploration in Tableau, visualizing weekly, daily, and hourly patterns across modes and zones, and identifying busiest time periods and boroughs.
External Factors: Incorporated weather data (conditions) into the dataset to study its impact on transport demand.
Dashboards: Designed interactive Tableau dashboards for stakeholders to explore multi-modal demand trends across the city.

**Future Directions**:
- Integrate permitted events, and traffic incident data to capture broader contextual demand drivers.
- Apply statistical methods (e.g., regression, hypothesis testing in IBM SPSS) to quantify the effects of weather, events, and traffic on demand patterns.
- Develop forecasting models (time series, machine learning regression, or deep learning) to predict demand and support operational decision-making.
- Deploy an interactive Streamlit dashboard to deliver real-time demand forecasts to stakeholders.

## Project Details

### Problem Statement

The demand for **multi-modal urban transport** (taxis, ride-hailing, buses, and subways) is influenced by dynamic factors such as weather, road incidents, and local events (Liu et al., 2020). Research by Lepage and Morency (2020) highlights that these external conditions significantly impact mode choice and service demand. For transportation providers, accurate forecasting of demand is essential to **allocate fleets efficiently**, **minimise wait times**, and **improve commuter reliability**. A data-driven approach to demand prediction can support more responsive and efficient transportation systems in NYC.


### Objectives
- To develop interactive dashboards that provide actionable insights into past, current, and emerging high-demand zones across multiple transport modes.
- To study the effects of weather, traffic and nearby events on transport demands in NYC.
- To build a predictive system which forecasts zone-based demand in New York City using real-time data on weather, traffic, and events.

### Tech Stack
- **Languages & Libraries**: Python, Pandas, NumPy, Scikit-learn, XGBoost
- **Data Sources**: NYC TLC, Open-Meteo API, NYC OpenData, NYS 511 (traffic & events)
- **Visualisation & Dashboarding**: Tableau, (Streamlit)
- **Pipeline & Automation**: Jupyter, Python Scripts, Airflow

 # Data Pipeline Design 

![image](https://github.com/user-attachments/assets/011fc3a7-4716-4126-aace-37d4899cd55a)

# Dashboards
### [Subway Demands in NYC (Tableau)](https://public.tableau.com/app/profile/muhamad.ikmal.arif.ahmad.basirun/viz/TransportDemandSeparateDatasets_17534557826470/SubwayDashboard)
<img width="2394" height="1236" alt="image" src="https://github.com/user-attachments/assets/5ebbd9c5-1401-490e-8902-f51a7eaaece9" />

The dashboard above highlights demand hotspots across multiple time periods (weekly, daily, and hourly), supporting more effective scheduling and resource allocation. Users can interactively explore hourly and daily demand patterns for each subway station, compare across modes of transport, and filter by location or timeframe to uncover actionable insights. To explore, visit this [link](https://public.tableau.com/app/profile/muhamad.ikmal.arif.ahmad.basirun/viz/TransportDemandSeparateDatasets_17534557826470/SubwayDashboard) on my public Tableau page.

### [Taxi & For-hire Vehicles (FHV) Demands in NYC](https://public.tableau.com/app/profile/muhamad.ikmal.arif.ahmad.basirun/viz/TaxiFHVDemandsinNYC/TaxiFHVDashboard)
<img width="1597" height="810" alt="image" src="https://github.com/user-attachments/assets/89bbb006-4978-46c2-9444-b7de64c6b197" />

This dashboard visualises demand trends for NYC taxis and for-hire vehicles (e.g., Uber, Lyft) across different boroughs, zones and time periods (weekly, daily, and hourly). It enables users to identify high-demand zones, analyse peak periods, and compare demand between service types, supporting more efficient fleet allocation and operational planning. To explore, visit this [link](https://public.tableau.com/app/profile/muhamad.ikmal.arif.ahmad.basirun/viz/TaxiFHVDemandsinNYC/TaxiFHVDashboard) on my public Tableau page.





