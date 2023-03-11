"""
Sunghee Park, Eunji Shin, Sooho Park
CSE 163 AF
03 - 13 - 2023

This file contains the data analysis of our first question, is there a
correlation between national unemployment rate and gun violence from
2014 to 2021? The analysis is represented with an interactive line graph

"""


import math

import pandas as pd
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go

from matplotlib import pyplot as plt
from plotly.subplots import make_subplots


gun = pd.read_csv('cse163/incident.csv')
unemployment = pd.read_csv('cse163/unemployment_rate_data.csv')

# year, month, and day from unemployment dataframe
unemployment['year'] = pd.DatetimeIndex(unemployment['date']).year
unemployment['month'] = pd.DatetimeIndex(unemployment['date']).month
unemployment['day'] = pd.DatetimeIndex(unemployment['date']).day

# year, month, and day from gun violence dataframe
gun['year'] = pd.DatetimeIndex(gun['Incident_Date']).year
gun['month'] = pd.DatetimeIndex(gun['Incident_Date']).month
gun['day'] = pd.DatetimeIndex(gun['Incident_Date']).day


def gun_and_unemployment(gun: pd.DataFrame, unemployment: pd.DataFrame) -> None:
    '''
    This method takes in two dataframes, secifically the gun violence dataset
    and unemployment dataset. It then cre
    '''
    # add 'both' column that contains the sum of 'Injured' and 'Killed' column
    gun['both'] = gun['Injured'] + gun['Killed']

    # group them by year & month
    gun2 = gun.groupby(['year', 'month'], as_index=False)['both'].sum()
    unemployment2 = unemployment.groupby(
        ['year', 'month'], as_index=False)['unrate'].mean()

    # filter unemployment from 2014 - 2021
    year_mask = (unemployment2['year'] >= 2014) & (
        unemployment2['year'] <= 2021)
    unemployment2 = unemployment2[year_mask]

    # filter gun_violence from 2014 - 2021
    year_mask = (gun2['year'] >= 2014) & (gun2['year'] <= 2021)
    gun2 = gun2[year_mask]

    # create date column with format of YYYY-MM
    gun2['date'] = gun2['year'].astype(str) + "-" + gun2['month'].astype(str)
    unemployment2['date'] = unemployment2['year'].astype(
        str) + "-" + unemployment2['month'].astype(str)

    # plot the data
    first_line = go.Scatter(
        x=gun2['date'], y=gun2['both'], name='gun violence')
    second_line = go.Scatter(
        x=unemployment2['date'], y=unemployment2['unrate'], name='unemployment rate')

    fig = make_subplots(rows=2, cols=1, x_title='Year', shared_xaxes=True)
    fig.add_trace(first_line, row=1, col=1)
    fig.add_trace(second_line, row=2, col=1)
    fig.update_yaxes(title_text="sum of gun violence", row=1, col=1)
    fig.update_yaxes(title_text="total unemployment rate", row=2, col=1)
    fig.update_layout(title='Gun Violence vs. Unemployment Rate ')

    # add a slider
    fig.update_layout(
        xaxis=dict(
            rangeslider=dict(
                visible=False
            ),
            type="category"
        ),
        xaxis2_rangeslider_visible=True,
        xaxis2_type="category"
    )
    fig.update_layout({'xaxis2': {'side': 'top'}})

    fig.show()