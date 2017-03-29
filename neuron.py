"""
https://ftims.edu.p.lodz.pl/pluginfile.php/78898/mod_resource/content/2/zad_01_DELTA_en.pdf
It solves following 1 task which generally is:
    Write a program which implements a single linear neuron trained with the delta rule
with the use of (a) single and (b) multiple training patterns.
"""
class Neuron(object):
    """
    Class implements neuron using delta rule for both
    single and multiple patterns
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize function
        :param args:
        :param kwargs:
        """
        self.weights = []
        super(self, Neuron).__init__(*args, **kwargs)


    def initialize_weights(self, weights_count, weights_range):
        """
        Initialize weights with random values as mentioned in task description
        :param weights_count:
        :param weights_range:
        :return:
        """


    def train(self, training_set):
        """
        Train the neuron
        :param training_set:
        list of int values - single pattern
        list of list which contains int values - multiple pattern
        :return:
        """
        pass