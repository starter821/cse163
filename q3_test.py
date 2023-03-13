import pandas as pd
import plotly.express as px

"""
Sunghee Park, Eunji Shin, Sooho Park
CSE 163 AF
03 - 13 - 2023

This file contains the data analysis of our first question, what is the proportion 
of the top 5 states with the highest gun violence to the total number of gun
violence in the United States from 2015 to 2021? The analysis is represented
through interactive pie charts 
"""

import pandas as pd
import plotly.express as px

test_data = pd.read_csv('/Users/soohopark/Desktop/cse163/test_gun_violence.csv')


# Create a pie chart for a given year
def create_pie_chart(data: pd.DataFrame, year: int) -> None:
    # Convert the Incident_Date to a datetime object
    data['Incident_Date'] = pd.to_datetime(data['Incident_Date'])

    # Filter the data from 2015 to 2021
    data = data[(data['Incident_Date'].dt.year >= 2015) &
                (data['Incident_Date'].dt.year <= 2021)]

    # Filter the data by the given year
    filtered_data = data[data['Incident_Date'].dt.year == year]

    # Get the total number of killed and injured cases for each state
    state_totals = filtered_data.groupby(
        'State_Code')[['Killed', 'Injured']].sum()

    # Get the top five states with the most gun violence cases
    top_states = state_totals.sum(axis=1).nlargest(5)

    # Combine all other states as "Other"
    other_states = pd.Series(data=state_totals.sum(axis=1)[~state_totals.sum(
        axis=1).index.isin(top_states.index)].sum(), index=['Other'])

    # Combine the top five states and "Other"
    combined_states = pd.concat([top_states, other_states])

    # Create a pie chart
    fig = px.pie(combined_states, values=combined_states,
                 names=combined_states.index, title=f'Gun Violence Cases by State ({year})')
    return fig


a = True
while a:
    year_input = input('Enter a year between 2015 and 2021 (or "q" to quit): ')

    if year_input.lower() == 'q':
        print('Program has been shut down :D')
        a = False
    # Easter Egg
    elif year_input.lower() == 'go':
        print('Huskies!')
    else:
        if not year_input.isnumeric():
            print('Invalid input. Please enter a valid year (e.g. 2015) or "q" to quit.')
        else:
            year = int(year_input)
            if year < 2015 or year > 2021:
                print('Invalid input. Please enter a year between 2015 and 2021.')
            else:
                fig = create_pie_chart(test_data, year)
                fig.show()
