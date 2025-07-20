def main():
    from src.data.load_transport_data import loadTaxi, loadFHV, loadBus, loadSubway, loadTaxiZone
    from src.data.load_weather_data import loadWeatherOpenMeteo

    from src.processing.transform_data import filterByDate, transformFHV, transformTaxi, createTripsDF, createDemandDF, transformWeatherData, mergeWeatherData, mergeTaxiZoneData
    from src.processing.clean_data import cleanDataFrame

    ### LOADING DATA

    print("Loading data...")

    # taxi_df
    taxi_df = loadTaxi("https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2024-12.parquet") # taxi trip dataset url
    print("     Taxi data loaded successfully.")

    # fhv_df
    fhv_df = loadFHV("https://d37ci6vzurychx.cloudfront.net/trip-data/fhvhv_tripdata_2024-12.parquet") # FHV trip dataset url
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

    ### TRANSFORMING DATA

    print("Tranforming data...")

    print("     Transforming taxi_df...")
    transformed_taxi_df = transformTaxi(taxi_df)

    print("     Transforming fhv_df...")
    transformed_fhv_df = transformFHV(fhv_df)
    
    print("     Transforming hourly_weather_df...")
    transformed_hourly_weather_df = transformWeatherData(hourly_weather_df)

    ### CLEANING DATA

    print("Cleaning data...")   

    print("     Cleaning taxi_df...")
    cleaned_taxi_df = cleanDataFrame(transformed_taxi_df)

    print("     Cleaning fhv_df...")
    cleaned_fhv_df = cleanDataFrame(transformed_fhv_df)

    print("     Cleaning hourly_weather_df...")
    cleaned_hourly_weather_df = cleanDataFrame(transformed_hourly_weather_df)

    ### DATA AGGREGATION
    print("Aggregating data...")

    # Joining Taxi and FHV
    print("     Joining taxi and FHV datasets...")
    trips_df = createTripsDF(cleaned_fhv_df, cleaned_taxi_df)
    
    # Creating the main dataset 'demand_df' for ML training
    print("     Creating Demand dataset...")
    demand_df = createDemandDF(trips_df)

    # Merge taxi zone data with demand dataset
    #print("     Merging taxi zones...")
    #demand_df = mergeTaxiZoneData(demand_df, zone_df)

    # Merge weather data with demand dataset
    print("     Merging weather data...")
    merged_df = mergeWeatherData(demand_df, cleaned_hourly_weather_df)

    print("Task completed. Dataset saved.")
    
    merged_df.to_csv("/Users/ikmalbasirun/Documents/GitHub/NYC_Transportation_Demand/data/processed/transport_demand_dec2024.csv", index=False)



# initiate script
if __name__ == "__main__":
    main()

