import pandas as pd
from sklearn.linear_model import LinearRegression 


file=pd.read_csv(r"E:\data python files\propertyprediction\train.csv")

#print(file.info())
#file=file.corr()
#file.to_csv("propertycorrelation.csv")
x_train=file[['OverallQual','GrLivArea']]
y_train=file[['SalePrice']]
model=LinearRegression()
model.fit(x_train,y_train)
print('coefficient of determination:', model.score(x_train,y_train))
print('intercept:', model.intercept_)
quality=int(input("Rate the overall material and finish of the house from 1 to 10: "))
area=int(input("Enter above grade (ground) living area square feet: "))
x_test=[[quality,area]]
y_test=model.predict(x_test)
print("Predicted sales price of house will be: ",int(y_test))
