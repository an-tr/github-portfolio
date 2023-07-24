import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('politics.csv')

#select by right and left
df_right=df.drop(df[df['orientation'] == 'Left'].index)
df_left=df.drop(df[df['orientation'] == 'Right'].index)

#select by the year

df_right_2005=df_right.drop(df_right[df_right['year'] != 2005].index)
df_right_2006=df_right.drop(df_right[df_right['year'] != 2006].index)
df_right_2007=df_right.drop(df_right[df_right['year'] != 2007].index)
df_right_2008=df_right.drop(df_right[df_right['year'] != 2008].index)
df_right_2009=df_right.drop(df_right[df_right['year'] != 2009].index)
df_right_2010=df_right.drop(df_right[df_right['year'] != 2010].index)
df_right_2011=df_right.drop(df_right[df_right['year'] != 2011].index)
df_right_2012=df_right.drop(df_right[df_right['year'] != 2012].index)
df_right_2013=df_right.drop(df_right[df_right['year'] != 2013].index)
df_right_2014=df_right.drop(df_right[df_right['year'] != 2014].index)

df_left_2005=df_left.drop(df_left[df_left['year'] != 2005].index)
df_left_2006=df_left.drop(df_left[df_left['year'] != 2006].index)
df_left_2007=df_left.drop(df_left[df_left['year'] != 2007].index)
df_left_2008=df_left.drop(df_left[df_left['year'] != 2008].index)
df_left_2009=df_left.drop(df_left[df_left['year'] != 2009].index)
df_left_2010=df_left.drop(df_left[df_left['year'] != 2010].index)
df_left_2011=df_left.drop(df_left[df_left['year'] != 2011].index)
df_left_2012=df_left.drop(df_left[df_left['year'] != 2012].index)
df_left_2013=df_left.drop(df_left[df_left['year'] != 2013].index)
df_left_2014=df_left.drop(df_left[df_left['year'] != 2014].index)


#calculate the avarages

mean_amministration_invest_right = df_right['amministration_invest'].mean()
mean_social_invest_right = df_right['social_invest'].mean()
mean_environment_invest_right = df_right['environment_invest'].mean()
mean_transport_invest_right = df_right['transport_invest'].mean()
mean_education_invest_right = df_right['education_invest'].mean()
mean_culture_invest_right = df_right['culture_invest'].mean()
mean_sport_invest_right = df_right['sport_invest'].mean()
mean_tourism_invest_right = df_right['tourism_invest'].mean()
mean_economic_invest_right = df_right['economic_invest'].mean()
mean_police_invest_right = df_right['police_invest'].mean()
mean_justice_invest_right = df_right['justice_invest'].mean()
mean_amministration_invest_left = df_left['amministration_invest'].mean()
mean_social_invest_left = df_left['social_invest'].mean()
mean_environment_invest_left = df_left['environment_invest'].mean()
mean_transport_invest_left = df_left['transport_invest'].mean()
mean_education_invest_left = df_left['education_invest'].mean()
mean_culture_invest_left = df_left['culture_invest'].mean()
mean_sport_invest_left = df_left['sport_invest'].mean()
mean_tourism_invest_left = df_left['tourism_invest'].mean()
mean_economic_invest_left = df_left['economic_invest'].mean()
mean_police_invest_left = df_left['police_invest'].mean()
mean_justice_invest_left = df_left['justice_invest'].mean()





#graphs for each category for all the years

####### amministration_invest

category='amministration_invest'
years=[2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014]
right_means=[df_right_2005[category].mean(),df_right_2006[category].mean(),df_right_2007[category].mean(),df_right_2008[category].mean(),df_right_2009[category].mean(),df_right_2010[category].mean(),df_right_2011[category].mean(),df_right_2012[category].mean(),df_right_2013[category].mean(),df_right_2014[category].mean()]
left_means=[df_left_2005[category].mean(),df_left_2006[category].mean(),df_left_2007[category].mean(),df_left_2008[category].mean(),df_left_2009[category].mean(),df_left_2010[category].mean(),df_left_2011[category].mean(),df_left_2012[category].mean(),df_left_2013[category].mean(),df_left_2014[category].mean()]

