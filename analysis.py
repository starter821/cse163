"""
Sunghee Park, Eunji Shin, Sooho Park
CSE 163 AF
03 - 13 - 2023

This file contains the data processing and cleaning up the data, and code
we used to create the visualization for our research questions and analysis. 
"""

import pandas as pd
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go

from matplotlib import pyplot as plt
from plotly.subplots import make_subplots

import question1

gun_violence_df = pd.read_csv('cse163/incident.csv')
unemployment_df = pd.read_csv('cse163/unemployment_rate_data.csv')
violent_crime_df = pd.read_csv('cse163/state_crime.csv')

# year, month, and day from unemployment dataframe
unemployment_df['year'] = pd.DatetimeIndex(unemployment_df['date']).year
unemployment_df['month'] = pd.DatetimeIndex(unemployment_df['date']).month
unemployment_df['day'] = pd.DatetimeIndex(unemployment_df['date']).day

# year, month, and day from gun_violence_df violence dataframe
gun_violence_df['year'] = pd.DatetimeIndex(gun_violence_df['Incident_Date']).year
gun_violence_df['month'] = pd.DatetimeIndex(gun_violence_df['Incident_Date']).month
gun_violence_df['day'] = pd.DatetimeIndex(gun_violence_df['Incident_Date']).day

def main():
    question1.gun_and_unemployment(gun_violence_df, unemployment_df)





if __name__ == '__main__':
    main()


# main
# question1.function(dataframe)
# question2.function(dataframe)
# question3.function(dataframe)


