import matplotlib.pyplot as plt

def generatePieChart():
    labels = ['A', 'B', 'C']
    values = [200, 34, 152]

    fig, ax = plt.subplots()
    ax.pie(values, labels = labels)
    plt.savefig('pie.png')
    plt.close()