plt.plot(years, right_means, label='right')
plt.plot(years, left_means, label='left')

plt.xlabel('year')
plt.ylabel('%'+' of the total investment')
plt.title('amministration year by year trend')
plt.legend()

plt.show()

#######

####### social_invest

category='social_invest'
years=[2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014]
right_means=[df_right_2005[category].mean(),df_right_2006[category].mean(),df_right_2007[category].mean(),df_right_2008[category].mean(),df_right_2009[category].mean(),df_right_2010[category].mean(),df_right_2011[category].mean(),df_right_2012[category].mean(),df_right_2013[category].mean(),df_right_2014[category].mean()]
left_means=[df_left_2005[category].mean(),df_left_2006[category].mean(),df_left_2007[category].mean(),df_left_2008[category].mean(),df_left_2009[category].mean(),df_left_2010[category].mean(),df_left_2011[category].mean(),df_left_2012[category].mean(),df_left_2013[category].mean(),df_left_2014[category].mean()]

plt.plot(years, right_means, label='right')
plt.plot(years, left_means, label='left')

plt.xlabel('year')
plt.ylabel('%'+' of the total investment')
plt.title('social year by year trend')
plt.legend()

plt.show()

#######

####### environment_invest

category='environment_invest'
years=[2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014]
right_means=[df_right_2005[category].mean(),df_right_2006[category].mean(),df_right_2007[category].mean(),df_right_2008[category].mean(),df_right_2009[category].mean(),df_right_2010[category].mean(),df_right_2011[category].mean(),df_right_2012[category].mean(),df_right_2013[category].mean(),df_right_2014[category].mean()]
left_means=[df_left_2005[category].mean(),df_left_2006[category].mean(),df_left_2007[category].mean(),df_left_2008[category].mean(),df_left_2009[category].mean(),df_left_2010[category].mean(),df_left_2011[category].mean(),df_left_2012[category].mean(),df_left_2013[category].mean(),df_left_2014[category].mean()]

plt.plot(years, right_means, label='right')
plt.plot(years, left_means, label='left')

plt.xlabel('year')
plt.ylabel('%'+' of the total investment')
plt.title('environment year by year trend')
plt.legend()

plt.show()

#######

####### transport_invest

category='transport_invest'
years=[2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014]
right_means=[df_right_2005[category].mean(),df_right_2006[category].mean(),df_right_2007[category].mean(),df_right_2008[category].mean(),df_right_2009[category].mean(),df_right_2010[category].mean(),df_right_2011[category].mean(),df_right_2012[category].mean(),df_right_2013[category].mean(),df_right_2014[category].mean()]
left_means=[df_left_2005[category].mean(),df_left_2006[category].mean(),df_left_2007[category].mean(),df_left_2008[category].mean(),df_left_2009[category].mean(),df_left_2010[category].mean(),df_left_2011[category].mean(),df_left_2012[category].mean(),df_left_2013[category].mean(),df_left_2014[category].mean()]

plt.plot(years, right_means, label='right')
plt.plot(years, left_means, label='left')

plt.xlabel('year')
plt.ylabel('%'+' of the total investment')
plt.title('transport year by year trend')
plt.legend()

plt.show()

#######

####### education_invest

category='education_invest'
years=[2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014]
right_means=[df_right_2005[category].mean(),df_right_2006[category].mean(),df_right_2007[category].mean(),df_right_2008[category].mean(),df_right_2009[category].mean(),df_right_2010[category].mean(),df_right_2011[category].mean(),df_right_2012[category].mean(),df_right_2013[category].mean(),df_right_2014[category].mean()]
left_means=[df_left_2005[category].mean(),df_left_2006[category].mean(),df_left_2007[category].mean(),df_left_2008[category].mean(),df_left_2009[category].mean(),df_left_2010[category].mean(),df_left_2011[category].mean(),df_left_2012[category].mean(),df_left_2013[category].mean(),df_left_2014[category].mean()]

