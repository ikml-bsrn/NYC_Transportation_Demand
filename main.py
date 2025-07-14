from src.data.load_transport_data import load_taxi, load_fhv
from src.processing.transform_transport_data import filter_by_date, transform_fhv_df, transform_taxi_df, create_trips_df

def main():

    ### TAXI

    # loading taxi_df
    print("Loading taxi data...")
    taxi_df = load_taxi()

    # transforming taxi_df
    if taxi_df is not None:
        # Filter by date
        print("Filtering taxi_df by date...")
        filter_by_date(taxi_df,'tpep_pickup_datetime', 2024, 12)

        print("Cleaning taxi_df...")
        transformed_taxi_df = transform_taxi_df(taxi_df)

        print("Saving taxi_df as CSV...")
        transformed_taxi_df.to_csv("data/processed/cleaned_taxi_dec2024.csv", index=False)
    else:
        print("Taxi data not loaded.")

    ### FHV

    # loading fhv_df
    print("Loading FHV data...")
    fhv_df = load_fhv()

    # transforming taxi_df
    if fhv_df is not None:
        # Filter by date
        print("Filtering fhv_df by date...")
        filter_by_date(fhv_df,'request_datetime', 2024, 12)

        print("Cleaning fhv_df...")
        transformed_fhv_df = transform_fhv_df(fhv_df)

        print("Saving fhv_df as CSV...")
        transformed_fhv_df.to_csv("data/processed/cleaned_fhv_dec2024.csv", index=False)
    else:
        print("FHV data not loaded.")

    ### TRIPS DF
    
    # Joining taxi and FHV dataframes
    if (transformed_taxi_df is not None) and (transform_fhv_df is not None):

        print("Creating trips_df...")
        trips_df = create_trips_df(transform_fhv_df, transformed_taxi_df)

        print("Saving trips_df as CSV...")
        trips_df.to_csv("data/processed/trips_dec2024.csv", index=False)
    else:
        print("Trips dataframe not created.")


if __name__ == "__main__":
    main()

