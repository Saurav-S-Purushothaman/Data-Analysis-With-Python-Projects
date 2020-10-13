import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df =pd.read_csv("medical_examination.csv")

# Add 'overweight' column
weight = df["weight"]
height_sq = df["height"]**2/10000
bmi = weight/height_sq
bmi[(bmi<=25)] =0
bmi[(bmi>25)] = 1

df['overweight'] = bmi.astype("int32")

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholestorol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.

chol = df["cholesterol"]
chol[(chol <=1)] =0
chol[(chol)>1]  =1

glucose = df["gluc"]
glucose[(glucose<=1)]=0
glucose[(glucose>1)]=1



# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df,id_vars = ["cardio"],value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active',  'overweight'])


    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the collumns for the catplot to work correctly.
    

    # Draw the catplot with 'sns.catplot()'
    fig =sns.catplot(data=df_cat,x = "variable",  hue="value",kind = "count",col="cardio")


    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) & 
      (df['height'] >= df['height'].quantile(0.025)) &
      (df['height'] <= df['height'].quantile(0.975))&
      (df['weight'] >= df['weight'].quantile(0.025)) &
      (df['weight'] <= df['weight'].quantile(0.975))
      ]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(corr)



    # Set up the matplotlib figure
    fig,ax= plt.subplots(figsize=(11,8))

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr,mask=mask,annot=True)


    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
