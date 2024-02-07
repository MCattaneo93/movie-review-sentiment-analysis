import os
import sys
import numpy as np
import pandas as pd
#author - Matthew Cattaneo

accuracy = 0.0
script_folder = os.path.dirname(os.path.abspath(__file__))

class LogisticRegression():
    #default eta value set to .15 based on evaluation
    def __init__(self, eta=.15, iterations=1000):
        self.eta = eta
        self.iterations = iterations
        self.weights = None
        self.bias = None
    #save w and b to movie-review-BOW.LR
    def save_parameters(self):
        file = open("movie-review-BOW.LR", "w")
        for w_i in self.weights:
            file.write(str(w_i))
            file.write(" ")
        file.write("\n")
        file.write(str(self.bias))
        file.close
    #load parameters passed from main
    def load_parameters(self, w, b):
        self.weights = w
        self.bias = b
    #cross entropy loss function, used to determine if SGD converged
    def l_ce(self, weight,bias, index, X,Y):
        if(Y[index] == 1):
            return -1*np.log(sigmoid(np.dot(X[index],weight)+bias))
        else:
            return -1*np.log(1-sigmoid((np.dot(X[index],weight)+bias)))
    #Train parameters using given X (training vectors) and Y (given labels)
    def fit(self, X, Y):
        loss_list = []
        n_samples = X.shape[0]
        #this way for each iteration, random samples are used
        
        file = open(os.path.join(script_folder,"TRACE.TXT"), "w")
        #run for 1000 iterations
        for i in range(self.iterations):
            sum_loss = 0
            #using permutation to randomly select samples
            perm = np.random.permutation(n_samples)
            for j in perm:
                #calculate z using dot product
                score = np.dot(self.weights, X[j]) + self.bias
                #calculate probability using sigmoid
                y_hat = sigmoid(score)
                #derivative wrt w
                dw = (np.dot(X[j],(y_hat - Y[j])))
                #derivative wrt bias
                db = y_hat-Y[j]
                #update values
                self.weights = self.weights - self.eta*dw
                self.bias = self.bias - self.eta*db
                #calculatel oss for this example
                loss = self.l_ce(self.weights,self.bias,j,X,Y)
                #sum loss to calculate overall average
                sum_loss += loss
                
            loss_list.append(sum_loss/n_samples)
            #self.track_change(i,file, loss_list)
            #iterate until one complete pass of the training examples is complete
            #if the difference in loss between two iterations is less than .0005, then break
            if(i > 0 and (abs(loss_list[i] - loss_list[i-1]) < .0005)):
                break
        #save w and b after SGD
        self.save_parameters()

    def track_change(self,iteration,file,loss_list):
        change_in_loss = abs(loss_list[iteration] - loss_list[iteration-1])
        file.write(str(iteration))
        file.write("DIFFERENCE IN L_CE:\n")
        file.write(str(change_in_loss))
        file.write("\n")
        file.write("---------------------------------------------------------------------------------------------------------------------------------------------------------------\n")

    #complete predictions of test examples given
    def predict(self, X):
        scores = np.dot(self.weights, X.T) + self.bias
        predictions = sigmoid(scores)
        if(np.iterable(predictions)):
            return [1 if y_hat >.5 else 0 for y_hat in predictions]
        else:
            return 1 if predictions > .5 else 0
    #print out probabilities
    def score_print(self, X):
        scores = np.dot(self.weights, X.T) + self.bias
        predictions = sigmoid(scores)
        file = open("raw_scores.txt", "w")
        file.write(predictions)



def read_in_parameters():
    
    with open(os.path.join(script_folder,"movie-review-BOW.LR"),'r',encoding ="utf8", errors="ignore") as file:
        params = file.readlines()
    
    w = np.array([float(i) for i in params[0].split()])
    b = (float(params[1]))
    return w,b

def load_train_data(file_name):
    with open(os.path.join(script_folder,file_name),'r',encoding ="utf8", errors="ignore") as file:
        X = np.loadtxt(file,dtype=float)
    
    if(np.ndim(X)>=2):
        Y = X[:,0]
        X = X[:,1:]
    else:
        Y = X[0]
        X = X[1:]
    
    return X,Y


def load_test_data(file_name):
    with open(os.path.join(script_folder,file_name),'r',encoding ="utf8", errors="ignore") as file:
        X = np.loadtxt(file,dtype=float)
    if(np.ndim(X)>=2):
        Y = X[:,0]
        X = X[:,1:]
    else:
        Y = X[0]
        X = X[1:]
    return X,Y


