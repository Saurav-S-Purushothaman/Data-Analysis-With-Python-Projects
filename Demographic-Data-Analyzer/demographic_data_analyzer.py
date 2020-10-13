import pandas as pd
import numpy as np


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df.groupby('race')['race'].count()
    

    # What is the average age of men?
    age =df[(df["sex"]) =="Male"]["age"].mean()
    average_age_men = round(age,1)

    # What is the percentage of people who have a Bachelor's degree?
    no_bachelors = len(df[(df["education"]=="Bachelors")])
    total = len(df)
    percentage = no_bachelors*100/total
    percentage_bachelors = round(percentage,1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    new=df[(df["education"]== "Bachelors") | (df["education"] =="Masters") | (df["education"]=="Doctorate")]
    more = new[(new["salary"]==">50K")]

    lnew=df[(df["education"]!= "Bachelors") & (df["education"] !="Masters") & (df["education"]!="Doctorate")]
    lmore = lnew[(lnew["salary"]==">50K")]
    
    higher_education = len(new)
    lower_education = len(lnew)

   

    # percentage with salary >50K
    higher_education_rich =  round(len(more)*100/len(new),1)
    lower_education_rich = round(len(lmore)*100/len(lnew),1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df["hours-per-week"].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = len(df[df['hours-per-week'] == min_work_hours])

    rich_percentage = round(len(df[(df['hours-per-week'] == min_work_hours) & (df['salary'] == '>50K')]) / num_min_workers * 100, 1)

    # What country has the highest percentage of people that earn >50K?
    fifty= df[(df["salary"]==">50K")]
    g1 = fifty.groupby("native-country").count()
    g2 = df.groupby("native-country").count()
    g3 = g1/g2


    highest_earning_country = g3["salary"].idxmax()
    highest_earning_country_percentage = round(g3["salary"].max()*100,1)

    # Identify the most popular occupation for those who earn >50K in India.
    india = df[(df["native-country"]=="India")  & (df["salary"]==">50K")]
    occ =india.pivot_table(index = ["occupation"],aggfunc = "size")
    top_IN_occupation = occ.idxmax()


    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
