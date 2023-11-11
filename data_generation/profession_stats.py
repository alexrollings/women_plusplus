import pandas as pd
import numpy as np
from pprint import pprint
import streamlit as st
import plotly.express as px # Interactive plots/visualisations

def extractFormatDataFromExcel(filename: str, sheet_name: str)-> pd.DataFrame:
    # Read in data from excel file
    df_raw = pd.read_excel(filename, sheet_name=sheet_name)

    # Remove empty cells at the top
    df_raw = df_raw.iloc[2:,:]
    df = df_raw.copy()
    # Drop NA columns/rows if all are empty 
    df.dropna(axis = 0, how = 'all', inplace=True)
    df.dropna(axis = 1, how = 'all', inplace=True)
    # Reset index to increase monotonically from 0
    df.reset_index(drop=True, inplace=True)

    # Unnamed: 1 is the column with the profession indexes
    # Unnamed: 2 is the column with the profession names 
    # Unnamed: 3-131 are the columns with the profession stats
    # With year and quarter in the first and second rows
    df.rename(columns={"Unnamed: 1": "Profession Index"}, inplace=True)
    df.rename(columns={"Unnamed: 2": "Profession Name"}, inplace=True)

    # Column 1 - 61 --> profession stats start
    # Drop all rows (after date information) with NA for profession index (white space in Exel)
    df = df[(df['Profession Name'].notna()) | (df.index < 2)].reset_index(drop=True)

    # Fill year columns that are empty with last non NA value
    df.iloc[0][:].ffill(inplace=True)

    # Re-index dataframe so that the profession index is the index
    df.set_index("Profession Index", inplace=True)
    # Drop totals (contain string like "G-S")
    # Ensure column is string type
    # str.contains cannot handle NaN values, so fill them with empty string
    df = df[~df.iloc[:,0].astype(str).fillna('').str.contains("-")]
    # Then remove this column (don't need it anymore, can uniquely identify profession by index)
    # Effectively remove the first column, as the profession indices are now the index
    df = df.iloc[:, 1:]

    # df = df.Year.apply(axis=1, func=lambda x: str(x) + " Q" + str(df.Quarter)))
    # Transpose dataframe so that profession indices are columns
    df = df.transpose()
    # Rename year and quarter columns
    df.rename(columns={"Industries\n Sections and Departments": "Year"}, inplace=True)
    df.rename(columns={np.nan: "Quarter"}, inplace=True)
    # Reformat year and quarter columns ready for datetime conversion
    # Quarterly information mapped to first month in quarter for datetime formatting
    quarter_mapping = {"I": "01", "II": "04", "III": "07", "IV": "10"}
    df.Quarter = df.Quarter.map(quarter_mapping)
    df = df.assign(Period = df.Year.astype(str) + "-" + df.Quarter)
    # Drop year and quarter columns 
    df.drop(["Year", "Quarter"], axis=1, inplace=True)

    # Remove Profession Name row before converting Period to datetime
    # Store information in a dictionary
    reference_df = df.iloc[0:1].T.drop("Period")
    df.drop("Profession Name", axis=0, inplace=True)
    # Convert Period column to datetime type
    df.Period = pd.to_datetime(df.Period, format='%Y-%m')
    # Set Period column as index
    df.set_index("Period", inplace=True)

    return df

if __name__ == "__main__":

    total_df = extractFormatDataFromExcel("./data/profession_stats.xlsx", "Total")
    female_df = extractFormatDataFromExcel("./data/profession_stats.xlsx", "Female")
    male_df = extractFormatDataFromExcel("./data/profession_stats.xlsx", "Male")

    # Dataframe with total number of people in tech and split by gender
    # Tech career indices: 62-63, 71, 72
    # Unfortunately 74 is combined with 73 & 75, so ignore this
    totals_df = pd.DataFrame({"Total": total_df["62-63"] + total_df["71"] + total_df["72"], 
                              "Female": female_df["62-63"] + female_df["71"] + female_df["72"], 
                              "Male": male_df["62-63"] + male_df["71"] + male_df["72"]})
    pprint(totals_df.head())

    # Streamlit app
    st.title("Women++ Challenge App Demo")
    st.header("Tech Employee Statistics in Switzerland")

    # Create sidebar with check box to see df or not
    # Checkbox will be created in main body of page if do not use st.sidebar.xx
    if st.sidebar.checkbox("Show Data"):
        st.subheader("Dataset")
        st.dataframe(data = totals_df) # Display dataframe

    # Create containers laid out as side by side columns
    # Pass either an int (# of cols) or an iter of numbers that specifies the relative widths
    left_col, mid_col, right_col = st.columns([3, 1, 1])

    # Widget: selectbox for gender
    # Widget: small standalone component that provides a specific functionality
    genders = totals_df.columns 
    gender = st.sidebar.selectbox("Choose a gender breakdown", options=genders)
    if gender == "Total":
        reduced_df = totals_df["Total"]
    elif gender == "Female":
        reduced_df = totals_df["Female"]
    else:
        reduced_df = totals_df["Male"]

    fig = px.line(reduced_df, x=reduced_df.index, y=gender, title='Number of employees in Tech over time')
    st.plotly_chart(fig)

    # fig.show()

