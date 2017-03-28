'''
Created on Mar 28, 2017

@author: leem42

visualizer.py creates a visual representation of the admissions data for a set of college students in 
various departments with their admission status.

'''

import pandas as pd
import plotly as py
import plotly.graph_objs as go

def main():
#     df = pd.read_csv("admissions.csv")
    
    x = ["Astronomy", "Biology","Law", "Physics","Psychology","Sociology"]

#===============================================================================
#     Boys Acceptance Rate
#===============================================================================
    trace1 = {
      'x': x,
      'y': [0.620606061, 0.058981233, 0.330935252, 0.630357143,0.369230769,0.277486911],
      'name': 'Males',
      'type': 'bar'
    };
#===============================================================================
#     Girls Acceptance Rate
#===============================================================================
    trace2 = {
      'x': x,
      'y': [-0.824074074, -0.070381232, -0.349333333, -0.68,-0.340640809,-0.239185751],
      'name': 'Females',
      'type': 'bar'
    };

#===============================================================================
#     Boys Rejection Rate
#===============================================================================
    trace3 = {
      'x': x,
      'y': [0.379393939, 0.941018767, 0.669064748, 0.369642857, 0.630769231,0.722513089],
      'name': 'Males',
      'type': 'bar'
    };
#===============================================================================
#     Girls Rejection Rate
#===============================================================================
    trace4 = {
      'x': x,
      'y': [-0.175925926, -0.929618768, -0.650666667,-0.32,-0.659359191, -0.760814249],
      'name': 'Females',
      'type': 'bar'
    };    


#     trace3 = {
#       'x': x,
#       'y': [-15, -3, 4.5, -8],
#       'name': 'Trace3',
#       'type': 'bar'
#      }
#      
#     trace4 = {
#       'x': x,
#       'y': [-1, 3, -3, -4],
#       'name': 'Trace4',
#       'type': 'bar'
#      }
#      
    data = [trace1, trace2];
    layout = {
      'xaxis': {'title': 'Department'},
      'yaxis': {'title': 'Rate'},
      'barmode': 'relative',
      'title': 'Admission Acceptance'
    };

    py.offline.plot({'data': data, 'layout': layout}, filename='barmode-acceptance.html')

    data2 = [trace3, trace4];
    layout = {
      'xaxis': {'title': 'Department'},
      'yaxis': {'title': 'Ratio'},
      'barmode': 'relative',
      'title': 'Admission Rejection'
    };

    py.offline.plot({'data': data2, 'layout': layout}, filename='barmode-rejection.html')


#     data = [go.Bar(
#                 x=['giraffes', 'orangutans', 'monkeys'],
#                 y=[20, 14, 23]
#         )]
#     py.offline.plot(data, filename='basic-bar.html')

if __name__ == '__main__':
    main()