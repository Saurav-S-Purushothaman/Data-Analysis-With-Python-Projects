import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv(
    "fcc-forum-pageviews.csv",
    index_col = 0,
    parse_dates = True
    )

# Clean data
df = df[
    (df["value"]>=df["value"].quantile(0.025)) &
    (df["value"]<= df["value"].quantile(0.975))
    ]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(18,6))
    ax.plot(df.index, df["value"],color="red")
    ax.set(xlabel="Date",ylabel="Page Views", title='Daily freeCodeCamp Forum Page Views 5/2016-12/2019') 




    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df.index = pd.to_datetime(df.index,format = "%Y-%m-%d")
    df_copy = pd.DataFrame(df)
    df_copy["Year"] = df.index.year
    df_copy["Month"] = df.index.month
    df_bar = df_copy.groupby(["Year","Month"]).mean()
    df_bar =df_bar.unstack()

    # Draw bar plot
    fig=df_bar.plot(kind ="bar",figsize=(12,6)).figure
    plt.xlabel("Years")
    plt.ylabel("Average Page Views")
    plt.legend(fontsize = 10, labels =["January","February","March","April","May","June","July","August","September","October","November","December"] )
    plt.show()




    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig , (ax_year, ax_month) = plt.subplots(1,2)
    fig.set_figwidth(15)
    fig.set_figheight(7)


    ax_year = sns.boxplot(x = df_box.year, y = df_box.value,ax=ax_year)
    ax_year.set(xlabel = "Year", ylabel = "Page Views", title = "Year-wise Box Plot (Trend)")


    ax_month = sns.boxplot(x = df_box["month"], y = df_box["value"], ax = ax_month)
    ax_month.set(xlabel = "Month", ylabel = "Page Views", title = "Month-wise Box Plot (Seasonality)")

       
  

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
