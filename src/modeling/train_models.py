def trainModel_ZoneBased(df):
    from sklearn.model_selection import train_test_split

    # split train test
    X_train, X_test, y_train, y_test = train_test_split(df, test_size=0.3, random_state=42)

    


def trainModel_CityWide(df):
    pass