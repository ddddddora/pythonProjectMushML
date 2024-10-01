import numpy as np
from neuron import SingleNeuron


# Пример данных (X - входные данные, y - целевые значения)
X = np.array([[14, 0, 10],
              [25, 1, 15]])
y = np.array([1, 0])  # Ожидаемый выход
# Инициализация и обучение нейрона
neuron = SingleNeuron(input_size=3)
neuron.train(X, y, epochs=5000, learning_rate=0.1)

# Сохранение весов в файл
neuron.save_weights('neuron_weights.txt')