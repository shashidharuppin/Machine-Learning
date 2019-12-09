# Dependencies
import numpy as np
import matplotlib.pyplot as plt

class LinearRegression:

    def __init__(self, features, labels):
        # Parameters and Hyperparameters
        self.x = features
        self.y = labels

        self.w = 0
        self.b = 0

        self.learning_rate = 0.01
        self.rss = 0
        self.tss = 0
        self.r2 = 0
        self.prediction = 0
        self.cost_list = []
        self.Model()


    def hypothesis(self):
        # Linear Regression Equation
        self.prediction = self.x * self.w + np.full((5,), self.b)
        return self.prediction

    def cost(self):
        # Mean Squared Error
        mse = np.mean(np.square(self.y - self.prediction))
        return mse

    def Gradients(self):
        # Partial Derivatives
        djdw = -2 * (self.y - self.prediction) * self.x
        djdb = -2 * (self.y - self.prediction)
        return djdw, djdb

    def Optimization(self):
        self.w = self.w - self.learning_rate * self.Gradients()[0]
        self.b = self.b - self.learning_rate * self.Gradients()[-1]
    
    def r2_score(self):
        self.rss = np.sum(np.square(self.y-self.prediction))
        self.tss = np.sum(np.square(self.y-np.mean(self.y)))
        self.r2 = 1 -(self.rss/self.tss)
        return self.r2

    def Model(self):
        for i in range(50):
            self.hypothesis()
            self.cost()
            self.Optimization()
            self.cost_list.append(self.cost())
            self.r2_score()
            print("Step: {}".format(i))
            print("Actual Values: {}".format(self.y))
            print("Predicted Values: {}".format(self.hypothesis()))
            print("R squared Error: {}".format(self.r2))
            print("Mean Squared Error: {}\n\n\n\n".format(self.cost()))
            

def main():

    x = np.array([1, 2, 3, 4, 5])
    y = x * 2 + 3

    regressor = LinearRegression(x, y)
    cost = regressor.cost_list
    
    x_val = range(len(cost))
    plt.plot(x_val, cost)
    plt.title("Training")
    plt.xlabel("Step")
    plt.ylabel("Cost Function")
    plt.show()

if __name__=="__main__":
    main()