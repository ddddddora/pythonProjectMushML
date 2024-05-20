import pickle
import pandas as pd
import numpy as np
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

menu = [{"name": "Лаба 1", "url": "p_knn"},
        {"name": "Лаба 2", "url": "p_lab2"},
        {"name": "Лаба 3", "url": "p_lab3"}]

loaded_model_knn = pickle.load(open('model/mushroom.fg', 'rb'))
loaded_model_lr = pickle.load(open('model/mushrooms_file', 'rb'))
loaded_model_dt = pickle.load(open('model/mush', 'rb'))

@app.route("/")
def index():
    return render_template('index.html', title="Лабораторные работы, выполненные Капшуковой Дарьей", menu=menu)


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
                               class_model="Это: " + pred[0])


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
                               class_model="Это: " + pred[0])


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

@app.route('/api_knn', methods=['get'])
def get_sort():
    X_new = np.array([[float(request.args.get('length_leg')),
                       float(request.args.get('diameter_hat')),
                       float(request.args.get('thickness_leg'))]])
    pred = loaded_model_knn.predict(X_new)
    return jsonify(sort=pred[0])

@app.route('/api_knnv2', methods=['get'])
def get_sort_v2():
    request_data = request.get_json()
    X_new = np.array([[float(request_data['length_leg']),
                       float(request_data['diameter_hat']),
                       float(request_data['thickness_leg'])]])
    pred = loaded_model_knn.predict(X_new)

    return jsonify(sort=pred[0])

@app.route('/api_lr', methods=['get'])
def get_sort():
    X_new = np.array([[float(request.args.get('length_leg')),
                       float(request.args.get('diameter_hat')),
                       float(request.args.get('thickness_leg'))]])
    pred = loaded_model_lr.predict(X_new)
    return jsonify(sort=pred[0])

@app.route('/api_lrv2', methods=['get'])
def get_sort_v2():
    request_data = request.get_json()
    X_new = np.array([[float(request_data['length_leg']),
                       float(request_data['diameter_hat']),
                       float(request_data['thickness_leg'])]])
    pred = loaded_model_lr.predict(X_new)

    return jsonify(sort=pred[0])

@app.route('/api_dr', methods=['get'])
def get_sort():
    X_new = np.array([[float(request.args.get('length_leg')),
                       float(request.args.get('diameter_hat')),
                       float(request.args.get('thickness_leg'))]])
    pred = loaded_model_lr.predict(X_new)
    return jsonify(sort=pred[0])

@app.route('/api_drv2', methods=['get'])
def get_sort_v2():
    request_data = request.get_json()
    X_new = np.array([[float(request_data['length_leg']),
                       float(request_data['diameter_hat']),
                       float(request_data['thickness_leg'])]])
    pred = loaded_model_lr.predict(X_new)

    return jsonify(sort=pred[0])

if __name__ == "__main__":
    app.run(debug=True)
