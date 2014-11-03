py-ECB-CA-2014
==============

European Bank Asset Quality Review  Stress Test Datapoints in Python 


Play out merger plans with combinatorical optimization easily by using the dataset in python objects.

There are more the 1 million data points pubblished on the european banking sector by ECB and EBA.
Would you like to have it an intelligent format ? No gigabites of xls and pdf - that even the ECB-EBA with their 6000 private consulents 
could not handle without smafus ... according to the wsj.

For now this is the data set from the 2014 edition. 

Objective is to add standardized items from balance-sheets and follow up in the comming years .


version 0.1

ECB_CA_2014.py , contains the main figuers from the ECB CA-DISCLOUSEREs with definitions and notes and original bank specific remarks are included. 

version 0.2

EBA_ST_2014.py was added. This contians all metadata for the .cvs files, conversions codes between EBA nd ECB entity IDs.


pyEBAtest101.py calculates the ECBs EU wide CET1 shortfall (B10) from EBA data for a test case (Eurobank Ergasias GR).

pyEBAtest103.py calculates the  shortfalls (B9 B10) taken into account restructuring plans. It prints a table for all banks under restructuring.





