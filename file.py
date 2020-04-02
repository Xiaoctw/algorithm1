from helper import *
import matplotlib.pyplot as plt

if __name__ == '__main__':
    data = make_data(100, 1000)
    #print(data)
    left, right,not_left,not_right = enumerate_data(data)
    plt.scatter(x=left, y=right, c='r', lw=4)
    plt.scatter(x=not_left,y=not_right,c='b',lw=2)
    plt.title('The enumeration method')
    plt.show()
