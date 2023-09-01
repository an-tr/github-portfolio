# Real time calculation of rental values for houses at auction in milan
## Introduction
The rental price of a house depends on several variables, the factors are varied, but the most indicative are the square metres, the area, the year of construction and the neighbours.
In addition to this complexity, the real estate market changes year by year, creating bewilderment for those wishing to invest in a property

![milano zone](https://github.com/an-tr/github-portfolio/assets/140265380/ede11b1e-f74e-4d59-9bb3-53e7612bed47)

## Project
the objective of this project is to create a tool capable of calculating the rental value of a property in milan at any given time, thus giving investors a tool to assess the possible rental value of houses at auction at this time. the project consists of 3 parts:

1) Rental data collection (scraping_affitti.py)
  
   when the programme starts, using the immobiliare.it website and using the "BeautifulSoup" library, the algorithm collects data on all the houses for           rent in milan, collecting data on size, area and price for each house

2) Auction data collection (scraping aste.py)

   similar to rent data collection, data is collected on all auction houses (size, base auction price and area)

3) Data cleaning (cleaning_affitti_aste.py)

   brief data cleaning to facilitate prediction by the machine leaning algorithm
  
4) Rent calculation and forecasting (machine_learning_affitti.py)

   using "sklearn" we use the linear regression model to predict the rent of all houses at auction right now, giving the user a clear overview of the current real estate situation in milan
