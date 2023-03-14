# Analyzing the relationships between gun violence, violent crimes, and unemployment rate
### Authors: Eunji Shin, Sunghee Park, Sooho Park

## Files

**Main**: *analysis.py;* <br />
This module includes all visualizations as it contains 4 different interactive charts.

**Data cleaning**: *question1.py, question2.py, question3.py;* <br />
These files are for cleaning and organizing the original datasets, and also contains all the code needed to generate our charts for each question. All the functions are imported by Analysis.py. <br />

**Testing**: *q1_test.py, q2_test.py, q3_test.py;* <br />
These files are for testing purposes. Each file tests the questionX.py file accordingly with the question number.

### Datasets Folder: <br />
**Original datasets**: <br />
*incident.csv*: US Gun Violence Dataset <br />
*state_crime.csv*: US State Crime Dataset <br />
*unemployment_rate_data.csv*: US Unemployment Data <br />
**Testing datasets**: <br />
*test_gun_violence.csv, test_crime_dataset.csv, test_unemployment.csv*




## Instruction
### Run *Analysis.py*:
Analysis.py is our main .py files which includes all of our visualizations.
This would be the only code that user will run, unless they want to test our code using qx_text.py files.

When you run, first, three charts including line chart, scatter plot, and bar chart are going to pop up. To get the last interactive chart, please go back to the code and look at the console. It will ask for the year you would like to see for pie charts. Input the year and the last chart will pop up. <br />

**Question1**: <br />
As users run the codes, the html will pop up. The chart includes slider which user can set the range of the period with. <br />

**Question2**: <br />
As users run the codes, the html will pop up. Users can choose either 'Safest' or 'Most dangerous', and it will show the right chart. <br />

**Question3**:<br />
As users run the code, the search bar is available on console. If users put any year between 2015 ~ 2021, the html will pop up and show the right chart.  

### Testing:
qx_test: Using the same code but smaller datasets, users can check if the code's are working porperly. You will need to run *each of the testing files* to see our tests.
