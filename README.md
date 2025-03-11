# Tokopedia Website Scraping using Selenium

## Project Overview
This project explores the aplication of website scraping of Hotwheels Indonesia product and price on its Tokopedia official store. It utilizes Selenium, Python, and Pandas to perform website scraping and data transformation.

## Data Flow

![data flow](https://github.com/rizkyjarr/web-scraping-tokopedia/blob/main/assets/data_flow.png)

## Technology & Tools Used
1. Programming Language - Python
2. Libraries :
    - Regular Expression (Regex) --> for handling data transformation
    - Selenium --> Perform website scraping and fetch text from Tokopedia's html page
    - Pandas --> Convert fetched data from text to dataframe and load into csv

## Scripts for project (based on order)
1. Website scraping using defined max pages - this script is created for testing purpose before scraping the whole products within the page - [python_case_2_func_paginated_max_page.py](https://github.com/rizkyjarr/web-scraping-tokopedia/blob/main/python_case_2_func_paginated_max_page.py)
2. Website scraping for the whole products - [python_case_2_func_paginated.py](https://github.com/rizkyjarr/web-scraping-tokopedia/blob/main/python_case_2_func_paginated.py)

## Project Results

Project results in .csv file containing the product and price. The data is analytics-ready for further analysis or competitor analysis.

![project results](https://github.com/rizkyjarr/web-scraping-tokopedia/blob/main/assets/results.png)