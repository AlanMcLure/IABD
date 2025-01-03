from sklearn.preprocessing import LabelBinarizer
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Flatten, Dense, Dropout

# Cargar datos MNIST
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

# Normalizar las imágenes al rango [0, 1]
x_train, x_test = x_train / 255.0, x_test / 255.0

# Codificar etiquetas con one-hot
label_binarizer = LabelBinarizer()
label_binarizer.fit(range(10))  # Las clases son 0-9
y_train_onehot = label_binarizer.transform(y_train)
y_test_onehot = label_binarizer.transform(y_test)

print("Etiqueta original:", y_train[0])  # Ejemplo: 7
print("One-hot:", y_train_onehot[0])  # Ejemplo: [0, 0, 0, 0, 0, 0, 0, 1, 0, 0]

# Definir el modelo
model = Sequential([
    Flatten(input_shape=(28, 28)),  # Aplanar las imágenes 28x28 a un vector de 784
    Dense(128, activation='relu'),  # Capa totalmente conectada con 128 neuronas y ReLU
    Dropout(0.2),  # Capa de regularización para evitar sobreajuste
    Dense(10, activation='softmax')  # Capa de salida con 10 clases y softmax
])

# Compilar el modelo
model.compile(optimizer='adam',
              loss='categorical_crossentropy',  # Para etiquetas one-hot
              metrics=['accuracy'])

# Entrenar el modelo
model.fit(x_train, y_train_onehot, epochs=5, validation_data=(x_test, y_test_onehot))

# Evaluar el modelo
test_loss, test_acc = model.evaluate(x_test, y_test_onehot)
print(f"Precisión en el conjunto de prueba: {test_acc * 100:.2f}%")
