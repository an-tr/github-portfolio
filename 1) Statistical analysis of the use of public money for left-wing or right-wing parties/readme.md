# Statistical analysis of the use of public money for left-wing or right-wing parties
## Introduction
the project aims to gain a deeper understanding of how the political right and left really impact on the municipalities governed, every municipality in italy must make public the investments made, using the website 'http://storico.openbilanci.it' it is possible to get an overview of the funds allocated to each category:
* Administration
  
      Sum of all expenses for the offices of the municipal services
* Social
  
      Expenditure on the provision of social services to citizens
* Environment

      Expenditure on land use, the environment and the maintenance of common areas
* Transport

      Expenditure to ensure local public transport services, roads and pavements.
* Education

      Expenditure on school services (excluding kindergartens) and maintenance of owned buildings.
* Culture

      Expenditure on the promotion of cultural activities, construction and maintenance of suitable buildings
* Sport

      Expenditure on the provision of sports services, the maintenance and construction of sports facilities, and the support or organisation of sports events
* Tourism

      Expenditure on the promotion of local tourism
* Economic

      Expenditure on local economic development, including expenditure on posters or advertising and organisation of events
* Police

      Expenses for the local police, including the purchase of goods, such as cars or adequate office facilities, and maintenance 
* Justice

      Expenses for judicial offices in the territory

after extrapolating and cleaning the data, a statistical analysis was carried out (using the t-student test) which showed significant differences in the approach to investments

## Collecting and cleaning data
To carry out the data collection (as I did not have any faster methods available), I opted to use SELENIUM and collected the investment data for each category and for each year for all Italian municipalities, then after a brief data cleaning I divided each party that governed in the municipalities into categories (right or left) to carry out the analysis in a clear manner

## Results of the analysis
After preparing the data, therefore, I analysed the trands of each investment category by comparing left and right (example below)



![education](https://github.com/an-tr/github-portfolio/assets/140265380/eca95ee0-6d34-4802-a0bc-c01ba6fd9f53)

and finally I carried out the analysis to highlight in which categories there are significant differences in how the left and right invest in the governed territory.
The project showed that the categories where the right and left differ are administration, education and tourism, where it is evident that the left invests more in administration while the right was the biggest investor in education and tourism.
in the other categories there are no statistical differences in the use of public money


![statistical difference between right and left in italy](https://github.com/an-tr/github-portfolio/assets/140265380/746f40bf-35e5-4279-a69e-a1d36e57ae0b)
