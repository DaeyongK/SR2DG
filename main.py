import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

def process_data():

    df=pd.read_csv('culture.csv')

    for index, row in df.iterrows():

        df.at[index,'TARGET_VALUE']=int(input(row['Name']+": "))

    return df

def train(df):

    x = df[['Hair Dark', 'Hair Light', 'Hair Red', 'Hair Blue', 'Hair Length', 'Hair Bang', 'Face Vibes', 'Eye Black',
            'Eye Brown', 'Eye Blue', 'Eye Red', 'Eye Purple', 'Eye Size', 'Blush', 'Tsundere', 'Kindness',
            'Breast Size', 'Hip Size', 'Mass', 'Exposure', 'Skin Darkness']]
    y = df['TARGET_VALUE']
    x_train, x_test, y_train, y_test = train_test_split(x, y)
    model = LogisticRegression()
    model.fit(x_train, y_train)
    return model

def predict(model):

    while True:

        stats = []
        response = input("Proceed? (Y/N) : ").upper()

        if response == "Y":

            stats.append(int(input("Hair Dark: ")))
            stats.append(int(input("Hair Light: ")))
            stats.append(int(input("Hair Red: ")))
            stats.append(int(input("Hair Blue: ")))
            stats.append(float(input("Hair Length: ")))
            stats.append(int(input("Hair Bang: ")))
            stats.append(float(input("Face Vibes: ")))
            stats.append(int(input("Eye Black: ")))
            stats.append(int(input("Eye Brown: ")))
            stats.append(int(input("Eye Blue: ")))
            stats.append(int(input("Eye Red: ")))
            stats.append(int(input("Eye Purple: ")))
            stats.append(float(input("Eye Size: ")))
            stats.append(int(input("Blush: ")))
            stats.append(float(input("Tsundere: ")))
            stats.append(float(input("Kindness: ")))
            stats.append(float(input("Breast Size: ")))
            stats.append(float(input("Hip Size: ")))
            stats.append(float(input("Mass: ")))
            stats.append(float(input("Exposure: ")))
            stats.append(float(input("Skin Darkness: ")))

            print(stats)
            print(model.predict([stats]))
            print(model.predict_proba([stats]))

        elif response == "N":

            print("Thank you for using SR2DG")
            break

        else:

            print("Please provide a proper input (Y/N)")

if __name__ == '__main__':

    df = process_data()
    model = train(df)
    predict(model)



