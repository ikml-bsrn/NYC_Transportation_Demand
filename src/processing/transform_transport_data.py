

def filter_by_date(df, column_name, year, month):
    """
    This module filters the DataFrame by year and month.

    Args:
        DataFrame (Pandas DataFrame): Pandas DataFrame which contains a DateTime column.
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

### FHV DF

def transform_fhv_df(df):
    fhs_code = {'HV0002':'Juno', 'HV0003':'Uber', 'HV0004':'Via', 'HV0005':'Lyft'}

    # creating a new column for For-Hire Services
    df['service_provider'] = df['hvfhs_license_num'].replace(fhs_code)

    # removing unnecessary columns
    df.drop(columns=['hvfhs_license_num',
                            'dispatching_base_num','originating_base_num',
                            'shared_request_flag','shared_match_flag','access_a_ride_flag',
                            'wav_request_flag','wav_match_flag','DOLocationID','on_scene_datetime','dropoff_datetime','trip_miles','trip_time',
                            'base_passenger_fare','tolls','bcf','sales_tax','tips','driver_pay','airport_fee','congestion_surcharge'
                            ], 
                            inplace=True)

    df.rename(columns={'pickup_datetime':'transit_timestamp',
                                'PULocationID':'LocationID'
                                },
                    inplace=True)
    
    # creating 'waiting_time' feature
    df['waiting_time'] = df['transit_timestamp'].dt.minute - df['request_datetime'].dt.minute
    
    # dropping 'request_datetime' as we don't need it anymore
    df.drop(columns=['request_datetime'],inplace=True)

    return df

### TAXI DF

def transform_taxi_df(df):
    df['service_provider'] = 'Taxi' # to fill in the 'service_provider' before joining with the FHV df
    df['waiting_time'] = 0.0 # since there is no waiting time for taxis, we will fill it as 0

    df.rename(columns=
                        {'tpep_pickup_datetime':'transit_timestamp',
                        'PULocationID':'LocationID'
                        }, 
                        inplace=True)

    df.drop(columns=['VendorID','passenger_count','store_and_fwd_flag',
                            'Airport_fee','improvement_surcharge','tolls_amount','tip_amount','mta_tax',
                            'payment_type','DOLocationID','RatecodeID','trip_distance','tpep_dropoff_datetime',
                            'fare_amount','total_amount','extra','congestion_surcharge'
                            ], inplace=True)
    
    return df

def create_trips_df(df1, df2):
    """
    Joins the taxi and FHV dataframes into one, called trips_df.

    Args:
        df1 (pd.DataFrame): DataFrame for Taxi data.
        df2 (pd.DataFrame): DataFrame for FHV data.
    
    Returns:
        pd.DataFrame or None: Trip data (taxi and FHV joined) if successful, else None. 
    """

    try:
        trips_df = df1.merge(df2, how='outer', on=[
            'transit_timestamp','service_provider','LocationID', 'waiting_time'
            ])
        
        return trips_df
    except Exception as e:
        print(f"Unable to create trips_df: {e}")