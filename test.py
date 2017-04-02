#!/usr/bin/python
import getopt
import json
import os
import time
import sys

from neuron import Neuron

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
DEFAULT_EPOCHS = 10000
DEFAULT_STEP = 0.001

def log(epochs, result, weights, step, precision):
    """
    TODO: Move that function outside this file
    :param epochs:
    :param result:
    :param weights:
    :param step:
    :return:
    """
    print '\nepochs {0}, result {1}, \n' \
          'step {2}, \nprecision {3}, \nweights {4}'.format(
        epochs, result, step, precision, weights,)

def get_data_from_file(file_path):
    """
    TODO: Move that function outside this file
    :param file_path:
    :return:
    """
    data = []
    for line in open(CURRENT_DIR + file_path):
        data += [float(ch) for ch in line.rstrip()]
    return data

def timing(f):
    def wrap(*args):
        time1 = time.time()
        ret = f(*args)
        time2 = time.time()
        print '%s function took %0.3f ms' % (f.func_name, (time2-time1)*1000.0)
        return ret
    return wrap

@timing
def neuron_response(neuron, test_data):
    """
    Measure neuron response time
    :param neuron:
    :param test_data:
    :return:
    """
    return neuron.get_output(test_data)

@timing
def neuron_training(neuron, train_pattern, epochs, step):
    """
    Measure neuron training time
    :param neuron:
    :param epochs:
    :param step:
    :return:
    """
    neuron.train(
        train_pattern, epochs, step
    )

with open('config.json') as data_file:
    config = json.load(data_file)

max_delta = float(config['max_delta'])
step = float(config['step'])

neuron = Neuron()
train_pattern = []
for i, train_file_path  in enumerate(config['train_paths']):
    train_pattern.append(
        (get_data_from_file(train_file_path), float(config['train_targets'][i])),
    )

neuron_training(neuron, train_pattern, max_delta, step)

for i, file_path  in enumerate(config['test_paths']):
    test_data = get_data_from_file(file_path)

    output = neuron_response(neuron, test_data)
    log(neuron.epochs, output, neuron.weights, step, max_delta)
