def cleanDataFrame(df):
    import pandas as pd
    """
    Cleans data from a DataFrame by removing duplicates,

    Args:
        df (pd.DataFrame): A DataFrame required to clean its data.

    Return:
        pd.DataFrame or None: DataFrame with duplicates removed, 
    """
    print("     Checking duplicates...")
    duplicate = df.duplicated()
    if True in duplicate:
        df = df.drop_duplicates()
        print("       Duplicates found and removed.")
    else:
        print("       No duplicates found.")

    print("     Analysing missing values...")
    missing_df = df.isna().sum()

    # analysing and handling missing values
    for column, missing_count in missing_df.items():
        percentage = (missing_count / len(df)) * 100
        print(f"       {column}: {percentage:.0f}%")

        if percentage == 0:
            continue
        elif percentage < 5:
            df = df.dropna(subset=[column])
            print(f"    Rows with missing values in {column} removed.")
        else:
            if type(df[column]) == 'float':
                median = df[column].median()
                df[column].fillna(median, inplace=True)
                print(f"    Missing values in {column} filled with median ({median}).")
            else:
                df[column].fillna("Unknown", inplace=True)
                print(f"    Missing values in {column} filled with 'Unknown'.")

    return df

