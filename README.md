# Laptop Market Analysis Tool

# Overview
This is a web scraping project using Selenium Python to extract the laptop search query data from Microcenter to help answer the question of "Which laptop should I buy?" using the prices and rating.  We extract the laptop name, the graphics card, cpu processor, RAM, harddrive, the original price, the current price, and the rating.  

# Features
**Automated Data Collection**: Python Selenium to navigate and extract laptop data from the Microcenter search query.  This data is then put into a Pandas dataframe to prepare it for data cleaning.
**Data Cleaning**: The Pandas dataframe is converted into a CSV for data cleaning.  Using the CSV, we remove duplicates and fix any errors.  
-It is important to note that some of the laptop entries do not have an original price or do not have any ratings, but are kept within the data.

-It is also important to note that there are blank cells within some of the rows.  These are not removed, as it is important to see what each laptop offers and what it does not have.

**Data Analysis**: Analysis on collected data to identify the best value laptops based on user-defined criteria (e.g., price, performance, graphics card, rating).

**Reporting**: The data is visualized using Tableau showcasing which laptop has the highest discount % along with the rating per laptop. 
(https://public.tableau.com/views/microcenter_laptop_analysis/Dashboard1?:language=en-US&:sid=&:display_count=n&:origin=viz_share_link)

# Getting Started
# Prerequisites
Python 3.6 or later
Selenium WebDriver
# Additional Python libraries: pandas for data manipulation.
