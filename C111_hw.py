from typing import final
import pandas as pd
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go
import random

file = pd.read_csv('School2.csv')

data = file['Math_score'].tolist()

mean = statistics.mean(data)

def findmeans():
    meanlist=[]

    for i in range(0,100):
        meanlist.append(data[random.randint(0,len(data)-1)])

    meanlistmean = statistics.mean(meanlist)

    return meanlistmean



def setup():
    finalmeanlist=[]

    for x in range(0,1000):
        finalmeanlist.append(findmeans())

    samplemean = statistics.mean(finalmeanlist)
    samplestd = statistics.stdev(finalmeanlist)

    fstd_s,fstd_e = samplemean - samplestd , samplemean + samplestd

    sstd_s,sstd_e = samplemean - 2*samplestd , samplemean + 2*samplestd

    tstd_s,tstd_e = samplemean - 3*samplestd , samplemean + 3*samplestd

    print('first std end:',fstd_e)
    print('second std end:',sstd_e)
    print('third std end:',tstd_e)

    file2 = pd.read_csv('School_2_Sample.csv')

    data2 = file2['Math_score'].tolist()

    newsamplemean = statistics.mean(data2)
    newsamplestd = statistics.stdev(data2)

    zscore = (newsamplemean - samplemean) / samplestd

    print('Z SCORE : ',zscore)


    graph = ff.create_distplot([finalmeanlist],['final mean list'])

    graph.add_traces(go.Scatter(x=[samplemean,samplemean],y=[0,0.2],mode='lines',name='Mean of final meanlist'))
    graph.add_traces(go.Scatter(x=[fstd_e,fstd_e],y=[0,0.2],mode='lines',name='fstd_e'))
    graph.add_traces(go.Scatter(x=[sstd_e,sstd_e],y=[0,0.2],mode='lines',name='sstd_e'))
    graph.add_traces(go.Scatter(x=[tstd_e,tstd_e],y=[0,0.2],mode='lines',name='tstd_e'))
    graph.add_traces(go.Scatter(x=[newsamplemean,newsamplemean],y=[0,0.2],mode='lines',name='new sample mean'))

    graph.show()


setup()