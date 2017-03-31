#!/usr/bin/python
import sys, getopt
import os

from neuron import Neuron

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
DEFAULT_EPOCHS = 10000
DEFAULT_STEP = 0.001
TEST_FILE = CURRENT_DIR + '/samples/zad1/test.txt'
TRAIN_FILE = CURRENT_DIR + '/samples/zad1/train.txt'

def log(epochs, result, weights, step):
    """
    TODO: Move that function outside this file
    :param epochs:
    :param result:
    :param weights:
    :param step:
    :return:
    """
    print '\nepochs {}, result {}, \n' \
          'step {},\nweights {}'.format(epochs, result, step, weights)

def get_data_from_file(file_path):
    """
    TODO: Move that function outside this file
    :param file_path:
    :return:
    """
    data = []
    for line in open(file_path):
        data += [float(ch) for ch in line.rstrip()]
    return data

epochs = 1000
step = DEFAULT_STEP
train_file_path = TRAIN_FILE
test_file_path = TEST_FILE
try:
    opts, args = getopt.getopt(sys.argv[1:], "e", ["epochs"])
    for i, opt in enumerate(opts):
        if opt[0] == '-e': # epochs
            epochs = int(args[i])
        elif opt[0] == '-p': # train data - pattern
            train_file_path = args[i]
        elif opt[0] == '-t': # test data txt file path
            test_file_path = args[i]
        elif opt[0] == '-s': #step
            test_file_path = args[i]

except getopt.GetoptError:
    print 'default epochs is set'

# actual code starts here
train_pattern = get_data_from_file(train_file_path)
test_data = get_data_from_file(test_file_path)
neuron = Neuron()

train_pattern = (
    train_pattern, 1,
)

neuron.train(
    train_pattern, epochs, step
)
output = neuron.get_output(test_data)

log(epochs, output, neuron.weights, step)

# multiple training patterns
train_pattern = get_data_from_file(train_file_path)
train_pattern1 = get_data_from_file(train_file_path.replace('.t', '1.t'))
train_pattern2 = get_data_from_file(train_file_path.replace('.t', '2.t'))
train_pattern3 = get_data_from_file(train_file_path.replace('.t', '3.t'))
test_data = get_data_from_file(test_file_path)

neuron = Neuron()

train_pattern = [
    (train_pattern, 1),
    (train_pattern1, 2),
    (train_pattern2, 3),
    (train_pattern3, 4),
]

neuron.train(
    train_pattern, epochs, step
)
output = neuron.get_output(test_data)

log(epochs, output, neuron.weights, step)
