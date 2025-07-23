

def filterByDate(df, column_name, year, month):
    """
    This module filters the DataFrame by year and month.

    Args:
        df (Pandas DataFrame): Pandas DataFrame which contains a DateTime column.
        column_name (Datetime): Name of column to be filtered.
        Year (int): The targeted year.
        Month (int): The targeted month.

    Returns:
        DataFrame if successful, else None.
    """
    
    try:
        df = df.loc[
            (df[column_name].dt.year == year) &
            (df[column_name].dt.month == month)
        ]

        return df
    
    except Exception as e:
        print(f"Unable to filter by year and month: {e}")

        return None
    

def splitDateTime(df, column_name):
    """
    This module splits DateTime series in a DataFrame into 'date', 'hour' and 'day of week' separately. 

    Args:
        df (Pandas DataFrame): Pandas DataFrame which contains a DateTime column.
        column_name (Datetime): Name of DateTime column.

    Returns:
        DataFrame if successful, else None.
    """
    import pandas as pd

    try:
        # ensure column is in DateTime format
        df[column_name] = pd.to_datetime(df[column_name])

        df['hour'] = df[column_name].dt.hour # hour
        df['day_of_week'] = df[column_name].dt.dayofweek # day of week
        df['date'] = pd.to_datetime(df[column_name].dt.date) # date

        return df
    
    except Exception as e:
        print(f"Unable to split DateTime column: {e}")

### FHV DF

def transformFHV(df):
    """
    This module transforms the FHV dataset to ensure consistency with other datasets prior to data aggregation.

    Args:
        DataFrame (Pandas DataFrame): Pandas DataFrame which contains FHV data.

    Returns:
        DataFrame if successful, else None.
    """
    import pandas as pd
    
    # filter by year and month
    df = filterByDate(df,'request_datetime', 2024, 12)

    # creating a new column for For-Hire Services
    fhs_code = {'HV0002':'Juno', 'HV0003':'Uber', 'HV0004':'Via', 'HV0005':'Lyft'}

    df['service_provider'] = df['hvfhs_license_num'].replace(fhs_code)

    # removing irrelevant columns
    df = df.drop(columns=['hvfhs_license_num',
                            'dispatching_base_num','originating_base_num',
                            'shared_request_flag','shared_match_flag','access_a_ride_flag',
                            'wav_request_flag','wav_match_flag','DOLocationID','on_scene_datetime','dropoff_datetime','trip_miles','trip_time',
                            'base_passenger_fare','tolls','bcf','sales_tax','tips','driver_pay','airport_fee','congestion_surcharge'
                            ])

    df = df.rename(columns={'pickup_datetime':'transit_timestamp',
                                'PULocationID':'LocationID'
                                })

    # splitting datetime format into 'date' and 'hour'
    df = splitDateTime(df, 'transit_timestamp')
    
    # dropping unnecessary columns
    df.drop(columns=['request_datetime', 'transit_timestamp'],inplace=True)

    # ensure LocationID is string/object type (for merging with subway/bus datasets)
    df['LocationID'] = df['LocationID'].astype('object')

    return df

### TAXI DF

def transformTaxi(df):
    """
    This module transforms the Taxi dataset to ensure consistency with other datasets prior to data aggregation.

    Args:
        DataFrame (Pandas DataFrame): Pandas DataFrame which contains Weather data.

    Returns:
        DataFrame if successful, else None.
    """
    import pandas as pd

    # filter by year and month
    df = filterByDate(df,'tpep_pickup_datetime', 2024, 12)

    df['service_provider'] = 'Taxi' # to fill in the 'service_provider' before joining with the FHV df

    # splitting datetime format into 'date' and 'hour'
    df = splitDateTime(df, 'tpep_pickup_datetime')

    df = df.rename(columns={'PULocationID':'LocationID'})

    df = df.drop(columns=['tpep_pickup_datetime','VendorID','passenger_count','store_and_fwd_flag',
                            'Airport_fee','improvement_surcharge','tolls_amount','tip_amount','mta_tax',
                            'payment_type','DOLocationID','RatecodeID','trip_distance','tpep_dropoff_datetime',
                            'fare_amount','total_amount','extra','congestion_surcharge'
                            ])
    
    # ensure LocationID is string/object type (for merging with subway/bus datasets)
    df['LocationID'] = df['LocationID'].astype('object')
    
    return df

