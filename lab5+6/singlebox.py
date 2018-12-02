import plotly
import math
import plotly.plotly as py
import plotly.graph_objs as go
plotly.tools.set_credentials_file(username='Dantide', api_key='yxopUzjN78CLtRZ5Kl0i')

def parse_data(file_name):
    """Parse through a data file for section 1.1 of ECE 2100 lab 4."""
    assert(isinstance(file_name, str))
    file_path = open(file_name, 'r')
    file_path.readline()
    frequency = []
    voltage_in = []
    current_in = []
    impedance = []
    phase = []
    for line in file_path:
        data_list = line.split()
        if len(data_list) == 5:
            frequency.append(float(data_list[0]))
            voltage_in.append(float(data_list[1]))
            current_in.append(float(data_list[2]))
            impedance.append(float(data_list[3]))
            phase.append(float(data_list[4]))
    file_path.close()
    return [frequency, current_in, voltage_in, impedance, phase]


single_box_lists = parse_data("singlebox.txt")
single_box_freq = single_box_lists[0]
single_box_current = single_box_lists[1]
single_box_voltage = single_box_lists[2]
single_box_impedance = single_box_lists[3]
single_box_phase = single_box_lists[4]

single_box_log_freq = list(map(lambda x: math.log10(x), single_box_freq))
single_box_log_impedance = list(map(lambda x: math.log10(x), single_box_impedance))


trace1 = go.Scatter(
    x=single_box_freq,
    y=single_box_impedance,
    name='Single Box Responce',
    mode='lines+markers',
    line=dict(
        color='rgb(0,0,0)',
        width=4
    ),
    marker=dict(
        size=7,
        color='rgb(0,0,0)'
    )
)

data = [trace1]
layout = dict(title="Log Impedance Magnitude vs Log Frequency",
              xaxis={'title': "Log Input Frequency", 'gridcolor': '#bdbdbd',
                     'type': 'log', 'dtick': "D1", 'ticks': 'outside',
                     'autorange': True, 'exponentformat': 'power'},
              yaxis={'title': "Log Impedance Magnitude (Ohms)", 'gridcolor': '#bdbdbd',
                     'type': 'log', 'exponentformat': 'power', 'autorange': True},
              paper_bgcolor='rgba(255,255,255,1)',
              plot_bgcolor='rgba(255,255,255,1)',
              font={'color': "#000", 'size': 16})
fig = dict(data=data, layout=layout)
py.plot(fig, filename="Lab 5: Single Box Impedance Magnitude")


trace1 = go.Scatter(
    x=single_box_freq,
    y=single_box_phase,
    name='Single Box Responce',
    mode='lines+markers',
    line=dict(
        color='rgb(0,0,0)',
        width=4,
    ),
    marker=dict(
        size=7,
        color='rgb(0,0,0)'
    )
)

data = [trace1]
layout = dict(title="Impedance Phase vs Log Frequency",
              xaxis={'title': "Log Input Frequency", 'gridcolor': '#bdbdbd',
                     'type': 'log', 'dtick': "D1", 'ticks': 'outside',
                     'autorange': True, 'exponentformat': 'power'},
              yaxis={'title': "Impedance Phase", 'gridcolor': '#bdbdbd',
                     'autorange': True},
              paper_bgcolor='rgba(255,255,255,1)',
              plot_bgcolor='rgba(255,255,255,1)',
              font={'color': "#000", 'size': 16})
fig = dict(data=data, layout=layout)
py.plot(fig, filename="Lab 5: Single Box Impedance Phase")
