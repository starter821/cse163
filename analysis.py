"""
Sunghee Park, Eunji Shin, Sooho Park
CSE 163 AF
03 - 13 - 2023

This file contains the data processing and cleaning up the data, and code
we used to create the visualization for our research questions and analysis. 
"""

import pandas as pd

from question1 import gun_and_unemployment
from question2 import gun_and_crime
from question3 import create_pie_chart

gun_violence_df = pd.read_csv('cse163/incident.csv')
unemployment_df = pd.read_csv('cse163/unemployment_rate_data.csv')
violent_crime_df = pd.read_csv('cse163/state_crime.csv')

# year, month, and day from unemployment dataframe
unemployment_df['year'] = pd.DatetimeIndex(unemployment_df['date']).year
unemployment_df['month'] = pd.DatetimeIndex(unemployment_df['date']).month
unemployment_df['day'] = pd.DatetimeIndex(unemployment_df['date']).day

# year, month, and day from gun_violence_df violence dataframe
gun_violence_df['year'] = pd.DatetimeIndex(
    gun_violence_df['Incident_Date']).year
gun_violence_df['month'] = pd.DatetimeIndex(
    gun_violence_df['Incident_Date']).month
gun_violence_df['day'] = pd.DatetimeIndex(gun_violence_df['Incident_Date']).day


def main():
    # Quesiton 1
    gun_and_unemployment(gun_violence_df, unemployment_df)

    # Question 2
    gun_and_crime(gun_violence_df, violent_crime_df)

    # Question 3
    year_input = input('Enter a year between 2015 and 2021 (or "q" to quit): ')

    if year_input.lower() == 'q':
        print('Program has been shut down :D')

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
                fig = create_pie_chart(gun_violence_df, year)
                fig.show()


if __name__ == '__main__':
    main()
