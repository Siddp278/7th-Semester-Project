from django.shortcuts import render
import tensorflow as tf
from tensorflow import Graph
from keras.preprocessing.sequence import pad_sequences
import pickle
from .processing import normalization_pipeline
max_len = 50


model_graph = Graph()
with model_graph.as_default():
    tf_session = tf.compat.v1.Session() # Session()
    with tf_session.as_default():
        model = tf.keras.models.load_model(r'polls/7ProjectModel.h5')


def predict(request):
    response = {}
    result = None
    tokenizerSequence = pickle.load(open(r'polls/tokenizerSequencing.pickle', 'rb'))
    if request.method == 'POST':
        sentence = request.POST['sentence']
        sentence = normalization_pipeline([sentence])
        sequence = tokenizerSequence.texts_to_sequences(sentence)
        pad_sequence = pad_sequences(sequence, maxlen=max_len)
        with model_graph.as_default():
            with tf_session.as_default():
                result = model.predict_proba(pad_sequence)
                print(result)
        response = helperFunction(result[0])
    else:
        print("Error")

    return render(request, 'index.html', {'response': response})


def helperFunction(x):
    if max(x) == x[0]:
        return {'neutral': x[0]}
    elif max(x) == x[1]:
        return {'positive': x[1]}
    else:
        return {'negative': x[2]}