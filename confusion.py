# import matplotlib.pyplot as plt 
# import numpy
# from sklearn import metrics 
# actual=numpy.random.binomial(1,.9,size=1000)
# predicted=numpy.random.binomial(1,.9,size=1000)
# confusion_matrix=metrics.confusion_matrix(actual,predicted)
# cm_display=metrics.ConfusionMatrixDisplay(confusion_matrix=confusion_matrix, display_labels=[0,1])
# cm_display.plot()
# plt.show()
# import numpy
# from sklearn import metrics 
# actual=numpy.random.binomial(1,.9,size=1000)
# predicted=numpy.random.binomial(1,.9,size=1000)
# Accuracy=metrics.accuracy_score(actual,predicted)
# print(Accuracy)
# import numpy
# from sklearn import metrics 
# actual=numpy.random.binomial(1,.9,size=1000)
# predicted=numpy.random.binomial(1,.9,size=1000)
# precision=metrics.precision_score(actual,predicted)
# print(precision)
# import numpy
# from sklearn import metrics 
# actual=numpy.random.binomial(1,.9,size=1000)
# predicted=numpy.random.binomial(1,.9,size=1000)
# sensitivity_recall=metrics.recall_score(actual,predicted)
# print(sensitivity_recall)
# import numpy
# from sklearn import metrics 
# actual=numpy.random.binomial(1,.9,size=1000)
# predicted=numpy.random.binomial(1,.9,size=1000)
# specificity=metrics.recall_score(actual,predicted,pos_label=0)
# print(specificity)
# import numpy
# from sklearn import metrics 
# actual=numpy.random.binomial(1,.9,size=1000)
# predicted=numpy.random.binomial(1,.9,size=1000)
# F1_score=metrics.f1_score(actual,predicted)
# print(F1_score)
import numpy
from sklearn import metrics 
actual=numpy.random.binomial(1,.9,size=1000)
predicted=numpy.random.binomial(1,.9,size=1000)
Accuracy=metrics.accuracy_score(actual,predicted)
precision=metrics.precision_score(actual,predicted)
sensitivity_recall=metrics.recall_score(actual,predicted)
specificity=metrics.recall_score(actual,predicted,pos_label=0)
F1_score=metrics.f1_score(actual,predicted)
print({"Accuracy":Accuracy,"precision":precision,"sensitivity_recall":sensitivity_recall,"specificity":specificity})