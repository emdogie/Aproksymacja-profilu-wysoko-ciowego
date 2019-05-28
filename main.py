import numpy
import csv
N = 512
distance = numpy.zeros(N)
height = numpy.zeros(N)

def load_data(filename):
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                distance[line_count-1] = row[0]
                height[line_count-1] = row[1]
                line_count+=1


load_data('GlebiaChallengera.csv')
print(distance)