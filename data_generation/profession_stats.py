import pandas as pd
import numpy as np
from pprint import pprint
import streamlit as st
import plotly.express as px 
import plotly.graph_objects as go
import plotly.io as pio


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
    totals_df = pd.DataFrame({"Total": total_df["62-63"] + total_df["71"] + total_df["72"] + total_df["73-75"], 
                              "Female": female_df["62-63"] + female_df["71"] + female_df["72"] + female_df["73-75"], 
                              "Male": male_df["62-63"] + male_df["71"] + male_df["72"] + male_df["73-75"]})

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=totals_df.index, y=totals_df.Total, mode=None, fill='tozeroy', line=dict(color='rgb(126, 82, 160)'), name="Total")) # Purple color with 0.5 translucency
    fig.add_trace(go.Scatter(x=totals_df.index, y=totals_df.Female, mode='lines', fill='tozeroy', line=dict(color='rgb(17, 29, 74)', width=4), name="Women")) # Green-blue color and thicker line
    fig.update_layout(
        title_text='Employees in Technical Roles in Switzerland (1991-2023)',
        title_font=dict(size=32), # Change the font size of the title
        legend=dict(x=0.02, y=1, font=dict(size=24)), # Move the legend to the top left corner and change its size
        annotations=[
        dict(
            x=1,
            y=-0.12,
            showarrow=False,
            text="Data source: <a href='https://www.bfs.admin.ch/bfs/de/home/statistiken/kataloge-datenbanken.assetdetail.27165007.html'>https://www.bfs.admin.ch/bfs/de/home/statistiken/kataloge-datenbanken.assetdetail.27165007.html</a>",
            xref="paper",
            yref="paper",
            font=dict(size=14)
        )
    ]
    )
    fig.update_xaxes(tickfont=dict(size=22)) # Change the font size of the x axis labels
    fig.update_yaxes(tickfont=dict(size=22)) # Change the font size of the y axis labels
    fig.show()
    # pio.write_image(fig, 'images/tech_employees.png')

    # Stats for presentation
    perc_women_in_tech = int(round(totals_df["Female"][-1]/totals_df["Total"][-1] * 100))
    print(f"As of June 2023 there are {perc_women_in_tech}% of tech jobs are filled by women, with {int(round(totals_df.Total[-1]))} total tech jobs in Switzerland.")
