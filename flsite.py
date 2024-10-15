import pickle
import tensorflow as tf
from model.neuron import SingleNeuron
import numpy as np
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

menu = [{"name": "Лаба 1", "url": "p_knn"},
        {"name": "Лаба 2", "url": "p_lab2"},
        {"name": "Лаба 3", "url": "p_lab3"},
        {"name": "Лаба 4", "url": "p_lab4"}]

loaded_model_knn = pickle.load(open('model/mushroom.fg', 'rb'))
loaded_model_lr = pickle.load(open('model/mushroom.fg', 'rb'))
loaded_model_dt = pickle.load(open('model/mushroom.fg', 'rb'))
# Загрузка весов из файла
new_neuron = SingleNeuron(input_size=3)
new_neuron.load_weights('model/neuron_weights.txt')
model_class = tf.keras.models.load_model('model/classification_model.h5')

@app.route("/")
def index():
    return render_template('index.html', title="Лабораторные работы, выполненные ФИО", menu=menu)


@app.route("/p_knn", methods=['POST', 'GET'])
def f_lab1():
    if request.method == 'GET':
        return render_template('lab1.html', title="Метод k -ближайших соседей (KNN)", menu=menu, class_model='')
    if request.method == 'POST':
        X_new = np.array([[float(request.form['list1']),
                           float(request.form['list2']),
                           float(request.form['list3'])]])
        pred = loaded_model_knn.predict(X_new)
        return render_template('lab1.html', title="Метод k -ближайших соседей (KNN)", menu=menu,
                               class_model="Это: " + pred)


@app.route("/p_lab2", methods=['POST', 'GET'])
def f_lab2():
    if request.method == 'GET':
        return render_template('lab2.html', title="Логистическая регрессия", menu=menu)

    if request.method == 'POST':
        X_new = np.array([[float(request.form['list1']),
                           float(request.form['list2']),
                           float(request.form['list3'])]])
        pred = loaded_model_lr.predict(X_new)
        return render_template('lab2.html', title="Логистическая регрессия", menu=menu,
                               class_model="Это: " + pred)


@app.route("/p_lab3", methods=['POST', 'GET'])
def f_lab3():
    if request.method == 'GET':
        return render_template('lab3.html', title="Дерево решений", menu=menu)

    if request.method == 'POST':
        X_new = np.array([[float(request.form['list1']),
                           float(request.form['list2']),
                           float(request.form['list3'])]])
        pred = loaded_model_dt.predict(X_new)
        return render_template('lab3.html', title="Дерево решений", menu=menu,
                               class_model="Класс: " + str(pred[0]))

@app.route("/p_lab4", methods=['POST', 'GET'])
def p_lab4():
    if request.method == 'GET':
        return render_template('lab4.html', title="Первый нейрон", menu=menu, class_model='')
    if request.method == 'POST':
        X_new = np.array([[float(request.form['list1']),
                           float(request.form['list2']),
                           float(request.form['list3'])
                           ]])
        predictions = new_neuron.forward(X_new)
        print("Предсказанные значения:", predictions, *np.where(predictions >= 0.5, 'Понедельник', 'Среда'))
        return render_template('lab4.html', title="Первый нейрон", menu=menu,
                               class_model="Это: " + str(*np.where(predictions >= 0.5, 'Понедельник', 'Среда')))

@app.route('/api_class', methods=['get'])
def predict_classification():
    # Получение данных из запроса http://localhost:5000/api_class?sun=1&temperature=25&wind=10
    input_data = np.array([[float(request.args.get('sun')),
                            float(request.args.get('temperature')),
                            float(request.args.get('wind'))]])
    print(input_data)
    # input_data = np.array(input_data.reshape(-1, 1))

    # Предсказание
    predictions = model_class.predict(input_data)
    print(predictions)
    result = 'Monday' if predictions >= 0.5 else 'Wednesday'
    print(result)
    # меняем кодировку
    app.config['JSON_AS_ASCII'] = False
    return jsonify(ov = str(result))


if __name__ == "__main__":
    app.run(debug=True)
