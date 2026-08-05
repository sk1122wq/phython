# from sklearn import datasets
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score
# from sklearn.tree import DecisionTreeClassifier
# data=datasets.load_wine(as_frame=True)
# X=data.data
# Y=data.target
# X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.25,random_state=22)
# dtree=DecisionTreeClassifier(random_state=22)
# dtree.fit(X_train,Y_train)
# Y_pres=dtree.predict(X_test)
# print("Train data accuracy:",accuracy_score(y_true=Y_train,y_pred=dtree.predict(X_train)))
# print("Test data accuracy:",accuracy_score(y_true=Y_test,y_pred=Y_pres))
import matplotlib.pyplot as plt 
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.ensemble import BaggingClassifier

data=datasets.load_wine(as_frame=True)
X=data.data
Y=data.target

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.25,random_state=22)
estimator_range=[2,4,6,8,10,12,14,16]

models=[]
scores=[]
for n_estimators in estimator_range:
    clf=BaggingClassifier(n_estimators=n_estimators,random_state=22 , _init=8)
    clf.fit(X_train,Y_train)
    models.append(clf)
    scores.append(accuracy_score(y_true=Y_test,y_pred=clf.predict(X_test)))
    plt.figure(figsize=(9,6))
    plt.plot(estimator_range,scores)
    plt.xlabel("n_estimators",frontsize=18)
    plt.ylabels("score",frontsize=18)
    plt.tick_params(labelsize=18)
    plt.tick_params(labelsize=16)
    plt.show()

