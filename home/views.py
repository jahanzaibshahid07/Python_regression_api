from django.shortcuts import render,HttpResponse
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression


# y(cord) = y(intercept) + bx

def Table(request): 
    df = pd.read_csv('E:/predicted.csv') 
    geeks_object = df.to_html() 
    # # return HttpResponse(geeks_object)
    reg=LinearRegression()
    reg.fit(df[['Date']],df.Price)
    df=pd.read_csv("E:/preloc.csv")
    b1=df.to_html()
    p=reg.predict(df)
    df['Price']=p
    b3=df.to_html()
    pri={b3}
    mak=df.to_csv('E:/sred.csv')
    return HttpResponse(true)
    # return render(request,'index.html')
    
    # b3 = {geeks_object,b1,pre}
  