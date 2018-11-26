import plotly
import math
import plotly.plotly as py
import plotly.graph_objs as go
plotly.tools.set_credentials_file(username='Dantide', api_key='yxopUzjN78CLtRZ5Kl0i')

def parse_data(file_name: str):
    """Parse through a data file for section 2.1 of ECE 2100 lab 4."""
    assert(isinstance(file_name, str))
    file_path = open(file_name, 'r')
    file_path.readline()
    file_path.readline()
    voltage1 = []
    current1 = []
    voltage2 = []
    for line in file_path:
        data_list = line.split()
        if len(data_list) == 3:
            voltage1.append(float(data_list[0]))
            current1.append(float(data_list[1]))
            voltage2.append(float(data_list[2]))
    file_path.close()
    return [voltage1, current1, voltage2]


unload_lists = parse_data("4.2.1.b.txt")
unload_vin = unload_lists[0]
unload_vout = unload_lists[2]

load_lists = parse_data("4.2.1.d.txt")
load_vin = load_lists[0]
load_vout = load_lists[2]


trace1 = go.Scatter(
    x=unload_vin,
    y=unload_vout,
    name='Unloaded',
    line=dict(
        color='rgb(0,0,0)',
        width=4,
        dash='dash'
    )
)

trace2 = go.Scatter(
    x=load_vin,
    y=load_vout,
    name='Loaded',
    line=dict(
        color='rgb(0,0,0)',
        width=4,
        dash='dot'
    )
)

data = [trace1, trace2]
layout = dict(title="Voltage Transfer Characteristics of UA741CP",
              xaxis={'title': "Input Voltage (V)", 'gridcolor': '#bdbdbd'},
              yaxis={'title': "Output Voltage (V)", 'gridcolor': '#bdbdbd'},
              paper_bgcolor='rgba(255,255,255,1)',
              plot_bgcolor='rgba(255,255,255,1)',
              font={'color': "#000", 'size': 16})
fig = dict(data=data, layout=layout)
py.plot(fig, filename="Lab 4.2: Voltage Transfer Characteristics")
