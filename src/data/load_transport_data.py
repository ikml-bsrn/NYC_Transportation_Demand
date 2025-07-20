import pandas as pd

def loadTaxi(url):
    """
    Loads the Yellow Taxi trip data for December 2024 from the NYC TLC CloudFront URL.

    Args:
        url (str): URL to retrieve taxi trip data file.

    Returns:
        pd.DataFrame: DataFrame containing the taxi trip data.
    """

    try:
        taxi_df = pd.read_parquet(url)

        return taxi_df
    
    except Exception as e:
        print(f"Unable to load taxi_df from source. Error: {e}")

        return None
    

def loadFHV(url):
    """
    Loads the FHV Taxi trip data for December 2024 from the NYC TLC CloudFront URL.

    Args:
        url (str): URL to retrieve taxi trip data file.

    Returns:
        pd.DataFrame: DataFrame containing the FHV trip data.
    """

    try:
        fhv_df = pd.read_parquet(url)

        return fhv_df
    
    except Exception as e:
        print(f"Unable to load fhv_df from source. Error: {e}")

        return None
    

def loadSubway():
    """
    Loads the Subway Ridership data for December 2024 from the local repository.

    Returns:
        pd.DataFrame: DataFrame containing the subway ridership data.
    """

    path = '/Users/ikmalbasirun/Documents/GitHub/NYC_Transportation_Demand/data/raw/MTA_Subway_Hourly_Ridership__2020-2024_20250415.csv'

    try:
        subway_ridership_df = pd.read_csv(path)

        return subway_ridership_df
    
    except Exception as e:
        print(f"Unable to load subway_ridership_df from source. Error: {e}")

        return None
    

def loadBus():
    """
    Loads the Bus Ridership data for December 2024 from local repository.

    Returns:
        pd.DataFrame: DataFrame containing the subway ridership data.
    """

    path = '/Users/ikmalbasirun/Documents/GitHub/NYC_Transportation_Demand/data/raw/MTA_Bus_Hourly_Ridership__2020-2024_20250415.csv'

    try:
        bus_ridership_df = pd.read_csv(path)

        return bus_ridership_df
    
    except Exception as e:
        print(f"Unable to load bus_ridership_df from source. Error: {e}")

        return None    
    

def loadTaxiZone():
    """
    Loads the taxi zone data for New York City from the NYC TLC. This is important for geospatial context.

    Returns:
        pd.DataFrame: DataFrame containing the NYC taxi zone data.
    """

    url = 'https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv'

    try:
        taxi_zone_df = pd.read_csv(url)

        return taxi_zone_df
    
    except Exception as e:
        print(f"Unable to load taxi_zone_df from source. Error: {e}")

        return None    