def main():
    from src.data.load_transport_data import loadTaxi, loadFHV, loadBus, loadSubway, loadTaxiZone
    from src.data.load_weather_data import loadWeatherOpenMeteo

    from src.processing.transform_data import filterByDate, transformFHV, transformTaxi, transformBus, transformSubway, createTripsDF, createDemandDF, transformWeatherData, mergeWeatherData, mergePublicTransportData
    from src.processing.clean_data import cleanDataFrame
    from src.visualisations.visualise_data import plot_and_saveBoxplots
    
    import pandas as pd
    import os

    ### LOADING DATA

    print("Loading data...")

    # taxi_df
    #taxi_df = loadTaxi("https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2024-12.parquet") # taxi trip dataset url
    taxi_df = pd.read_parquet("/Users/ikmalbasirun/Documents/GitHub/NYC_Transportation_Demand/data/raw/yellow_tripdata_2024-12.parquet")
    print("     Taxi data loaded successfully.")

    # fhv_df
    #fhv_df = loadFHV("https://d37ci6vzurychx.cloudfront.net/trip-data/fhvhv_tripdata_2024-12.parquet") # FHV trip dataset url
    fhv_df = pd.read_parquet("/Users/ikmalbasirun/Documents/GitHub/NYC_Transportation_Demand/data/raw/fhvhv_tripdata_2024-12.parquet")
    print("     FHV data loaded successfully.")

    # subway_df
    subway_df = loadSubway()
    print("     Subway data loaded successfully.")
    
    # bus_df
    bus_df = loadBus()
    print("     Bus data loaded successfully.")

    # weather_df                      #lat     #lon      #start date   #end date
    hourly_weather_df = loadWeatherOpenMeteo(40.7143, -74.006, "2024-12-01", "2025-01-01")
    print("     Weather data loaded successfully.")

    # taxi_zone_df
    zone_df = loadTaxiZone()
    print("     Taxi zone data loaded successfully.")

    ### CLEANING DATA

    print("Cleaning data...")

    # TAXI
    print("     Cleaning taxi_df...")
    # plot_and_saveBoxplots(
    #     taxi_df,
    #     base_dir="/Users/ikmalbasirun/Documents/GitHub/NYC_Transportation_Demand/data/processed/visualisations",
    #     folder_name="taxi_outliers",
    #     fig_version="before"
    #     )
    cleaned_taxi_df = cleanDataFrame(taxi_df)
    # plot_and_saveBoxplots(
    #     cleaned_taxi_df,
    #     base_dir="/Users/ikmalbasirun/Documents/GitHub/NYC_Transportation_Demand/data/processed/visualisations",
    #     folder_name="taxi_outliers",
    #     fig_version="after"
    #     )

    # FHV
    print("     Cleaning fhv_df...")

    # plot_and_saveBoxplots(
    #     fhv_df,
    #     base_dir="/Users/ikmalbasirun/Documents/GitHub/NYC_Transportation_Demand/data/processed/visualisations",
    #     folder_name="fhv_outliers",
    #     fig_version="before"
    #     )
    cleaned_fhv_df = cleanDataFrame(fhv_df)
    # plot_and_saveBoxplots(
    #     cleaned_fhv_df,
    #     base_dir="/Users/ikmalbasirun/Documents/GitHub/NYC_Transportation_Demand/data/processed/visualisations",
    #     folder_name="fhv_outliers",
    #     fig_version="after"
    #     )

    # BUS
    print("     Cleaning bus_df...")

    # plot_and_saveBoxplots(
    #     bus_df,
    #     base_dir="/Users/ikmalbasirun/Documents/GitHub/NYC_Transportation_Demand/data/processed/visualisations",
    #     folder_name="bus_outliers",
    #     fig_version="before"
    #     )
    cleaned_bus_df = cleanDataFrame(bus_df)
    print(cleaned_bus_df.head(10))
    # plot_and_saveBoxplots(
    #     cleaned_bus_df,
    #     base_dir="/Users/ikmalbasirun/Documents/GitHub/NYC_Transportation_Demand/data/processed/visualisations",
    #     folder_name="bus_outliers",
    #     fig_version="after"
    #     )

    # SUBWAY
    print("     Cleaning subway_df...")

    # plot_and_saveBoxplots(
    #     subway_df,
    #     base_dir="/Users/ikmalbasirun/Documents/GitHub/NYC_Transportation_Demand/data/processed/visualisations",
    #     folder_name="subway_outliers",
    #     fig_version="before"
    #     )
    cleaned_subway_df = cleanDataFrame(subway_df)
    # plot_and_saveBoxplots(
    #     cleaned_subway_df,
    #     base_dir="/Users/ikmalbasirun/Documents/GitHub/NYC_Transportation_Demand/data/processed/visualisations",
    #     folder_name="subway_outliers",
    #     fig_version="after"
    #     )

    # WEATHER
    print("     Cleaning hourly_weather_df...")
    cleaned_hourly_weather_df = cleanDataFrame(hourly_weather_df)

    ### TRANSFORMING DATA

    print("Tranforming data...")

    print("     Transforming taxi_df...")
    transformed_taxi_df = transformTaxi(cleaned_taxi_df)
    print(transformed_taxi_df.head(10))

    print("     Transforming fhv_df...")
    transformed_fhv_df = transformFHV(cleaned_fhv_df)
    print(transformed_fhv_df.head(10))

    print("     Transforming bus_df...")
    transformed_bus_df = transformBus(cleaned_bus_df)
    print(transformed_bus_df.head(10))
    transformed_bus_df.to_csv("/Users/ikmalbasirun/Documents/GitHub/NYC_Transportation_Demand/data/processed/cleaned_bus_data.csv", index=False)

    print("     Transforming subway_df...")
    transformed_subway_df = transformSubway(cleaned_subway_df)
    print(transformed_subway_df.head(10))
    
    print("     Transforming hourly_weather_df...")
    transformed_hourly_weather_df = transformWeatherData(cleaned_hourly_weather_df)

    ### DATA AGGREGATION
    print("Aggregating data...")

    # Joining Taxi and FHV
    print("     Joining taxi and FHV datasets...")
    trips_df = createTripsDF(transformed_taxi_df, transformed_fhv_df)
    
    # Creating the main dataset 'demand_df' for ML training
    print("     Creating Demand dataset...")
    demand_df = createDemandDF(trips_df)

    # Merge taxi zone data with demand dataset
    #print("     Merging taxi zones...")
    #demand_df = mergeTaxiZoneData(demand_df, zone_df)

    # Join public transport data with demand dataset
    print("     Joining public transportation (bus and subway) datasets...")
    demand_df_with_publicTransport = mergePublicTransportData(demand_df, transformed_bus_df, transformed_subway_df)

    # Merge weather data with demand dataset
    print("     Merging weather data...")
    final_df = mergeWeatherData(demand_df_with_publicTransport, transformed_hourly_weather_df)

    print("Task completed. Dataset saved.")
    
    final_df.to_csv("/Users/ikmalbasirun/Documents/GitHub/NYC_Transportation_Demand/data/processed/demand_dec2024_withWeather.csv", index=False)

# initiate script
if __name__ == "__main__":
    main()

