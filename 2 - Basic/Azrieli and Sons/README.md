This exercise will expose you to "dirty" and scattered information that you will need to clean up and merge into one central table that contains clean and comprehensive information.

Through the exercise, you will be exposed to the types of problems (real) that can appear in the information you will be working on in the future, and you will develop awareness of the importance of the process of clearing the information and the quality of the data on which you work.

This exercise also requires analytical capabilities to collect and cross-reference data from various sources, which are also needed for the basic analytical stage that you learned in the previous stage.

It is not for nothing that you are asked to use these capabilities in this exercise: Many steps of clearing information tend to be done during the basic analysis of the data. This is because only at this stage do we begin to get an initial understanding of the data we have through which we can understand whether the information makes sense and requires cleaning.

It is advisable, of course, to try to anticipate possible flaws and problems in the information as soon as possible, as late detection of problems will be more expensive to handle and will require rerun of all products developed to the discovery stage. However, it is unreasonable to expect that we will be able to detect and address all the problems we have before we preliminary analysis.




Azrieli Trucks and Sons Company

The Azrieli and Sons trucks company pays its drivers every month based on the amount of kilometers they traveled in that month. Each kilometer has a different tariff according to the day it was carried out (day or night), the identity of the supplier who ordered the trip and many other factors.

The following information is provided by the Company:
1. Taarif.csv: This file contains a tariff table for kilometers traveled, when the rate varies according to many parameters relating to the nature of the trip.
The table fields are as follows:
• Customer - The name of the company that ordered the trip. Each company pays different rates according to the contract signed between it and Azrieli and Sons.
• Basic_taarif - The payment paid by the ordering company for each kilometer within the first 200 kilometers of each trip.
• Extra_milage - The payment per kilometer after the first 200 kilometers per trip.
• Night_bonus - a percentage addition to the tariff for every kilometer that takes place at night.
• Weekend_bonus - a percentage addition to the tariff for each kilometer that takes place on weekends.

2. Drivers_with_kviut.csv, new_drivers.csv: These files contain information about drivers in the company. The fields in the table are listed below:
• Id - ID number Of the driver
• Birthdate - the driver's date of birth
• Gender
• Vetek - seniority in the company (time the employee works at the company)

3. Trips: This folder contains a file for each month and a truck. The file name will be in format <date> _ <truck_id>. Each file contains a table describing information about the truck's journey that month. The table fields are listed below:
• Driver_id - ID Of the driver on the ride
• Customer - The name of the customer who ordered the trip
• Start_time - A date that indicates the start time of the trip
• End_time - A date that indicates the end time of the trip
• Km - The number of kilometers traveled

Mission

You must generate from the data you received a table named summary.csv. The table will contain for each driver and month information about the driver and performance of the driver that month. The fields that should appear in the table are:

• Driver_id - ID Of the driver
• Month - the month, for example 01/2015
• Total_income - total driver's salary that month
• Total_km - the total number of kilometers traveled by the driver that month
• Gender - the gender of the driver
• Age - the driver's age in years (exactly one digit after decimal point.)
• Vetek - seniority of the driver in the company in years (exactly one digit after the dot.)
The calculation of the total salary of the driver should be carried out according to the tariff table.




Highlights and comments

1. As in any project, the raw information received from the customer may be dirty and contain many problems. Since this is an exercise in data cleaning, we have put a lot of problems into the data. So you need to be sharp, feel the information, and systematically search for possible information problems.

2. Record all problems with the information you encounter in a separate Word document. Many times, the concentration of information problems for the client is an interesting product in its own right. When you document problems, do it as neatly and clearly as possible so that the customer can view them yourself easily. You must submit this document to your mentor when the exercise is completed.

3. Do not hesitate to ask the client (ie the mentor) for explanations of information you do not understand, or for problems with information that require interpretation / clarification. However, try to discover a degree of independence, too, and if there are things that you can solve without the customer did so. Of course, it is worth concentrating these steps and documenting them so that the customer and anyone who looks at the products of the project will be aware of them.

4. Test your solution.
