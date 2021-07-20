import plotly.figure_factory as ff
import pandas as pd
import statistics
import csv
import random

df=pd.read_csv("population.csv")
population_mean=statistics.mean(data)
print("Population mean is:",population_mean)

def random_set_of_mean(counter):
  data_set=[]
  for i in range(0,30):
    random_index=random.randint(0,len(data))
    value=data[random_index]
    data_set.append(value)
  mean=statistics.mean(data_set)
  return mean

def show_fig(mean_list):
  df=mean_list
  fig=ff.create_distplot([df],["temp"],show_hist=False)
  fig.show()

def setup():
  mean_list = []
  for i in range(0,100):
    set_of_means=random_set_of_mean(30)
    mean_list.append(set_of_means)
    sampling_mean=statistics.mean(mean_list)

print("Sampling mean is:",sampling_mean)
  
  show_fig(mean_list)