import pandas as pd 
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC



columns=['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
file=pd.read_csv(r'E:\tech vision notes\25th june\ML Session 25th Jun\iris.data',names=columns)
#print(file.shape)
#print(file.info())
#print(file.describe())
array=file.values
#print(array)

x=array[:,0:4]
y=array[:,4]
#print(x)
#print(y)
x_train, x_test, y_train, y_test =model_selection.train_test_split(x, y, test_size=.20, random_state=7)
#print(len(x_train))
#print(len(x_test))
model = []
model.append(LogisticRegression())
model.append(DecisionTreeClassifier())
model.append(KNeighborsClassifier())
model.append(LinearDiscriminantAnalysis())
model.append(GaussianNB())

model.append(SVC())

print(model)
results=[]
for m in model:
     kfold = model_selection.KFold(n_splits=10, random_state=7)
     cv_results = model_selection.cross_val_score(m, x_train,y_train,cv=kfold,scoring='accuracy')
     #results.append(cv_results)
     #msg = "%f (%f)" % ( cv_results.mean(), cv_results.std())
     #print(msg)
     results.append([cv_results.mean(),cv_results.std()])
     
     


print(results)
