import numpy as np

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
import keras


# TODO: fill out the function below that transforms the input series 
# and window-size into a set of input/output pairs for use with our RNN model
def window_transform_series(series,window_size):
    # containers for input/output pairs
    X = []
    y = []
    
    for i in range(0, len(series) - window_size):
        X.append(series[i:i + window_size])
        y.append(series[i+window_size])
    # reshape each 
    X = np.asarray(X)
    X.shape = (np.shape(X)[0:2])
    y = np.asarray(y)
    y.shape = (len(y),1)
    
    return X,y

# TODO: build an RNN to perform regression on our time series input/output data
def build_part1_RNN(step_size, window_size):
	# given - fix random seed - so we can all reproduce the same results on our default time series
    np.random.seed(0)

	# TODO: build an RNN to perform regression on our time series input/output data
    model = Sequential()
    model.add(LSTM(5, input_shape=(window_size, 1)))
    model.add(Dense(1))
    pass


### TODO: list all unique characters in the text and remove any non-english ones
def clean_text(text):
    import string
    # find all unique characters in the text
    uniq_char = list(set(text))

    punc_list = [' ', '!', ',', '.', ':', ';', '?']
    # remove as many non-english characters and character sequences as you can 
    for ch in uniq_char:
        if ch not in string.ascii_lowercase and ch not in punc_list:
            text = text.replace(ch, '')
    
    # shorten any extra dead space created above
    text = text.replace('  ',' ')


### TODO: fill out the function below that transforms the input text and window-size into a set of input/output pairs for use with our RNN model
def window_transform_text(text,window_size,step_size):
    # containers for input/output pairs
    inputs = []
    outputs = []
    
    for l in range(0, len(text), step_size):
        if l+window_size >= len(text):
            break
        inputs.append(text[l:l+window_size])
        outputs.append(text[l+window_size])
    
    return inputs,outputs
