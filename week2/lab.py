import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats


def show_details(data):
    print(data.head())
    print()
    print(data.info())


if __name__ == "__main__":
    df = pd.read_csv('user_behavior_dataset.csv')

    # show_details(df)

    # clean data
    df = df.dropna()
    df = df.drop(columns=['User_ID'])
    df = df[df['Screen_On_Time'] > 0]
    show_details(df)

    # descriptive stats
    mean_screen = df['Screen_On_Time'].mean()
    median_screen = df['Screen_On_Time'].median()
    mode_screen = df['Screen_On_Time'].mode()[0]
    std_screen = df['Screen_On_Time'].std()
    range_screen = df['Screen_On_Time'].max() - df['Screen_On_Time'].min()
    print(f"\nSCREEN ON TIME STATS")
    print(f"mean: {mean_screen:.2f}\nmedian: {median_screen}\nmode: {mode_screen}\nstandard dev: {std_screen:.2f}\nrange: {range_screen}")

    # visualisations
    # distribution
    plt.figure(figsize=(8,5))
    sns.histplot(df['Screen_On_Time'], bins=20, kde=True)
    plt.title("Distribution of Screen-On Time")
    plt.xlabel("Hours/Day")
    plt.ylabel("Frequency")
    plt.show()

    # app usage
    plt.figure(figsize=(8,5))
    sns.boxplot(x=df['App_Usage_Time'])
    plt.title("Boxplot of App Usage Time")
    plt.xlabel("Minutes/Day")
    plt.show()

    # correlation
    plt.figure(figsize=(8,5))
    sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
    plt.title("Correlation Between Variables")
    plt.show()

    # grouped analysis
    os_group = df.groupby('Operating_System')['Screen_On_Time'].mean()
    os_group.plot(kind='bar', color=['skyblue', 'salmon'])
    plt.title("Average Screen-On Time by OS")
    plt.ylabel("Hours/Day")
    plt.show()

    # summary table
    print(df.describe())
    