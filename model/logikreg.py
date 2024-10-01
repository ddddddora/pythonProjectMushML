import pickle
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

bmushr_df = pd.read_csv("mushroomss.csv")
X = bmushr_df.drop(["species"],axis=1)
Y = bmushr_df["species"]
X_train1,X_test1,Y_train1,Y_test1=train_test_split(X, Y,test_size=0.5,random_state=3)
model = LogisticRegression()
model.fit(X_train1,Y_train1)
with open('mushroom.fg', 'wb') as pkl:
    pickle.dump(model, pkl)