import pandas as pd

FILEPATH = "titanic.csv"

def load_file():
    df = pd.read_csv(FILEPATH)

    return df


def explore_data(data):
    print(f"{data.info()}\n")

    print(f"{data.isnull().sum()}\n")


if __name__ == "__main__":
    # load dataset
    df = load_file()
    
    # explore data
    explore_data(df)

    # drop irrelevant columns
    df.drop(['PassengerId', 'Name', 'Ticket', 'Cabin'], axis=1, inplace=True)
    explore_data(df)

    # fill missing values
    df['Age'] = df['Age'].fillna(df['Age'].median())
    df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])
    explore_data(df)

    # encode catagorical variables
    df['Sex'] = df['Sex'].map({'male': 0, 'female': 1}) # set male to 0 and female to 1
    df = pd.get_dummies(df, columns=['Embarked'], drop_first=True)
    explore_data(df)

    # save dataset
    df.to_csv('titanic_cleaned.csv', index=False)
