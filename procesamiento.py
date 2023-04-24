import numpy as np

class Process:
    def __init__(self, weights, options):
        self.options = options
        self.weights = np.array(weights)
    
    def activation_fn(self, x):
        # Función de activación sigmoidea
        return 1 / (1 + np.exp(-x))
    
    def predict(self, x):
        # Calcula la suma ponderada de los valores de entrada y los pesos
        z = np.dot(x, self.weights)
        # Aplica la función de activación sigmoidea y devuelve el resultado
        y_pred = self.activation_fn(z)
        return y_pred
    
    def make_decision(self):
        # Define las opciones y sus respectivos pesos
        options = self.options
        # Calcula la probabilidad de cada opción utilizando la red neuronal
        probabilities = [self.predict(np.array(weights)) for weights in self.weights]
        # Devuelve la opción con la probabilidad más alta
        decision = options[np.argmax(probabilities)]
        return decision

