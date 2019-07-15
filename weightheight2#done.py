import pandas as pd
import numpy as np 
from sklearn.linear_model import LinearRegression 


x=int(input('for weight and height in kgs and foot enter 1 or enter 2 for pounds and inch:'))

if x==1:
    try:
        wh=pd.read_csv(r'E:\data python files\weight-height2.csv')
    except:
        print('File is not found on your PC!')
    x_male1=wh.iloc[:5000, 1].values
    x_female1=wh.iloc[5000:, 1].values
    x_male = np.array(x_male1).reshape((-1, 1))
    x_female = np.array(x_female1).reshape((-1, 1))

    y_male=wh.iloc[:5000, 2].values
    y_female=wh.iloc[5000:, 2].values


    gender=int(input("enter 1 for male and 2 for female:"))
    model=LinearRegression()
    if gender==1:
        model.fit(x_male,y_male)
        r_sq = model.score(x_male, y_male)
        print('coefficient of determination:', r_sq)

        print('intercept:', model.intercept_)

    if gender==2:
        model.fit(x_female,y_female)
        r_sq = model.score(x_female, y_female)
        print('coefficient of determination:', r_sq)

        print('intercept:', model.intercept_)


    newdata =[]
    for i in range(1,4):
          h = float(input('enter height(ft): '))
          newdata.append(h)

          
    x_new = np.array(newdata).reshape((-1, 1))
    y_new = model.predict(x_new)
    print(y_new,'kg')


elif x==2:
    try:
        wh=pd.read_csv(r'E:\data python files\weight-height.csv')
    except:
        print('File not found on your PC!')
    x_male1=wh.iloc[:5000, 1].values
    x_female1=wh.iloc[5000:, 1].values
    x_male = np.array(x_male1).reshape((-1, 1))
    x_female = np.array(x_female1).reshape((-1, 1))

    y_male=wh.iloc[:5000, 2].values
    y_female=wh.iloc[5000:, 2].values


    gender=int(input("enter 1 for male and 2 for female"))
    model=LinearRegression()
    if gender==1:
        model.fit(x_male,y_male)
        r_sq = model.score(x_male, y_male)
        print('coefficient of determination:', r_sq)

        print('intercept:', model.intercept_)

    if gender==2:
        model.fit(x_female,y_female)
        r_sq = model.score(x_female, y_female)
        print('coefficient of determination:', r_sq)

        print('intercept:', model.intercept_)


    newdata =[]
    for i in range(1,4):
          h = float(input('enter height(in) : '))
          newdata.append(h)

          
    x_new = np.array(newdata).reshape((-1, 1))
    y_new = model.predict(x_new)
    print(y_new,'pound')

else:
    print('only 1 and 2 is acceptable')
