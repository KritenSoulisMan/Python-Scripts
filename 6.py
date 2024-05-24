import os
import shutil
import tensorflow as tf

from tensorflow import keras



model = keras.Sequential([
    keras.layers.Dense(32, input_shape=(784,)),  # Полносвязный слой с 32 нейронами
    keras.layers.Activation('relu'),  # Функция активации ReLU
    keras.layers.Dense(10),  # Полносвязный слой с 10 нейронами
    keras.layers.Activation('softmax')  # Функция активации softmax
])


model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

train_features = [...]  # your training features data
train_labels = [...]    # your training labels data

model.fit(train_features, train_labels, epochs=10, batch_size=32)

unsuccessful_output = "your output"


result = model.predict(unsuccessful_output)


if not os.path.exists('trained_scripts'):
    os.mkdir('trained_scripts')
    
output = "Some output text"
with open('result.txt', 'w') as result_file:
    result_file.write(f"{filter}:\n{output}\n\n")


    
for file in os.listdir('.'):
    if file.endswith('.py'):
        shutil.copy(file, 'trained_scripts')

for file in os.listdir('trained_scripts'):
    if file.endswith('.py'):
        output = os.popen(f'python trained_scripts/{file}').read()

with open('result.txt', 'w') as result_file:
    result_file.write(f"{file}:\n{output}\n\n")


successful_scripts = 0
unsuccessful_scripts = 0

results = "200"
for line in results.split('\n'):
    if line.startswith('File'):
        script_name, output = line.split(':')
        output = output.strip()
    if output == 'Success':
        successful_scripts += 1
    else:
        unsuccessful_scripts += 1

print(f"Successful scripts: {successful_scripts}")
print(f"Unsuccessful scripts: {unsuccessful_scripts}")

