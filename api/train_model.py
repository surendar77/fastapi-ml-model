import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib
data={
        'math':[78,65,78,45,30,60,80,40,20,50],
    'science':[20,68,45,82,63,81,20,40,60,90],
    'English':[30,70,45,65,98,42,30,30,60,60],
    'Result':['Fail','Pass','Pass','Pass','Fail'
              ,'Pass','Fail','Fail','Fail','Pass']
}
df=pd.DataFrame(data)
df['Result']=df['Result'].map({'Pass':1,'Fail':0})
#train the model
x=df[['math','science','English']]
y=df['Result']
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
#call the model
model=LogisticRegression()
model.fit(x_train,y_train)
joblib.dump(model,'model.pkl')
