import numpy as np
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten
from tensorflow.keras.utils import to_categorical

# Вставьте данные здесь
input_data = np.array([your_input_data])  # Replace this with your input data
output_labels = np.array([your_output_labels])  # Replace this with your output labels

# Скалярный преобразователь для нормализации данных
scaler = MinMaxScaler()
scaled_input_data = scaler.fit_transform(input_data)

# Модель с учитыванием падения на входе и выходе
model = Sequential([
    Dense(128, activation='relu'),
    Dropout(0.5),  # Уменьшаем вероятность перекрестного обучения
    Dense(64, activation='relu'),
    Dropout(0.3),
    Dense(len(output_labels) + 1, activation='softmax')
])

# Обучение модели на данных с использованием метода максимального правдоподобия (MSE)
model.compile(optimizer=Adam(learning_rate=0.001), loss='categorical_crossentropy', metrics=[Accuracy()])  # Учёт точности на основе категориального кроссэнтропийского потери (ACC)

# Подготовка данных для модели
X = np.reshape(scaled_input_data, (X.shape[0], X.shape[1] // 2))
y = to_categorical(output_labels)

# Обучение модели на входных данных и вычисление точности по мере обучения
history = model.fit(X, y, epochs=50, verbose=1)

# Вывод точности модели на основе категориального кроссэнтропийского потери (ACC) во время обучения
for i in range(len(output_labels)):
    print("Epoch:", history.epoch, "Accuracy:", output_labels[i], "->", y_true[i])
