

import pandas as pd
import seaborn as sns

train_df=pd.read_csv('/content/Star3642_balanced.csv')

train_df.head()

train_df.info()

train_df.describe()

new_train_df=train_df.drop(columns='SpType')

new_train_df

corr = train_df[['TargetClass','SpType']].corr()

sns.heatmap(corr)

corr1=new_train_df.corr()

sns.heatmap(corr1,annot=True);

X=new_train_df.drop(['TargetClass'],axis=1)
y=new_train_df['TargetClass']

from sklearn.model_selection import train_test_split
X_train , X_test , y_train , y_test = train_test_split(X,y,test_size=0.2)

from sklearn.linear_model import RidgeClassifier
khalid=RidgeClassifier()
clf = khalid.fit(X_train, y_train)
clf.score(X_train,y_train)

clf.predict(X_test)
clf.score(X_test,y_test)

from sklearn import svm
clf=svm.SVC()
aziz=clf.fit(X_train,y_train)
aziz.score(X_train,y_train)