## BUS_DF
def transformBus(df):
    """
    This module transforms the Bus ridership dataset to ensure consistency with other datasets prior to data aggregation.

    Args:
        DataFrame (Pandas DataFrame): Pandas DataFrame which contains Bus data.

    Returns:
        DataFrame if successful, else None.
    """
    import pandas as pd

    # splitting datetime format into 'date' and 'hour'
    df = splitDateTime(df, 'transit_timestamp')

    df = df.drop(columns=['fare_class_category', 'transfers', 'payment_method','transit_timestamp'])

    df = df.groupby(['date', 'hour', 'day_of_week', 'bus_route']).sum('ridership').reset_index()

    df.rename(
        columns={'ridership':'demand','bus_route':'LocationID'},
        inplace=True
        )

    df['service_provider'] = 'Bus'
    
    return df

## SUBWAY_DF
def transformSubway(df):
    """
    This module transforms the Subway ridership dataset to ensure consistency with other datasets prior to data aggregation.

    Args:
        DataFrame (Pandas DataFrame): Pandas DataFrame which contains Subway data.

    Returns:
        DataFrame if successful, else None.
    """
    import pandas as pd

    # splitting datetime format into 'date' and 'hour'
    df = splitDateTime(df, 'transit_timestamp')

    df = df.drop(columns=['fare_class_category', 'transfers', 'latitude','longitude','payment_method','transit_timestamp',
                                        'station_complex', 'borough', 'Georeference'])

    df = df.groupby(['date', 'hour', 'day_of_week', 'station_complex_id']).sum('ridership').reset_index()

    df.rename(
        columns={'ridership':'demand', 
                'transit_mode':'service_provider',
                'station_complex_id':'LocationID'},
        inplace=True
        )

    df['LocationID'] = df['LocationID'].astype('category')
        
    df['service_provider'] = 'Subway'
    
    return df

## HOURLY_WEATHER DF

def transformWeatherData(df):
    """
    This module transforms the Weather dataset to ensure consistency with other datasets prior to data aggregation.

    Args:
        DataFrame (Pandas DataFrame): Pandas DataFrame which contains Weather data.

    Returns:
        DataFrame if successful, else None.
    """
    import pandas as pd

    # decoding WMO interpretation codes (WW)
    weather_codes = {
        0: 'clear',
        1: 'mainly_clear',
        2: 'partly_cloudy',
        3: 'overcast',
        45: 'fog',
        48: 'depositing_rime_fog',
        51: 'light_drizzle',
        53: 'moderate_drizzle',
        55: 'dense_drizzle',
        56: 'freezing_light_drizzle',
        57: 'freezing_dense_drizzle',
        61: 'slight_rain',
        63: 'moderate_rain',
        65: 'heavy_rain',
        66: 'freezing_light_rain',
        67: 'freezing_heavy_rain',
        71: 'slight_snowfall',
        73: 'moderate_snowfall',
        75: 'heavy_snowfall',
        77: 'snow_grains',
        80: 'slight_rain_showers',
        81: 'moderate_rain_showers',
        82: 'violent_rain_showers',
        85: 'slight_snow_showers',
        86: 'heavy_snow_showers',
        95: 'thunderstorm',
        96: 'thunderstorm_slight_hail',
        99: 'thunderstorm_heavy_hail'
    }

    # map codes into a new column
    df['weather_description'] = df['weather_code'].map(weather_codes)
    df['weather_description'] = df['weather_description'].astype('category') # change type to 'category'

    # Remove timezone for standardisation
    df['date'] = df['date'].dt.tz_convert('UTC').dt.tz_localize(None)

    # split 'datetime' into 'date' and 'hour'
    df['hour'] = df['date'].dt.hour
    df['date'] = pd.to_datetime(df['date'].dt.date)

    return df

## DATA AGGREGATION

