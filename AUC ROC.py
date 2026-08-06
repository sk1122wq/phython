# import numpy as np
# from sklearn.metrics import accuracy_score, confusion_matrix, roc_auc_score,roc_curve
# n=10000
# ratio=.95
# n_0=int ((1-ratio)*n)
# n_1=int(ratio*n)
# y=np.array([0]*n_0+[1]*n_1)
# y_proba=np.array([1]*n)
# y_pred=y_proba> .5
# print(f'accuracy score:{accuracy_score(y,y_pred)}')
# cf_mat=confusion_matrix(y,y_pred)
# print('confusion matrix')
# print(cf_mat)
# print(f'class 0 accuracy:{cf_mat[0][0]/n_0}')
# print(f'class 1 accuracy :{cf_mat[1][1]/n_1}')
# import numpy as np
# from sklearn.metrics import accuracy_score, confusion_matrix, roc_auc_score,roc_curve
# n=10000
# ratio=.95
# n_0=int ((1-ratio)*n)
# n_1=int(ratio*n)
# y=np.array([0]*n_0+[1]*n_1)
# y_proba_2=np.array(np.random.uniform(0,.7,n_0).tolist()+np.random.uniform(.3,1,n_1).tolist())
# y_pred_2=y_proba_2> .5
# print(f'accuracy score:{accuracy_score(y,y_pred_2)}')
# cf_mat=confusion_matrix(y,y_pred_2)
# print('confusion matrix')
# print(cf_mat)
# print(f'class 0 accuracy:{cf_mat[0][0]/n_0}')
# print(f'class 1 accuracy :{cf_mat[1][1]/n_1}')
import matplotlib.pyplot as plt 
from sklearn.metrics import roc_curve, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import datasets 
data=datasets.load_breast_cancer()
x=data.data
y=data.target
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=22)
model=LogisticRegression(max_iter=10000)
model.fit(x_train,y_train)
y_proba=model.predict_proba(x_test)[:,1]
def plot_roc_curve(true_y,y_prob):
    """   plots the roc curve based of the probabilities"""
    fpr, tpr, thresholds= roc_curve(true_y,y_prob)
    plt.figure(figsize=(8,6))
    plt.plot(fpr,tpr,marker='o',label='Model')
    plt.plot([0,1],[0,1],linestyle='--',color='red',label='Random')
    plt.xlabel('False positive Rate ')
    plt.ylabel('True positive Rate')
    plt.title('Roc Curve')
    plt.legend()
    plt.grid(True)
    plt.show()
plot_roc_curve(y_test,y_proba)
print(f'model 1 AUC score :{roc_auc_score(y_test,y_proba):.4f}')

