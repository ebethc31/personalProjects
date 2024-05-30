Hospital Price Estimating Tool

The goal of this project is to provide clarity to the average pateint. Often times patients are left wondering how their hospital bill is calculated.

The main goals are as follows: 
1.) Allow the user to search their procedure/visit type and get an estimated cost. 
2.) Provide an itemized list that contributes to the estimated cost. 
3.) Save estimates and directly compare them to other hospitals.

Throughout this project, the scope has changed drastically. Initially, this was meant to be an application that could work for any public hospital in the U.S. and could estimate the cost off of a discription. It was also meant to include different types of insurance and their negotiated prices. The scope has been narrowed to public Hopsitals in upstate SC, the most common procedures, and it only gives estimates for payments in cash.

Current Status:

Out of the public hospitals that published a machine readable file of their pricing data in upstate SC, I cleaned that data to only contained desired attributes. These attributes included: charge code, charge description, rev code, and any cash pricing data.

The next step is to create a python script that calls an SQL query that corellates with the entered procedure. 
-More details: 
    - Provide a menu that the user can pick a procedure from 
    - Display the charge code that correlates with the procdure, its charge description, and pricing

After this step, I would like to map out a correlating procedures list. What this would look like is a after recieving the desired procedure the application would put together a list of similar procedure that correlate with the given procudure. Then allow the user to pick and choose witch of the similar procuders should be included in the estimate.
