def cleanDataFrame(df):
    import pandas as pd
    """
    Cleans data from a DataFrame by removing duplicates,

    Args:
        df (pd.DataFrame): A DataFrame required to clean its data.

    Return:
        pd.DataFrame or None: DataFrame with duplicates removed, 
    """
    # checking duplicates
    print("     Checking duplicates...")
    duplicate = df.duplicated()
    if True in duplicate:
        df = df.drop_duplicates()
        print("       Duplicates found and removed.")
    else:
        print("       No duplicates found.")

    # analysing and handling missing values
    print("     Analysing missing values...")
    missing_df = df.isna().sum()

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

    # handling outliers
    print("     Handling outliers using IQR method...")
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns

    for col in numeric_cols:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR

        if IQR == 0:
            print(f"         Skipped outlier check for '{col}' (IQR=0).")
            continue
        else:
            original_len = len(df)
            df = df[(df[col] >= lower_bound) & (df[col] <= upper_bound)]
            removed = original_len - len(df)

            if removed > 0:
                print(f"         Removed {removed} outliers from '{col}'.")
            else:
                print(f"         No outliers detected in '{col}'.")
    
    return df