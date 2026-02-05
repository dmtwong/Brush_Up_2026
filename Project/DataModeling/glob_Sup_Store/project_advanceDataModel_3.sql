/* 
README
----------
2026-02-05 16:28:
Will redesign the data model from ER diagram rather than backward engineering
(Though the data type 'learnt' will still be used.
2026-02-05 17:25:
forward engineer from revised ER to deploy physcial data model
2026-02-05 17:52:
Now develope the warehouse (star schema) as/in a seperate database. It could be 
done in the same database more easily but it will defeat the purpose of seperating 
the analytical query from transactional database. Could be overkill and 
causing more complex Airflow DAGs to move data between two different MySQL connections but 
for now let's do it in two seperate schema.
SQL script that is generated from ER diagram (gss_ER.mwb) using forward engineering feature of mysql workbench (source): fromER.sql 
SQL script to create star: gss_star_schema.sql
ER diagram backward engineered from the star schema: gss_star_Backward.mwb

*/

