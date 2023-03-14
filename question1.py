"""
Sunghee Park, Eunji Shin, Sooho Park
CSE 163 AF
03 - 13 - 2023

This file contains the data analysis of our first question, is there a
correlation between national unemployment rate and gun violence from
2014 to 2021? The analysis is represented with an interactive line graph
"""


import pandas as pd
import plotly.graph_objects as go
import numpy as np

from plotly.subplots import make_subplots


def filter_gun_data(gun: pd.DataFrame) -> pd.DataFrame:
    '''
    The method takes in a dataFrame, specifically gun dataframe, and filters
    the dataframe to be used in plotting the charts. It returns the
    filtered dataFrame.
    '''
    # add 'both' column that contains the sum of 'Injured' and 'Killed' column
    gun['both'] = gun['Injured'] + gun['Killed']

    # group them by year & month
    gun2 = gun.groupby(['year', 'month'], as_index=False)['both'].sum()

    # filter dataset from 2014 - 2021
    year_mask = (gun2['year'] >= 2014) & (gun2['year'] <= 2021)
    gun2 = gun2[year_mask]

    # create date column with format of YYYY-MM
    gun2['date'] = gun2['year'].astype(str) + "-" + gun2['month'].astype(str)

    # turn 'date' column into datetime type, format it to yyyy-mm and sort
    gun2['date'] = pd.to_datetime(gun2['date'])
    gun2['date'] = gun2['date'].dt.strftime('%Y-%m')
    gun2 = gun2.sort_values(by=['date'])

    return gun2


def filter_unemployment_data(unemployment: pd.DataFrame) -> pd.DataFrame:
    '''
    The method takes in a dataFrame, specifically unemployment dataFrame,
    and filters it to be used in plotting the charts. It returns the
    filtered dataFrame.
    '''
    # group the dataset by year & month
    unemployment2 = unemployment.groupby(
        ['year', 'month'], as_index=False)['unrate'].mean()

    # filter unemployment from 2014 - 2021
    year_mask = (unemployment2['year'] >= 2014) & (
        unemployment2['year'] <= 2021)
    unemployment2 = unemployment2[year_mask]

    # create date column with format of YYYY-MM
    unemployment2['date'] = unemployment2['year'].astype(
        str) + "-" + unemployment2['month'].astype(str)

    # turn 'date' column into datetime type, format it to yyyy-mm and sort
    unemployment2['date'] = pd.to_datetime(unemployment2['date'])
    unemployment2['date'] = unemployment2['date'].dt.strftime('%Y-%m')
    unemployment2 = unemployment2.sort_values(by=['date'])

    return unemployment2


def gun_and_unemployment_line(gun: pd.DataFrame,
                              unemployment: pd.DataFrame) -> None:
    '''
    This method takes in two dataframes, specifically the gun violence
    and unemployment dataFrame. It then creates the line chart portraying
    the regression of each dataset with a slider that can filter the
    range of years. It returns nothing.
    '''
    gun2 = filter_gun_data(gun)
    unemployment2 = filter_unemployment_data(unemployment)

    # plot the data
    first_line = go.Scatter(
        x=gun2['date'],
        y=gun2['both'],
        name='gun violence')
    second_line = go.Scatter(
        x=unemployment2['date'],
        y=unemployment2['unrate'],
        name='unemployment rate')

    # make subplot for two graphs to be on the same page.
    fig = make_subplots(rows=2, cols=1, x_title='Year', shared_xaxes=True)
    fig.add_trace(first_line, row=1, col=1)
    fig.add_trace(second_line, row=2, col=1)

    # add title and labels
    fig.update_yaxes(title_text="gun violence", row=1, col=1)
    fig.update_yaxes(title_text="unemployment rate", row=2, col=1)
    fig.update_layout(title='Gun Violence vs. Unemployment Rate ')

    # add a slider
    fig.update_layout(
        xaxis=dict(
            rangeslider=dict(
                visible=False
            ),
            type="date"
        ),
        xaxis2_rangeslider_visible=True,
        xaxis2_type="date"
    )
    fig.update_layout({'xaxis2': {'side': 'top'}})

    fig.show()


def gun_and_unemployment_scatter(gun: pd.DataFrame,
                                 unemployment: pd.DataFrame) -> None:
    '''
    This method takes in two dataframes, specifically the gun violence
    and unemployment dataFrame. It then creates a scatter plot portraying
    the correlation between the number of gun violence and the
    unemployment rate. It also creates a drop down menu where
    the user can choose and compare between correlation of them between
    2014 - 2019 and 2014 - 2021
    '''
    # clean and filter data
    unemployment2 = filter_unemployment_data(unemployment)
    gun2 = filter_gun_data(gun)

    # filter unemployment from 2014 - 2019
    year_mask_2019 = (unemployment2['year'] >= 2014) & (
        unemployment2['year'] <= 2019)
    unemployment_2019 = unemployment2[year_mask_2019]

    # unemployment dataset from 2014 - 2021
    unemployment_2021 = unemployment2

    # filter gun_violence from 2014 - 2019
    year_mask_2019 = (gun2['year'] >= 2014) & (gun2['year'] <= 2019)
    gun_2019 = gun2[year_mask_2019]

    # gun dataset from 2014 - 2021
    gun_2021 = gun2

    # join data -- automatically drops na
    data_2019 = gun_2019.merge(unemployment_2019, on=['date', 'year', 'month'])
    data_2021 = gun_2021.merge(unemployment_2021, on=['date', 'year', 'month'])

    # Initialize figure
    fig = go.Figure()

    # Add Traces -- create the scatter plot
    fig.add_trace(
        go.Scatter(x=data_2019['both'],
                   y=data_2019['unrate'],
                   mode='markers',
                   marker=dict(
            color=data_2019['year'],
            colorscale='Viridis',
            showscale=True,
        ),
            showlegend=False,
        )
    )

    fig.add_trace(
        go.Scatter(x=data_2021['both'],
                   y=data_2021['unrate'],
                   mode='markers',
                   marker=dict(
            color=data_2021['year'],
            colorscale='Viridis',
            showscale=True
        ),
            showlegend=False
        )
    )

    # # Calculate the best-fit lines
    z1 = np.polyfit(data_2019['both'], data_2019['unrate'], 1)
    p1 = np.poly1d(z1)

    z2 = np.polyfit(data_2021['both'], data_2021['unrate'], 1)
    p2 = np.poly1d(z2)

    # add best-fit lines
    fig.add_trace(
        go.Scatter(
            x=data_2019['both'],
            y=p1(data_2019['both']),
            name='Trend line 1',
            line=dict(color='black'),
            showlegend=False,
        )
    )

    fig.add_trace(
        go.Scatter(
            x=data_2021['both'],
            y=p2(data_2021['both']),
            name='Trend line 2',
            line=dict(color='black'),
            showlegend=False
        )
    )

    # add title and labels
    fig.update_layout(
        title='Correlation between Gun Violence and Unemployment Rate',
        xaxis=dict(
            title="Number of Gun Violence"
        ),
        yaxis=dict(
            title="Unemployment Rate"
        )
    )

    # add drop down menus
    fig.update_layout(
        updatemenus=[
            dict(
                active=0,
                buttons=list([
                    dict(label="2014 - 2019",
                         method="update",
                         args=[{"visible": [True, False]}]),
                    dict(label="2014 - 2021",
                         method="update",
                         args=[{"visible": [False, True]}]),
                ]),
            )
        ])
    # make the first graph visible as default when first ran
    fig.data[1].visible = False
    fig.data[3].visible = False

    # show the graph
    fig.show()
