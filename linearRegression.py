import numpy as np
import matplotlib.pyplot as plt

def coefficient_est(x, y): 
    ## number of observations/points 
    n = np.size(x) 
  
    ## mean of house_size(x) and price(y) vector 
    meanX, meanY = np.mean(x), np.mean(y) 
  
    ## calculating cross-deviation and deviation about x 
    SS_xy = np.sum(y*x) - n*meanY*meanX 
    SS_xx = np.sum(x*x) - n*meanX*meanX 
  
    ## calculating regression coefficients 
    B1 = SS_xy / SS_xx 
    B0 = meanY - B1*meanX 
  
    return(B0, B1) 
  
def regressionLine(x, y, b): 
    ## plotting the actual points as red colored stars 
    plt.scatter(x, y, color = "red", 
               marker = "*", s = 40) 
  
    ## prediction response vector 
    y_pred = b[0] + b[1]*x 
  
    ## plotting the regression line with purple color
    plt.plot(x, y_pred, color = "purple") 
  
    ## putting house size in x-axis and prise in y-axis
    plt.xlabel('house_size') 
    plt.ylabel('prize') 
  
    ## for showing the result 
    plt.show() 
  
def main(): 
    ## Data 
    x = np.array([1, 2, 3, 5,8, 10, 12, 14]) 
    y = np.array([300, 500, 450, 590, 700, 880, 1000, 1100]) 
  
    ## estimating coefficients 
    b = coefficient_est(x, y) 
    print("Estimated coefficients:\nb_0 = {}  \nb_1 = {}".format(b[0], b[1])) 
  
    ## plotting regression line 
    regressionLine(x, y,b) 
  
if __name__ == "__main__": 
    main() 
