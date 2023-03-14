"""
Sunghee Park, Eunji Shin, Sooho Park
CSE 163 AF
03 - 13 - 2023

This file contains the data analysis of our second question, What are the 5 most
dangerous and safest states based on the total number of incidents
(gun violence and violent crime cases) per population in 2018?
The analysis is represented with an interactive bar chart.
"""


import pandas as pd
import seaborn as sns
import plotly.graph_objs as go

sns.set()

state_dict = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY'
}


def convert_state(state_name):
    return state_dict.get(state_name)


def gun_and_crime(gun_violence_df: pd.DataFrame, violent_crime_df: pd.DataFrame) -> None:
    # filter both dataframe so it only contains data in 2018
    gun_violence_year = gun_violence_df['year'] == 2018
    violent_crime_year = violent_crime_df['Year'] == 2018

    # take only necessary columns
    gun_violence_df = gun_violence_df[gun_violence_year]
    gun_violence_df = gun_violence_df.groupby(
        'State_Code')[['Killed', 'Injured']].sum()
    gun_violence_df['gun_total'] = gun_violence_df['Killed'] + \
        gun_violence_df['Injured']
    gun_violence = gun_violence_df.loc[:, ['gun_total']]
    print("Gun violence dataset:")
    print(gun_violence)

    violent_crime_df = violent_crime_df[violent_crime_year]
    violent_crime_df = violent_crime_df.loc[:, [
        'State', 'Data.Population', 'Data.Totals.Violent.All']]
    violent_crime_df['State'] = violent_crime_df['State'].apply(convert_state)
    violent_crime = violent_crime_df.dropna()
    print("Violent crime dataset:")
    print(violent_crime)

    crime_gun_merged = violent_crime.merge(
        gun_violence, left_on='State', right_on='State_Code')
    crime_gun_merged['Total'] = crime_gun_merged['gun_total'] + \
        crime_gun_merged['Data.Totals.Violent.All']
    crime_gun_merged['Total_per_capita'] = \
        crime_gun_merged['Total'] / crime_gun_merged['Data.Population']
    print("Merged dataset:")
    print(crime_gun_merged)

    # Define a dictionary that maps the options to the corresponding top 5 data frames
    data_frames = {
        'Safest': crime_gun_merged.nsmallest(5, 'Total_per_capita'),
        'Most Dangerous': crime_gun_merged.nlargest(5, 'Total_per_capita')
    }

    # Define the initial data frame to display
    current_df = data_frames['Safest']

    # Define the layout for the interactive bar chart
    layout = go.Layout(
        title='Top 5 Safest or Most Dangerous States',
        xaxis=dict(title='State'),
        yaxis=dict(title='Total Incidents per population'),
        updatemenus=[
            dict(
                buttons=list([
                    dict(
                        label='Safest',
                        method='update',
                        args=[{'y': [current_df['Total_per_capita']],
                              'x': [current_df['State']],
                               'type': 'bar',
                               'name': 'Total Incidents'}]),
                    dict(
                        label='Most Dangerous',
                        method='update',
                        args=[{'y': [data_frames['Most Dangerous']['Total_per_capita']],
                              'x': [data_frames['Most Dangerous']['State']],
                               'type': 'bar',
                               'name': 'Total Incidents'}])
                ]),
                type='buttons',
                direction='right',
                showactive=True
            )
        ]
    )

    # Define the initial trace for the interactive bar chart
    trace = go.Bar(
        x=current_df['State'],
        y=current_df['Total_per_capita'],
        name='Total Incidents'
    )

    # Create the figure for the interactive bar chart
    fig = go.Figure(data=[trace], layout=layout)

    # Display the interactive bar chart
    fig.show()


def main():
    
    gun_violence_df = pd.read_csv('https://raw.githubusercontent.com/starter821/cse163/main/datasets/test_gun_violence.csv')
    violent_crime_df = pd.read_csv('https://raw.githubusercontent.com/starter821/cse163/main/datasets/test_crime_dataset.csv')

    # year, month, and day from gun_violence_df violence dataframe
    gun_violence_df['year'] = pd.DatetimeIndex(
        gun_violence_df['Incident_Date']).year
    gun_violence_df['month'] = pd.DatetimeIndex(
        gun_violence_df['Incident_Date']).month
    gun_violence_df['day'] = pd.DatetimeIndex(
        gun_violence_df['Incident_Date']).day
    
    gun_and_crime(gun_violence_df, violent_crime_df)


if __name__ == '__main__':
    main()