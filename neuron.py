import random
"""
https://ftims.edu.p.lodz.pl/pluginfile.php/78898/mod_resource/content/2/zad_01_DELTA_en.pdf
It solves following 1st task which generally is:
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
        super(Neuron, self).__init__(*args, **kwargs)


    def initialize_weights(self, weights_range_lower, weights_range_upper, no):
        """
        Initialize weights with random values as mentioned in task description
        :param weights_range_lower:
        :param weights_range_upper:
        :param no: number of inputs
        :return:
        """
        for i in xrange(0, no):
            self.weights.append(
                random.uniform(
                    weights_range_lower,
                    weights_range_upper
                )
            )

    def get_output(self, inputs):
        """
        Calculate Neuron output
        :param inputs:
        :return:
        """
        sum = 0.0
        for i, input in enumerate(inputs):
            sum += input * self.weights[i]

        return sum

    def train(
            self,
            training_sets,
            epochs=10000,
            step=0.01,
            w_lower=1,
            w_upper=2,
    ):
        """
        Train the neuron
        :param training_set:
        tuple - single pattern
        ([input1, input2, ..., inputN], Z - expected neuron output)
        or list of tuples above for multiple patterns
        :param training_set:
        :param epochs:
        :param step:
        :param w_lower:
        :param w_upper:
        :return:
        """
        if isinstance(training_sets, tuple):
            training_sets = [training_sets]
        self.initialize_weights(w_lower, w_upper, len(training_sets[0][0]))
        for k in xrange(epochs):
            for training_input in training_sets:
                neuron_inputs = training_input[0]
                expected_out = training_input[1]
                neuron_out = self.get_output(neuron_inputs)

                for i, weight in enumerate(self.weights):
                    delta = expected_out - neuron_out
                    # modifying weight
                    self.weights[i] += step * delta * neuron_inputs[i]
