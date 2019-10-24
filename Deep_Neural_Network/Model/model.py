from prepearing import *
import matplotlib.pyplot as plt
from tensorflow.keras.layers import *
from tensorflow.keras.models import *
from tensorflow.keras.optimizers import *
from tensorflow.keras.regularizers import *
from keras.callbacks import EarlyStopping

x, y = prepearing('train.csv')
count_examples = len(y)
count_train = int(count_examples * 0.9)
x_train = np.array(x[:count_train])
y_train = np.array(y[:count_train])
x_test = np.array(x[count_train + 1:])
y_test = np.array(y[count_train + 1:])
# print("Printing training data count: {0}".format(len(x_train)))
# for t in range(len(x_train)):
#     print(x_train[t], y_train[t])
# print("Printing test data count: {0}".format(len(x_test)))
# for t in range(len(x_test)):
#     print(x_test[t], y_test[t])

# # Создаём, компилируем,обучаем и сохраняем модель
# model = Sequential()
# model.add(Dense(45, input_dim=45, activation='sigmoid'))
# model.add(Dense(45, activation='sigmoid'))
# model.add(Dense(3, activation='softmax'))
# model.compile(loss='binary_crossentropy', optimizer=Adam(lr=0.0001), metrics=['accuracy'])
# early_loss = EarlyStopping(monitor='val_loss', patience=50)
# history = model.fit(x_train, y_train, epochs=1000, batch_size=2, validation_data=(x_test, y_test), callbacks=[early_loss], verbose=2, shuffle=True)
# model.save('motive.h5')
# model.evaluate(x_test, y_test, batch_size=1, verbose=1)
# # Выводим % обучения модели
# print("Точность: {0}".format(np.mean(history.history["val_acc"])))
#
# # Рисуем график ответов
# plt.plot(history.history['acc'])
# plt.plot(history.history['val_acc'])
# plt.title('Model accuracy')
# plt.ylabel('Accuracy')
# plt.xlabel('Epoch')
# plt.legend(['Train', 'Test'], loc='upper left')
# plt.show()
#
# # Рисуем график ошибок
# plt.plot(history.history['loss'])
# plt.plot(history.history['val_loss'])
# plt.title('Model loss')
# plt.ylabel('Loss')
# plt.xlabel('Epoch')
# plt.legend(['Train', 'Test'], loc='upper left')
# plt.show()


model = load_model('motive_the_best.h5')
for i in range(100):
    to_predict = []
    to_predict.append(x_test[i])
    print(model.predict(np.array(to_predict)), y_test[i])