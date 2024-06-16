import matplotlib.pyplot as plt
from sklearn.datasets import make_regression

import tensorflow as tf
import pandas as pd

x,y=make_regression(n_samples=50,bias=50,noise=15,random_state=1,n_features=1)
x=x.ravel()
df=pd.DataFrame({'y':y,'x':x},index=range(1,51))
figure,axes=plt.subplots()
plt.scatter(x,y)
line,=axes.plot(x,[0]*len(x),color='g')

def predict(x):
    return w*x+b

def loss(y,y_predict):
    return tf.reduce_mean(tf.square(y-y_predict))

def draw(w,b):
    y_new=[w*xplot +b for xplot in x]
    line.set_data(x,y_new)
    plt.show()

def train(x,y,epochs:int=20,learning_rate:float=0.5):
    current_loss=0
    for epoch in range(epochs):
        with tf.GradientTape() as t:
            current_loss=loss(y,predict(x))
            dw,db=t.gradient(current_loss,[w,b])
            print(f'dw:{dw},db:{db}')
            w.assign_sub(learning_rate*dw)
            b.assign_sub(learning_rate*db)
            draw(w,b)
            print(f'Epoch:{epoch},Loss:{current_loss.numpy()}')

w=tf.Variable(0.0)
b=tf.Variable(0.0)
train(x,y,5)
print(f'w={w.numpy()},b={b.numpy()}')
plt.show()