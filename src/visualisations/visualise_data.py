import matplotlib.pyplot as plt
import seaborn as sns
import os

def plot_and_saveBoxplots(df, base_dir, folder_name, fig_version):
    """
    Saves and displays boxplots of all numerical columns in the given DataFrame into a subfolder.

    Args:
        df (pd.DataFrame): Input DataFrame
        base_dir (str): Base directory where folders will be created
        folder_name (str): Name of the subfolder for this DataFrame
        fig_version (str): Name of version of the Boxplot (eg, "before_cleaning").
    """
    # creates a subfolder to store boxplot figures for the selected DataFrame
    output_dir = os.path.join(base_dir, folder_name)
    os.makedirs(output_dir, exist_ok=True)

    numeric_cols = df.select_dtypes(include=['int64','float64']).columns

    for col in numeric_cols:
        plt.figure(figsize=(6, 2.5))

        sns.boxplot(x=df[col], color='skyblue')

        plt.title(f'Boxplot for {col}')
        plt.xlabel(col)
        plt.tight_layout()

        output_path = os.path.join(output_dir, f"{col}_boxplot_{fig_version}.png")
        plt.savefig(output_path, format='png')
        
        plt.show()
        plt.close()