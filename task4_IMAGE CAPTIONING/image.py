from tensorflow.keras.layers import Input, Dense, Embedding, LSTM
from tensorflow.keras.layers import Dropout, add
from tensorflow.keras.models import Model

image_input = Input(shape=(2048,))
image_layer = Dropout(0.5)(image_input)
image_layer = Dense(256, activation='relu')(image_layer)

caption_input = Input(shape=(34,))
caption_layer = Embedding(5000, 256, mask_zero=True)(caption_input)
caption_layer = LSTM(256)(caption_layer)

decoder = add([image_layer, caption_layer])
decoder = Dense(256, activation='relu')(decoder)
output = Dense(5000, activation='softmax')(decoder)

model = Model([image_input, caption_input], output)
model.compile(loss='categorical_crossentropy',
              optimizer='adam')
