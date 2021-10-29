# Imports the pandas library and gives it the alias of pd
import pandas as pd 

# Reads the CSV file containing all of the IMDB movie data and set those valuses equal 
# to a data frame named movies_df
movies_df = pd.read_csv('IMDb movies.csv')

# Question 1
print(" \nQuestion #1: What genres are the highest grossing films on average in the US?\n")

# This is a function that cleans up the income column of the data set. It's hard to see because 
# there are so many data point but many on the incomes are listed as NaN and others are listed as 
# a non US currency (ex. EUR 2398573). Because I only wanted to deal with the US's data for this 
# project, this function goes through and replaces all of the NaN with a 0 and all of the non US's 
# currency values with a zero. This function also removes the '$' and a space from each value and 
# converts the number from a string to an integer. 
def edit_incomes(usa_gross_income):
    if pd.isna(usa_gross_income):
        return 0
    elif any(chr.isdigit() for chr in usa_gross_income[:3]):
        row_income = usa_gross_income.replace('$ ', '')
        row_income_int = int(row_income)
        return row_income_int
    elif not any(chr.isdigit() for chr in usa_gross_income[:3]):
        return 0

# This code replaces the usa_gross_income column with the new updated column by using the apply method
movies_df['usa_gross_income'] = movies_df['usa_gross_income'].apply(edit_incomes)

# This code uses the groupby method to group the data by genre. It then finds the mean of all of the 
# numeric values for each genre. It then sorts the values using the sort_values method by the 
# usa_gross_income from greatest to smallest
update_movies_df = movies_df.groupby(['genre']).mean().sort_values('usa_gross_income', ascending=False)

# These are print statements to display the answer. I use an f string to input the values that I need. 
# I use the iloc method to get the exact location of the usa_gross_income in the dataframe. 
print("Top three highest grossing genres in the US on average:\n")
print(
    f"Action, Family, Romance: $ {update_movies_df.iloc[0, 3]:,.2f} \n"
    f"Action, Adventure, Sci-Fi: $ {update_movies_df.iloc[1, 3]:,.2f} \n"
    f"Adventure, Mystery, Sci-Fi: $ {update_movies_df.iloc[2, 3]:,.2f}"
)

print("\n======================================================\n")

# Question 2
print(" \nQuestion #2: Which movie has the longest runtime?\n")

# All of the logic for this question is done directly in the print statement. The first value 
# in the f string sorts the movies_df by duration and then gets the duration of the first value 
# or the movies with the longest duration using the iloc method. The second value is simply there
# to display the duration in hours instead of minutes by dividing the minutes by 60. The third 
# values simpley gets the name of the film that has the longest duration using the iloc method. 
print(
  f"\nAt {movies_df.sort_values('duration', ascending=False).iloc[0, 6]}"
  f" minutes ({(int(movies_df.sort_values('duration', ascending=False).iloc[0, 6]) / 60):.2f} hours!),"
  f"'{movies_df.sort_values('duration', ascending=False).iloc[0, 2]}' "
  f"is the longest movie in this database.\n"
)

print("\n======================================================\n")

# Question 3
print(" \nQuestion #3: Which production company has made the most money from their films? Both total and on average?\n")

# This code groups the movies_df by production company. It then sums all of the numeric values 
# and sorts the values by usa_gross_income.It then returns only the first 3 values using the head 
# method and specifying 3 rows. It then set this equal to a new dataframe.
movies_by_production = movies_df.groupby(['production_company']).sum().sort_values('usa_gross_income', ascending=False).head(3)

# This code is very similar to question 1 where the values for the usa_gross_income are found 
# using the iloc method and then inserted using an f string.
print("Top three highest grossing production companies in the US:\n")
print(
    f"Warner Bros.: $ {movies_by_production.iloc[0, 3]:,.2f}\n"
    f"Universal Pictures: $ {movies_by_production.iloc[1, 3]:,.2f}\n"
    f"Paramount Pictures: $ {movies_by_production.iloc[2, 3]:,.2f}\n"
)

# All this code is exactly the same as above but instead of finding the sum of all the numeric values 
# it finds the mean which returns different results for the top 3 production companies. 
movies_by_production_avg = movies_df.groupby(['production_company']).mean().sort_values('usa_gross_income', ascending=False).head(3)
print("Top three highest grossing production companies in the US on average:\n")
print(
    f"Marvel Studios: $ {movies_by_production_avg.iloc[0, 3]:,.2f}\n"
    f"Fairview Entertainment: $ {movies_by_production_avg.iloc[1, 3]:,.2f}\n"
    f"Lucasfilm: $ {movies_by_production_avg.iloc[2, 3]:,.2f}\n"
)