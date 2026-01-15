/* 
Firefighter's Average

Given a table FIREFIGHTERS, query the average of all the people saved by the Firefighters whose CountryCode is PM.

The description of the table FIREFIGHTERS is as follows:

Image

NOTE : The output should contain only 1 column ‘AVG(PeopleSaved)’ .

Example : 


*/

/* YOUR QUERY GOES HERE
   Example: SELECT * FROM EMPLOYEE; 
*/
SELECT AVG(PeopleSaved)
FROM FIREFIGHTERS
WHERE CountryCode = "PM";