def load_unsup_test_data(file_name):
    with open(os.path.join(script_folder,file_name),'r',encoding ="utf8", errors="ignore") as file:
        X = np.loadtxt(file,dtype=float)
    return X


def output_results(Y_HAT, Y):
    
    file = open("result.txt", "w")
    counter = 0
    
    for i, y_i in enumerate(Y_HAT):
        if(y_i == Y[i]):
            counter+=1

        file.write(str(i))
        file.write(" ")
        file.write(str(y_i))
        file.write(" ")
        file.write(str(Y[i]))
        file.write("\n")
    file.write("Accuracy: ")
    file.write(str(counter))
    file.write("/")
    file.write(str(len(Y_HAT)))
    file.write(" = ")
    file.write(str(counter/len(Y_HAT)*100))
    file.write("%")
    
    counter = float(counter)
    total = float(len(Y_HAT))
    my_accuracy = counter/total
    
    return my_accuracy

def output_incorrect_results(Y_HAT, Y, X):
    
    incorrect_FN = []
    incorrect_FP = []
    for i, y_i in enumerate(Y_HAT):
        if(y_i != Y[i]):
            if(y_i == 0):
                incorrect_FN.append(X[i])
            else:
                incorrect_FP.append(X[i])

    df1 = pd.DataFrame(incorrect_FN)
    df2 = pd.DataFrame(incorrect_FP)

    with pd.ExcelWriter('incorrect_FN.xlsx') as writer:
        df1.to_excel(writer, sheet_name='Sheet1', index=False)

    with pd.ExcelWriter('incorrect_FP.xlsx') as writer:
        df2.to_excel(writer, sheet_name='Sheet1', index=False)


def output_unsup_results(Y_HAT):
    file = open(os.path.join(script_folder,"result.txt"), "w")
    if(np.iterable(Y_HAT)):
        for i, y_i in enumerate(Y_HAT):
            file.write(str(i))
            file.write(" ")
            file.write(str(y_i))
            file.write("\n")            
    else:
        file.write(str(Y_HAT))
    

def sigmoid(z):
    return (1/(1+np.exp(-z)))

def main():
    lr = LogisticRegression()
    #process LR without any arguments
    if(len(sys.argv) <= 1):
        
        X,Y = load_train_data("train_data.txt")
        w = np.zeros(X.shape[1])
        lr.load_parameters(w,0)
        lr.fit(X, Y)
        X,Y = load_test_data("test_data.txt")
    #debug flag
    elif(sys.argv[1] == 'debug'):
        X,Y = load_train_data("train_data.txt")
        w = np.zeros(X.shape[1])
        lr.load_parameters(w,0)
        lr.fit(X, Y)
        X,Y = load_test_data("test_data.txt")
        Y_HAT = lr.predict(X)
        output_incorrect_results(Y_HAT,Y,X)
        return
    #unsup flag - if data to predict on doesnt have labels
    elif(sys.argv[1] == 'unsup'):
        w,b = read_in_parameters()
        lr.load_parameters(w,b)
        X,Y = load_train_data(sys.argv[2])
        lr.fit(X, Y)
        X = load_unsup_test_data(sys.argv[3])
        lr.score_print(X)
        Y_HAT = lr.predict(X)
        output_unsup_results(Y_HAT)
        return
    elif(len(sys.argv) == 2):
        
        w,b = read_in_parameters()
        lr.load_parameters(w,b)
        X,Y = load_test_data(sys.argv[1])
        
    elif(sys.argv[1] == '--loop'):
        
        lr = LogisticRegression(eta = float(sys.argv[2]))
        X,Y = load_train_data("train_data.txt")
        w = np.zeros(X.shape[1])
        lr.load_parameters(w,0)
        lr.fit(X, Y)
        X,Y = load_test_data("test_data.txt")
        
    else:
        w,b = read_in_parameters()
        lr.load_parameters(w,b)
        X,Y = load_train_data(sys.argv[1])
        lr.fit(X, Y)
        X,Y = load_test_data(sys.argv[2])
        

    Y_HAT = lr.predict(X)
    accuracy = output_results(Y_HAT, Y)
    
    return accuracy




if __name__ == "__main__":
    print(main())