plt.plot(years, right_means, label='right')
plt.plot(years, left_means, label='left')

plt.xlabel('year')
plt.ylabel('%'+' of the total investment')
plt.title('education year by year trend')
plt.legend()

plt.show()

#######

####### culture_invest

category='culture_invest'
years=[2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014]
right_means=[df_right_2005[category].mean(),df_right_2006[category].mean(),df_right_2007[category].mean(),df_right_2008[category].mean(),df_right_2009[category].mean(),df_right_2010[category].mean(),df_right_2011[category].mean(),df_right_2012[category].mean(),df_right_2013[category].mean(),df_right_2014[category].mean()]
left_means=[df_left_2005[category].mean(),df_left_2006[category].mean(),df_left_2007[category].mean(),df_left_2008[category].mean(),df_left_2009[category].mean(),df_left_2010[category].mean(),df_left_2011[category].mean(),df_left_2012[category].mean(),df_left_2013[category].mean(),df_left_2014[category].mean()]

plt.plot(years, right_means, label='right')
plt.plot(years, left_means, label='left')

plt.xlabel('year')
plt.ylabel('%'+' of the total investment')
plt.title('culture year by year trend')
plt.legend()

plt.show()

#######

####### sport_invest

category='sport_invest'
years=[2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014]
right_means=[df_right_2005[category].mean(),df_right_2006[category].mean(),df_right_2007[category].mean(),df_right_2008[category].mean(),df_right_2009[category].mean(),df_right_2010[category].mean(),df_right_2011[category].mean(),df_right_2012[category].mean(),df_right_2013[category].mean(),df_right_2014[category].mean()]
left_means=[df_left_2005[category].mean(),df_left_2006[category].mean(),df_left_2007[category].mean(),df_left_2008[category].mean(),df_left_2009[category].mean(),df_left_2010[category].mean(),df_left_2011[category].mean(),df_left_2012[category].mean(),df_left_2013[category].mean(),df_left_2014[category].mean()]

plt.plot(years, right_means, label='right')
plt.plot(years, left_means, label='left')

plt.xlabel('year')
plt.ylabel('%'+' of the total investment')
plt.title('sport year by year trend')
plt.legend()

plt.show()

#######

####### tourism_invest

category='tourism_invest'
years=[2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014]
right_means=[df_right_2005[category].mean(),df_right_2006[category].mean(),df_right_2007[category].mean(),df_right_2008[category].mean(),df_right_2009[category].mean(),df_right_2010[category].mean(),df_right_2011[category].mean(),df_right_2012[category].mean(),df_right_2013[category].mean(),df_right_2014[category].mean()]
left_means=[df_left_2005[category].mean(),df_left_2006[category].mean(),df_left_2007[category].mean(),df_left_2008[category].mean(),df_left_2009[category].mean(),df_left_2010[category].mean(),df_left_2011[category].mean(),df_left_2012[category].mean(),df_left_2013[category].mean(),df_left_2014[category].mean()]

plt.plot(years, right_means, label='right')
plt.plot(years, left_means, label='left')

plt.xlabel('year')
plt.ylabel('%'+' of the total investment')
plt.title('tourism year by year trend')
plt.legend()

plt.show()

#######

####### economic_invest

