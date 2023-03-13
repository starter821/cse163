# Analyzing the relationships between gun violence, violent crimes, and unemployment rate

### Authors: Eunji Shin, Sunghee Park, Sooho Park

## Files 

main: *analysis.py;* <br />
Data cleaning: *question1.py, question2.py, question3.py;* <br />
Testing: *q1_test.py, q2_test.py, q3_test.py;* <br />
Original datasets: *incident.csv, state_crime.csv, unemployment_rate_data.csv;* <br />
Testing datasets: *test_gun_violence.csv, test_crime_dataset.csv, test_unemployment.csv*

Analysis.py includes all visulizations. There are 3 differnt interactive charts.
questionX.py files are for cleaning and organizing the original datasets. The new datasets are imported by Analysis.py. <br />
qx_test.py files are for testing our codes. 



## Instruction
### Analysis.py
Analysis.py is our main .py files which includes all of our visualizations.
This would be the only code that user will run, unless they want to test our code using qx_text.py files.

Question1: As users run the codes, the html will pop up.
           The chart includes slider which user can set the range of the period with. <br />
Question2: As users run the codes, the html will pop up.
           Users can choose either 'Safest' or 'Most dangerous', and it will show the right chart. <br />
Question3: As users run the code, the search bar is available on console.
           If users put any year between 2015 ~ 2021, the html will pop up and show the right chart.  

### Testing:
qx_test: Using the same code but different datasets, users can check if the code's are working porperly.
 



