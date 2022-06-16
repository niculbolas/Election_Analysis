# Election_Analysis
## Overview of Election Audit:
The purpose of this project was to take election results, given in the form of a CSV file, from the election commission and then using Python code help them determine the voter turnout for all counties, the total number of votes for each candidate, and then determine who won the election.

## Election-Audit Results:
* How many votes were cast in this congressional election?\
From the below screenshot we can see that there were a total of 369,711 votes cast in this election.

* Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.\
Jefferson: 10.5% (38,855 votes)\
Denver: 82.8% (306,055 votes)\
Arapahoe: 6.7% (24,801 votes)

* Which county had the largest number of votes?\
Denver had the most votes at a total of 306,055 or 82.8% of the total votes.

* Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.\
Charles Casper Stockham: 23% (85,213 votes)\
Diana DeGette: 73.8% (306,055 votes)\
Raymon Anthony Doane: 3.1% (11,606 votes)

* Which candidate won the election, what was their vote count, and what was their percentage of the total votes?\
The winner of the election was Diana DeGette with 272,892 votes which was 73.8% of the 369,711 total votes.

### Election-Audit Results Screenshot:
![Election Results](https://github.com/niculbolas/Election_Analysis/blob/main/Analysis/election_results_screenshot.png?raw=true)

## Election-Audit Summary:
The code used to do this analysis could be used to analyze other elections as well, but there are some recommendations for changes I would make first.
* Firstly, I would recommend changing the code so that the user can specify which CSV file they want to read and get results for.  This way, the code is more flexible rather than relying on a file being named something specific in a specific location.
* Secondly, I would recommend updating the code so that the user is prompted what they would like to call the output text file.  Otherwise, if someone ran multiple elections through the code now it would overwrite the results each time!  Or if not prompt the user for a name, at least check to see if the output would overwrite an existing file and if so name the new file something else like election_results001.