category='economic_invest'
years=[2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014]
right_means=[df_right_2005[category].mean(),df_right_2006[category].mean(),df_right_2007[category].mean(),df_right_2008[category].mean(),df_right_2009[category].mean(),df_right_2010[category].mean(),df_right_2011[category].mean(),df_right_2012[category].mean(),df_right_2013[category].mean(),df_right_2014[category].mean()]
left_means=[df_left_2005[category].mean(),df_left_2006[category].mean(),df_left_2007[category].mean(),df_left_2008[category].mean(),df_left_2009[category].mean(),df_left_2010[category].mean(),df_left_2011[category].mean(),df_left_2012[category].mean(),df_left_2013[category].mean(),df_left_2014[category].mean()]

plt.plot(years, right_means, label='right')
plt.plot(years, left_means, label='left')

plt.xlabel('year')
plt.ylabel('%'+' of the total investment')
plt.title('economic year by year trend')
plt.legend()

plt.show()

#######

####### police_invest

category='police_invest'
years=[2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014]
right_means=[df_right_2005[category].mean(),df_right_2006[category].mean(),df_right_2007[category].mean(),df_right_2008[category].mean(),df_right_2009[category].mean(),df_right_2010[category].mean(),df_right_2011[category].mean(),df_right_2012[category].mean(),df_right_2013[category].mean(),df_right_2014[category].mean()]
left_means=[df_left_2005[category].mean(),df_left_2006[category].mean(),df_left_2007[category].mean(),df_left_2008[category].mean(),df_left_2009[category].mean(),df_left_2010[category].mean(),df_left_2011[category].mean(),df_left_2012[category].mean(),df_left_2013[category].mean(),df_left_2014[category].mean()]

plt.plot(years, right_means, label='right')
plt.plot(years, left_means, label='left')

plt.xlabel('year')
plt.ylabel('%'+' of the total investment')
plt.title('police year by year trend')
plt.legend()

plt.show()

#######

####### justice_investd

category='justice_invest'
years=[2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014]
right_means=[df_right_2005[category].mean(),df_right_2006[category].mean(),df_right_2007[category].mean(),df_right_2008[category].mean(),df_right_2009[category].mean(),df_right_2010[category].mean(),df_right_2011[category].mean(),df_right_2012[category].mean(),df_right_2013[category].mean(),df_right_2014[category].mean()]
left_means=[df_left_2005[category].mean(),df_left_2006[category].mean(),df_left_2007[category].mean(),df_left_2008[category].mean(),df_left_2009[category].mean(),df_left_2010[category].mean(),df_left_2011[category].mean(),df_left_2012[category].mean(),df_left_2013[category].mean(),df_left_2014[category].mean()]

plt.plot(years, right_means, label='right')
plt.plot(years, left_means, label='left')

plt.xlabel('year')
plt.ylabel('%'+' of the total investment')
plt.title('justice year by year trend')
plt.legend()

plt.show()

#######


#using the t-student method to understand in which category there is a statistical difference between right and left in investments

category_diff=[]
categories=['amministration_invest','social_invest','environment_invest','transport_invest','education_invest','culture_invest','sport_invest','tourism_invest','economic_invest','police_invest','justice_invest']

for cat in categories:
    right = df_right[cat].values
    left = df_left[cat].values
    t_stat, p_value = stats.ttest_ind(right, left)

    if p_value < 0.05:
        category_diff.append(cat)

#plotting only the categories with a p-value less the 0,05 to show the difference between left and right 

fig, ax = plt.subplots()
bar1 = ax.bar( 1,mean_amministration_invest_left,0.1,  label='amministration left')
bar2 = ax.bar( 1+0.1,mean_amministration_invest_right,0.1, label='amministration right')

bar3 = ax.bar( 1.5,mean_education_invest_left,0.1,  label='education left')
bar4 = ax.bar( 1.5+0.1,mean_education_invest_right,0.1, label='education right')

bar5 = ax.bar( 2,mean_tourism_invest_left,0.1,  label='tourism left')
bar6 = ax.bar( 2+0.1,mean_tourism_invest_right,0.1, label='tourism right')


ax.set_ylabel('%'+' of the total investment')
ax.legend()
plt.show()

