import pandas as pd 

from sklearn.linear_model import LinearRegression 

file=pd.read_csv(r'E:\tech vision notes\24th june\mtcars.csv')
#file1=file.corr()
#file1.to_csv('corr in cars.csv')
x = file[['cyl','disp','hp','wt']]
y = file['mpg']

model=LinearRegression()

model.fit(x,y)

print('coefficient of determination:', model.score(x,y))
print('intercept:', model.intercept_)

cyl=int(input('enter no. of cylinders:'))
disp=float(input('enter disp:'))
hp=int(input('enter hp:'))
wt=float(input('enter weight:'))
x_new=[[cyl,disp,hp,wt]]
y_new=model.predict(x_new)
print('the predicted mpg will be:',y_new)

