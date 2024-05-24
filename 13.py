import cv2
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

# Загрузка и предобработка данных
images = []
labels = []

POSITIVE_DIR = "data/positive" # Изображения с окном Minecraft
NEGATIVE_DIR = "data/negative" # Изображения без окна Minecraft 

for img in os.listdir(POSITIVE_DIR):
  # Добавляем изображение и метку 1
  images.append(cv2.imread(os.path.join(POSITIVE_DIR,img)))
  labels.append(1)

for img in os.listdir(NEGATIVE_DIR):
  # Добавляем изображение и метку 0
  images.append(cv2.imread(os.path.join(NEGATIVE_DIR,img))) 
  labels.append(0)
  
images = np.array(images)
labels = np.array(labels)

# Создание и обучение модели
model = Sequential()
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(150, 150, 3)))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(32, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())
model.add(Dense(1, activation='sigmoid'))

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(images, labels, epochs=5, batch_size=32)

# Использование модели
image = cv2.imread('screen.png')
prediction = model.predict(np.array([image]))[0][0] 

if prediction > 0.5:
  print("Minecraft window detected!")
else:
  print("Minecraft window not detected.")
