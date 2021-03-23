# Technical Report

This report contains my implementation/design choice and a time complexity analysis.
It will also explain, how can the implementation by improved.

## Database Design

The database contains only one table and has the same column names as the excel file.
It contains an additional id column which stores the id for the session and the subsession.

## Import Agenda Implementation and Time Complexity

### Implementation

Import Agenda uses a loop to go over all the rows in the excel file, format them and then add it to the dabase. For the id column, every new session is given a new id. If the row is a subsession, then the id of the subsession is same as the parent session.

### Time Complexity

The time complexity is O(nmk), where
n = number of rows in the excel file (this happens in the for loop of the main function)
m = number of columns in the excel file (this happens in the for loop of the formatItem function)
k = length of the string for replace function (this is time complexity of the replace function)
Note that the time complexity of insert function is not added into this time complexity.

## Loop Up Implementation and Time Complexity

### Implementation

Loop up agenda first uses the select function to get rows containing the specific values. This gets the parent sessions. It then uses a for loop to get the id of the rows and then uses another select to extract all the id.This gets the parent sessions as well as the sub sessions.

### Time Complexity

The time complexity is O(nm), where
n = number of rows extracted to display/print
k = time complexity of the select function

## An Improved Implementation with better Time complexity

### Database Design

One table for the sessions and one table for the sub sessions. The subsession table would also contain a column to store the id of the parent session.

## Import Agenda Implementation

The only change in the import agenda implementation would be to store the subsession and the session separately into their respective tables. There wouldn't be much impact on the time complexity here.

## Look Up agenda Implementation

In the look up agenda implementation, we will extract the rows based on the values from the parent session table.
Then using the id's of the parent sessions, we will extract the specific rows from the sub session table.
This would prevent us from going over the session table twice thus improving the time complexity.

## Reason for my choice

The excel file provided contains only 80 rows and loop over the database of 80 rows doesn't take much time. Yes if the database contains thousads of rows, then the second implementation would be better.
