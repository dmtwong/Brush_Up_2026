/* 
Neutral Reviewers
Write a SQL Query to find the name of all reviewers who have rated their ratings with a NULL value.
Output Schema:
reviewer_name
NOTE: Output column name has to match the given output schema.

Example Output:
reviewer_name
MaxPlank
NeilsBohr
Schrodinger

*/

SELECT A.reviewer_name
FROM reviewers as A
INNER JOIN ratings as B
ON A.reviewer_id = B.reviewer_id
WHERE B.reviewer_stars IS NULL;