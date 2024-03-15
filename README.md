# microcenter_webscraping_analysis

This is a web scraping project using Selenium Python to extract the laptop search query data from Microcenter to help answer the question of "Which laptop should I buy?".  We extract the laptop name, the graphics card, cpu processor, RAM, harddrive, the original price, the current price, and the rating.  *It is important to note that some of the laptop entries do not have an original price or do not have any ratings.   

This data is then processed through Pandas to create a dataframe and exported to a CSV for data cleaning.  

The data is cleaned using Excel/Sheets for duplicates, incorrect data, and NULLs.

The data is visualized using Tableau showcasing which laptop has the highest discount % along with the rating per laptop. 
(https://public.tableau.com/views/microcenter_laptop_analysis/Dashboard1?:language=en-US&:sid=&:display_count=n&:origin=viz_share_link)


