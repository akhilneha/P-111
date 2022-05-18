import csv
import pandas as pd
import random
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go 

df = pd.read_csv("studentMarks.csv")
data = df["Math_score"].tolist()

def random_set_of_mean(counter):
    dataset = []
    for i in range(0,counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    Mean = statistics.mean(dataset)   
    return Mean

meanList = []

for i in range(0,1000):
    set_of_means = random_set_of_mean(100)
    meanList.append(set_of_means)

finalMean = statistics.mean(meanList)
finalStandardDeviation = statistics.stdev(meanList)

print(finalMean)     
print(finalStandardDeviation) 

Group1 = pd.read_csv("data1.csv")
score_Group1 = Group1["Math_score"].tolist()
mean_of_Group1=statistics.mean(score_Group1)

Group2 = pd.read_csv("data2.csv")
score_Group2 = Group2["Math_score"].tolist()
mean_of_Group2=statistics.mean(score_Group2)

Group3 = pd.read_csv("data3.csv")
score_Group3 = Group3["Math_score"].tolist()
mean_of_Group3=statistics.mean(score_Group3)

z_score1 = (mean_of_Group1-finalMean)/finalStandardDeviation
print(z_score1)

z_score2 = (mean_of_Group2-finalMean)/finalStandardDeviation
print(z_score2)

z_score3 = (mean_of_Group3-finalMean)/finalStandardDeviation
print(z_score3)

fig = ff.create_distplot([meanList],["studentMarks"],show_hist=False)
fig.add_trace(go.Scatter(x=[finalMean,finalMean],y=[0,0.2],mode="lines",name="MeanLine"))
fig.add_trace(go.Scatter(x=[mean_of_Group1,mean_of_Group1],y=[0,0.2],mode="lines",name="Group given ipads"))
fig.add_trace(go.Scatter(x=[mean_of_Group2,mean_of_Group2],y=[0,0.2],mode="lines",name="Group given 2 hours of extra classes"))
fig.add_trace(go.Scatter(x=[mean_of_Group3,mean_of_Group3],y=[0,0.2],mode="lines",name="Group given worksheets"))
fig.show()