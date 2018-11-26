import plotly
import math
import plotly.plotly as py
import plotly.graph_objs as go
plotly.tools.set_credentials_file(username='Dantide', api_key='yxopUzjN78CLtRZ5Kl0i')

def parse_data(file_name: str):
    """Parse through a data file for section 1.1 of ECE 2100 lab 4."""
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


ua_lists = parse_data("4.1.1.b.txt")
ua_vin = ua_lists[0]
ua_iin = ua_lists[1]
ua_logcurrent = list(map(lambda x: math.log10(x), ua_iin))
ua_vout = ua_lists[2]

lf_lists = parse_data("4.1.2.txt")
lf_vin = lf_lists[0]
lf_iin = lf_lists[1]
lf_logcurrent = list(map(lambda x: math.log10(x) if (x > 0) else "None", lf_iin))
lf_vout = lf_lists[2]


trace1 = go.Scatter(
    x=ua_vin,
    y=ua_vout,
    name='UA741CP',
    line=dict(
        color='rgb(0,0,0)',
        width=4,
        dash='dash'
    )
)

trace2 = go.Scatter(
    x=lf_vin,
    y=lf_vout,
    name='LF353',
    line=dict(
        color='rgb(0,0,0)',
        width=4,
        dash='dot'
    )
)

data = [trace1, trace2]
layout = dict(title="Open Loop Op Amp Response",
              xaxis={'title': "Input Voltage (V)", 'gridcolor': '#bdbdbd'},
              yaxis={'title': "Output Voltage (V)", 'gridcolor': '#bdbdbd'},
              paper_bgcolor='rgba(255,255,255,1)',
              plot_bgcolor='rgba(255,255,255,1)',
              font={'color': "#000", 'size': 16})
fig = dict(data=data, layout=layout)
py.plot(fig, filename="Lab 4.1: Open Loop Op Amp Response")


trace1 = go.Scatter(
    x=ua_logcurrent,
    y=ua_vin,
    name='UA741CP',
    line=dict(
        color='rgb(0,0,0)',
        width=4,
        dash='dash'
    )
)

trace2 = go.Scatter(
    x=lf_logcurrent,
    y=lf_vin,
    name='LF353',
    line=dict(
        color='rgb(0,0,0)',
        width=4,
        dash='dot'
    ),
    connectgaps=True
)

data = [trace1, trace2]
layout = dict(title="Log Input Current vs Input Voltage",
              xaxis={'title': "Log Current", 'gridcolor': '#bdbdbd'},
              yaxis={'title': "Output Voltage (V)", 'gridcolor': '#bdbdbd'},
              paper_bgcolor='rgba(255,255,255,1)',
              plot_bgcolor='rgba(255,255,255,1)',
              font={'color': "#000", 'size': 16})
fig = dict(data=data, layout=layout)
py.plot(fig, filename="Lab 4.1: Op Amp's Input Current and Input Resistance")
