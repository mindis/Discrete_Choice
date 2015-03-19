# Script for running the logit_estimator
#
# Python 3.4 64 bit with SciPy

import numpy
import csv
from logit_estimator import LogitEstimator
# import pandas

project_location = 'D:\Cooper\Python\Discrete_Choice'
data_csv_file = project_location + '\\' + 'data.csv'

# Reading the csv using Pandas might be faster
# data_mat = pandas.io.parsers.read_csv(data_csv_file)

with open(data_csv_file) as file:
    reader = csv.reader(file)
    headers = next(reader)

data_mat = numpy.loadtxt(open(data_csv_file, 'rb'),
                         delimiter=',', skiprows=1, dtype='float')

print(headers)

logit_model = LogitEstimator.estimate_model(data_mat)