def createTripsDF(fhv_df, taxi_df):
    import pandas as pd
    """
    Joins the taxi and FHV dataframes into one, called trips_df.

    Args:
        fhv_df (pd.DataFrame): DataFrame for Taxi data.
        taxi_df (pd.DataFrame): DataFrame for FHV data.
    
    Returns:
        pd.DataFrame or None: Trip data (taxi and FHV joined) if successful, else None. 
    """

    try:
        transport_df = fhv_df.merge(taxi_df, 
                               how='outer', 
                               on=['date','hour','day_of_week','service_provider','LocationID']
                               )

        return transport_df
    
    except Exception as e:
        print(f"Unable to create trips_df: {e}")

def createDemandDF(df):
    """
    Creates a DataFrame which calculates transportation demand by 'date', 'hour', 'service_provider', and 'LocationID'.

    Args:
        df (pd.DataFrame): DataFrame for trips data.
    
    Returns:
        pd.DataFrame or None: Transport demand data if successful, else None. 
    """
    import pandas as pd

    try:
        df = df.groupby(['date','hour','service_provider','day_of_week','LocationID']).size().reset_index(name='demand')
        
        # ensure LocationID is string/object type (for merging with subway/bus datasets)
        df['LocationID'] = df['LocationID'].astype('object')
        
        return df
    
    except Exception as e:
        print(f"Unable to create demand_df: {e}")

# Merge taxi zone data
def mergeTaxiZoneData(demand_df, zone_data):
    """
    Merges taxi zone data with the Demand dataset.

    Args:
        demand_df (pd.DataFrame): DataFrame for Demand data.
        weather_data (pd.DataFrame): DataFrame for Taxi Zone (LocationID) data.
    
    Returns:
        pd.DataFrame or None: Transport demand data if successful, else None. 
    """
    import pandas as pd

    try:
        # Merge datasets
        merged_df = demand_df.merge(
            zone_data[['LocationID', 'Borough', 'Zone', 'service_zone']],
            on=['LocationID'],
            how='left'
        )

        return merged_df
    
    except Exception as e:
        print(f"Unable to merge taxi zone data: {e}")

        return demand_df

# Merge weather data
def mergeWeatherData(demand_df, weather_data):
    """
    Merges weather data with the Demand dataset.

    Args:
        demand_df (pd.DataFrame): DataFrame for Demand data.
        weather_data (pd.DataFrame): DataFrame for Weather data.
    
    Returns:
        pd.DataFrame or None: Transport demand data if successful, else None. 
    """
    import pandas as pd

    try:
        # Merge datasets
        merged_df = demand_df.merge(
            weather_data[['date', 'hour', 'weather_description']],
            on=['date','hour'],
            how='left'
        )

        return merged_df
    
    except Exception as e:
        print(f"Unable to merge weather data: {e}")

        return demand_df
    
# Merge Public Transport data
def mergePublicTransportData(demand_df, bus_df, subway_df):
    """
    Merges Bus and Subway ridership datasets with the Demand dataset.

    Args:
        demand_df (pd.DataFrame): DataFrame for Demand data.
        bus_df (pd.DataFrame): DataFrame for Bus ridership data.
        subway_df (pd.DataFrame): DataFrame for Subway ridership data.
    
    Returns:
        pd.DataFrame or None: Transport demand data if successful, else None. 
    """
    import pandas as pd

    try:
        # Merge bus dataset
        merged_df = demand_df.merge(
            bus_df,
            on=['date','hour','day_of_week', 'service_provider','LocationID','demand'],
            how='outer'
        )

        # Merge subway dataset
        merged_df = merged_df.merge(
            subway_df,
            on=['date','hour','day_of_week','service_provider','LocationID','demand'],
            how='outer'
        )

        return merged_df
    
    except Exception as e:
        print(f"Unable to merge public transport data: {e}")

def transform_to_CityWideDF(df, subway_df, bus_df):
    """
    Transforms Demand DF into city-wide, instead of zone-based, by removing 'LocationID' and merging two other modes of transportation.

    Args:
        df (pd.DataFrame): DataFrame for Demand data.
        subway_df (pd.DataFrame): DataFrame for Subway ridership data.
        bus_df (pd.DataFrame): DataFrame for Bus ridership data.
    
    Returns:
        pd.DataFrame or None: City-wide transport demand data if successful, else None. 
    """
    import pandas as pd
    
    df.drop(columns='LocationID', inplace=True)

    # reaggregates (city-wide) demand without zone-based feature: 'LocationID'
    df = df.groupby(['date','hour','service_provider']).size().reset_index(name='demand')