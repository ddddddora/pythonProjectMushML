import tensorflow as tf
import numpy as np

X_class = np.array([[18, 0, 5],
                    [22, 1, 10]])
y_class = np.array([1, 0])

# Создание модели для классификации
model_class = tf.keras.Sequential([
    tf.keras.layers.Dense(3, input_shape=(3,)),
    tf.keras.layers.Dense(3),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

model_class.compile(optimizer='adam', loss='binary_crossentropy')

# Обучение модели
model_class.fit(X_class, y_class, epochs=100)

# Прогноз
test_data = np.array([[20, 1, 10]])
y_pred_class = model_class.predict(test_data)
print("Предсказанные значения:", y_pred_class, *np.where(y_pred_class >= 0.5, 'Понедельник', 'Среда'))
# Сохранение модели для классификации
model_class.save('classification_model.h5')