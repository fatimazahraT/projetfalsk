import matplotlib.pyplot as plt

class Graphe:
    @staticmethod
    def generate_graph(x_data, y_data, title, xlabel, ylabel):
        plt.plot(x_data, y_data)
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.grid(True)
        plt.show()
