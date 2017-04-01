#!/usr/bin/python
import getopt
import json
import os
import sys

from neuron import Neuron

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
DEFAULT_EPOCHS = 10000
DEFAULT_STEP = 0.001

def log(epochs, result, weights, step):
    """
    TODO: Move that function outside this file
    :param epochs:
    :param result:
    :param weights:
    :param step:
    :return:
    """
    print '\nepochs {0}, result {1}, \n' \
          'step {2},\nweights {3}'.format(epochs, result, step, weights)

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

with open('config.json') as data_file:
    config = json.load(data_file)

epochs = int(config['epochs'])
step = float(config['step'])

neuron = Neuron()
train_pattern = []
for i, train_file_path  in enumerate(config['train_paths']):
    train_pattern.append(
        (get_data_from_file(train_file_path), float(config['train_targets'][i])),
    )

neuron.train(
    train_pattern, epochs, step
)

for i, file_path  in enumerate(config['test_paths']):
    test_data = get_data_from_file(file_path)

    output = neuron.get_output(test_data)
    log(epochs, output, neuron.weights, step)
