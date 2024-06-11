import sys
def main():




    #Training data
    #x0 corrosponds to the x coordinate
    #x1 corrosponds to the y coordinate
    x0 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    x1 = [5.3,8.3,11.3,14.3,17.3,20.3,23.3,26.3,29.3,32.3,35.3,38.3,41.3,44.3,47.3,50.3,53.3,56.3,59.3]
    y = [0,1,0,1,0,1,0,0,1,1]

    #Weights and biases
    w0 = 0.2
    w1 = -0.23
    b = 0.22


    #train single neuron network
    #Makes it learn on its own (10000 is just an example)
    for i in range (0,100000):
        loss = 0
        for j in range(0,len(y)):
            a = w0*x0[j] + w1 * x1[j] + b #
            loss += 0.5 * (y[j] - a)**2 #** is power 2. 50% multiplied by probability of 1 or 0(y is 0 or 1)
            dw0 = -(y[j]-a)*x0[j] #x0 is input, subtracts a by y[j]
            dw1 = -(y[j]-a)*x1[j] 
            db = -(y[j]-a)

            w0 = w0 - 0.0001 * dw0
            w1 = w1 - 0.0001 * dw1
            b = b - 0.0001 * db

        print('loss = ',loss)


    #testing code
    x0 = 2.7
    x1 = 6.0
    output = x0*w0 + x1*w1 + b
    print('output for (',x0,',',x1,') = ',output)

    x0 = 5.3 #Assumption of input
    x1 = 10.4 #Assumption of output
    output = x0*w0 + x1*w1 + b
    print('output for (',x0,',',x1,') = ',output)

if __name__ == "__main__": 
    sys.exit(int(main() or 0))
