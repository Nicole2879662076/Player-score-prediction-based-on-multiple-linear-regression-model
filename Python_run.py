import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import sklearn
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
import math
import seaborn as sns


sns.set_style('dark')
plt.subplots(figsize = (30,20))
mask = np.zeros_like(df1.corr(), dtype=np.bool)
mask[np.triu_indices_from(mask)] = True


sns.heatmap(df1.corr(), 
	cmap=sns.diverging_palette(20, 220, n=200), 
	mask = mask, 
	annot=True, 
	center = 0,
	)
# Give title. 
#plt.title("Heatmap of all the Variable", fontsize = 30)
#plt.savefig('sns_heatmap3.jpg')
train = pd.read_csv("/kaggle/input/trainn/train.csv")
train.dropna(inplace=True)
train.replace(np.inf, 0, inplace=True)
train


#partial residual
def partial_residual(i,j,bate):
	name = i
	x = train[i]
	y = bate*x+train[j]
	plt.xlabel(i)
	plt.ylabel("partial_residual")
	plt.scatter(x,y, c = "black", marker = "+",alpha=0.8)
	plt.savefig(f'{name}_8f.png')


#RStudent plot
plt.scatter(df["id"],train["Residual_8"], c = "black", marker = "*",alpha=0.58)
plt.title("RStudent plot: overal_rating")
plt.savefig('newRS.png')
test = pd.read_csv("/kaggle/input/ra-test-overfiting/test.csv")
test.dropna(inplace=True)
test.replace(np.inf, 0, inplace=True)


#test
def summary (y_test, y_predict):
	r_2 = sklearn.metrics.r2_score(y_test, y_predict)
 	sse = np.sum((y_test - y_predict) ** 2)
 	ssr = np.sum((y_predict - np.mean(y_test)) ** 2)
 	sst = np.sum((y_test - np.mean(y_test)) ** 2)
 	rmse = np.sqrt(mean_squared_error(y_test, y_predict))
	print("r_2 ",r_2, "rmse ",rmse, "sse ",sse, "ssr ",ssr, "sst ",sst)

intercept_8f = -6.36684
age_8f = 0.43885*test['age']
height_cm_8f = 0.00026926*test['height_cm']
weight_kgs_8f = 0.00642*test['weight_kgs']
value_8flog = 4.50456*(test['value_euro'].apply(np.log))
finishing_8f = -0.02848*test['finishing']
dribbling_8f = 0.00485*test['dribbling']
acceleration_8f = 0.00169*test['acceleration']
crossing_8f = 0.00696*test['crossing']

Y_8f = 
intercept_8f+age_8f+height_cm_8f+weight_kgs_8f+value_8flog+finishing_8f+dribbling_8
f+acceleration_8f+crossing_8f

summary(y_true,Y_8f