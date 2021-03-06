#Code based on Stanford Deep Learning ai, with some modifications for specific project
import os
import sys
import scipy.io
import scipy.misc
import matplotlib.pyplot as plt 
from matplotlib.pyplot import imshow 
from PIL import Image
from nst_utils import *
import numpy as np
import tensorflow as tf

#%matplotlib inline
#set up the vgg 19 model
model = load_vgg_model("pretrained-model/imagenet-vgg-verydeep-19.mat")
print(model)

def compute_content_cost(a_C, a_G): 
    """
        Computes the content cost
    Arguments:
        a_C -- tensor of dimension (1, n_H, n_W, n_C), hidden layer activations re
    presenting content of the image C
        a_G -- tensor of dimension (1, n_H, n_W, n_C), hidden layer activations re
    presenting content of the image G
        Returns:
        J_content -- scalar that you compute using equation 1 above.
    """

    # Retrieve dimensions from a_G (≈1 line)
    m, n_H, n_W, n_C = a_G.get_shape().as_list()
    # Reshape a_C and a_G (≈2 lines)
    a_C_unrolled = tf.reshape(a_C, shape= (m * n_H * n_W * n_C, 1))
    a_G_unrolled = tf.reshape(a_G, shape= (m * n_H * n_W * n_C, 1))
    # compute the cost with tensorflow (≈1 line)
    J_content = (1/(4 * n_H * n_W * n_C)) * tf.reduce_sum(tf.square(tf.subtract(a_C_unrolled, a_G_unrolled)))
    return J_content


tf.reset_default_graph()
with tf.Session() as test:
tf.set_random_seed(1)
a_C = tf.random_normal([1, 4, 4, 3], mean=1, stddev=4) 
a_G = tf.random_normal([1, 4, 4, 3], mean=1, stddev=4) 
J_content = compute_content_cost(a_C, a_G) 
print("J_content = " + str(J_content.eval()))


def gram_matrix(A): """
    Argument:
    A -- matrix of shape (n_C, n_H*n_W)
    Returns:
    GA -- Gram matrix of A, of shape (n_C, n_C)
    """
    
    GA = tf.matmul(A, A, transpose_b=True) ### END CODE HERE ###
    return GA


tf.reset_default_graph()
with tf.Session() as test:
tf.set_random_seed(1)
A = tf.random_normal([3, 2*1], mean=1, stddev=4) GA = gram_matrix(A)
print("GA = " + str(GA.eval()))

