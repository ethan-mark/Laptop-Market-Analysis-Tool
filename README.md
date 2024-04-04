# Laptop Market Analysis Tool

DATA LINK: https://www.microcenter.com/search/search_results.aspx?N=4294967288&NTK=all&sortby=match&rpp=96 
# Overview
This is a web scraping project using Selenium Python to extract the laptop search query data from Microcenter to help answer the question of "Which laptop should I buy?" using the prices and rating of each laptop.  We extract the laptop name, the graphics card, cpu processor, RAM, harddrive, the original price, the current price, and the rating from the laptop entries within the search query page. 

# Features
**Automated Data Collection**: Python Selenium to navigate and extract laptop data from the Microcenter search query.  This data is then put into a Pandas dataframe to prepare it for data cleaning.

**Data Cleaning**: The Pandas dataframe is converted into a CSV for data cleaning.  Using the CSV, we remove duplicates and fix any errors.  

(It is important to note that some of the laptop entries do not have an original price or do not have any ratings, but are kept within the data.  It is also important to note that there are blank cells within some of the rows, but are not removed, as it is important to still see how those compare with the rest of the data.)

**Data Analysis**: Analysis on collected data to identify the best value laptops based on user-defined criteria (e.g., price, performance, graphics card, rating).

**Reporting**: The data is visualized using Tableau showcasing which laptop has the highest discount % along with the rating per laptop. 
(https://public.tableau.com/views/microcenter_laptop_analysis/Dashboard1?:language=en-US&:sid=&:display_count=n&:origin=viz_share_link)

# Getting Started
# Prerequisites
Python 3.6 or later
Selenium WebDriver
Additional Python libraries: pandas for data manipulation.

# SQL Preview
| INDEX  | NAME | CPU_PROCESSOR | GRAPHICS_CARD | RAM | HARD_DRIVE | RATING | ORIGINAL_PRICE | CURRENT_PRICE | MONEY_SAVED | DISCOUNT_PERCENT |
|-------------| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
|222|HP ZBook Studio G9 Mobile Workstation 16" Laptop Computer - Silver|Intel Core i9 12900H 1.8GHz Processor|NVIDIA RTX A2000 8GB GDDR6|32GB DDR5-4800 RAM| 1TB Solid State Drive|4.8|2999.99|1399.99|1600|0.53|
|54|HP ZBook Firefly G9 Mobile Workstation 16" Laptop Computer - Silver	| Intel Core i5 12th Gen 1245U 1.6GHz Processor	| NVIDIA Quadro T550 4GB GDDR6	| 16GB DDR5-4800 RAM	| 256GB Solid State Drive|	5	|1969.99	|599.99	|1370|	0.70|
| 79	|Apple MacBook Pro MK1A3LL/A (Late 2021) 16.2" Laptop Computer (Refurbished) - Space Gray	| Apple M1 Max 10-Core CPU	| 32-Core GPU/16-Core Neural Engine	| 32GB Unified Memory	|NO RATINGS | 1TB Solid State Drive	|	2974.99|	1899.99	|1075	|0.36
| 129	|Acer Predator Triton X PTX17-71-95HW 17.0" Gaming Laptop Computer - Abyssal Black	| Intel Core i9 13th Gen 13900HX 1.6GHz Processor	| NVIDIA GeForce RTX 4090 16GB GDDR6|	 64GB DDR5-5200 RAM|	 2TB Solid State Drive|	5	|3799.99	|2799.99|	1000	|0.26|
| 290|	Dell Alienware x16 R1 16" Gaming Laptop Computer - Lunar Silver	| Intel Core i9 13th Gen 13900HK 1.9GHz Processor	| NVIDIA GeForce RTX 4080 12GB GDDR6|32GB LPDDR5-6000 RAM	| 1TB Solid State Drive|	4.9|	3599.99|	2599.99	|1000	|0.28|
| 135|	Razer Blade 18 (2023) 18" Gaming Laptop Computer - Black	| Intel Core i9 13th Gen 13950HX 1.6GHz Processor	| NVIDIA GeForce RTX 4090 16GB GDDR6	| 32GB DDR5-5600 RAM	| 1TB SSD+1TB SSD	|4.5|	4499.99	|3699.99|	800	|0.18|

