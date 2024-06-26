
import pandas as pd
import numpy as np
import matplotlib as mpl


def read_and_print_csv(file_path):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)

    # Print the first 5 rows of the DataFrame
    print(df.head())


if __name__ == '__main__':
    print("Test")
    # Specify the path to your CSV file
    csv_file_path = 'sample_data.csv'

    # Call the function
    print("Testing a branch")
    read_and_print_csv(csv_file_path)
    print("Testing branch again")
