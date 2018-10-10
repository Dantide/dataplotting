# import plotly
import math
import numpy
import plotly.plotly as py
import plotly.graph_objs as go
# plotly.tools.set_credentials_file(username='Dantide', api_key='yxopUzjN78CLtRZ5Kl0i')


def parse_data(file_name: str):
    """Parse through a data file for section 1.1 of ECE 2100 lab 2."""
    assert(isinstance(file_name, str))
    file_path = open(file_name, 'r')
    file_path.readline()
    file_path.readline()
    voltage1 = []
    current1 = []
    log_current = []
    for line in file_path:
        data_list = line.split()
        if len(data_list) == 3:
            voltage1.append(float(data_list[0]))
            current1.append(float(data_list[1]))
            log_current.append(float(data_list[2]))
    file_path.close()
    return [voltage1, current1, log_current]


amber_lists = parse_data("1.1amb.txt")
amber_voltage1 = amber_lists[0]
amber_current1 = amber_lists[1]
amber_log_current = amber_lists[2]

blue_lists = parse_data("1.1ble.txt")
blue_voltage1 = blue_lists[0]
blue_current1 = blue_lists[1]
blue_log_current = blue_lists[2]

green_lists = parse_data("1.1grn.txt")
green_voltage1 = green_lists[0]
green_current1 = green_lists[1]
green_log_current = green_lists[2]

red_orange_lists = parse_data("1.1rdo.txt")
red_orange_voltage1 = red_orange_lists[0]
red_orange_current1 = red_orange_lists[1]
red_orange_log_current = red_orange_lists[2]

red_lists = parse_data("1.1red.txt")
red_voltage1 = red_lists[0]
red_current1 = red_lists[1]
red_log_current = red_lists[2]

royal_blue_lists = parse_data("1.1roy.txt")
royal_blue_voltage1 = royal_blue_lists[0]
royal_blue_current1 = royal_blue_lists[1]
royal_blue_log_current = royal_blue_lists[2]

white_lists = parse_data("1.1wht.txt")
white_voltage1 = white_lists[0]
white_current1 = white_lists[1]
white_log_current = white_lists[2]

warm_white_lists = parse_data("1.1wht-l.txt")
warm_white_voltage1 = warm_white_lists[0]
warm_white_current1 = warm_white_lists[1]
warm_white_log_current = warm_white_lists[2]


# Plotting Current vs Voltage
trace1 = go.Scatter(
    x=amber_voltage1,
    y=amber_current1,
    name='Amber LED',
    line=dict(
        color='rgb(255, 191, 0)',
        width=4,
        dash='dash')
)

trace2 = go.Scatter(
    x=blue_voltage1,
    y=blue_current1,
    name='Blue LED',
    line=dict(
        color='rgb(0, 0, 255)',
        width=4,
        dash='dash')
)

trace3 = go.Scatter(
    x=green_voltage1,
    y=green_current1,
    name='Green LED',
    line=dict(
        color='rgb(0, 255, 0)',
        width=4,
        dash='dash')
)

trace4 = go.Scatter(
    x=red_orange_voltage1,
    y=red_orange_current1,
    name='Red Orange LED',
    line=dict(
        color='rgb(255, 165, 0)',
        width=4,
        dash='dash')
)

trace5 = go.Scatter(
    x=red_voltage1,
    y=red_current1,
    name='Red LED',
    line=dict(
        color='rgb(255, 0, 0)',
        width=4,
        dash='dash')
)

trace6 = go.Scatter(
    x=royal_blue_voltage1,
    y=royal_blue_current1,
    name='Royal Blue LED',
    line=dict(
        color='rgb(65, 105, 255)',
        width=4,
        dash='dash')
)

trace7 = go.Scatter(
    x=white_voltage1,
    y=white_current1,
    name='White LED',
    line=dict(
        color='rgb(0, 0, 0)',
        width=4,
        dash='dash')
)

trace8 = go.Scatter(
    x=warm_white_voltage1,
    y=warm_white_current1,
    name='Warm White LED',
    line=dict(
        color='rgb(0, 0, 0)',
        width=4,
        dash='dot')
)

data = [trace1, trace2, trace3, trace4, trace5, trace6, trace7, trace8]
layout = dict(title="Terminal Characteristic LEDs",
              xaxis={'title': "Voltage (V)", 'gridcolor': '#bdbdbd'},
              yaxis={'title': "Current (A)", 'gridcolor': '#bdbdbd'},
              paper_bgcolor='rgba(255,255,255,1)',
              plot_bgcolor='rgba(255,255,255,1)',
              font={'color': "#000", 'size': 16}
)
fig = dict(data=data, layout=layout)
# py.plot(fig, filename="Lab 2.1.1: LED IV Plots")

def modeled_blue(i):
    I0 = 99e-9
    ktq = 25.86
    n = 0.5
    Rser = 0.7
    return n * ktq * math.log(i/I0) + i * Rser

# Plotting Blue with modeled data
trace1 = trace2

trace2 = go.Scatter(
    x=null,
    y=null,
    name='Modeled Blue LED',
    mode='lines'
)


# Plotting Log Current vs Voltage
trace1 = go.Scatter(
    x=amber_voltage1,
    y=amber_log_current,
    name='Amber LED',
    line=dict(
        color='rgb(255, 191, 0)',
        width=4,
        dash='dash')
)

trace2 = go.Scatter(
    x=blue_voltage1,
    y=blue_log_current,
    name='Blue LED',
    line=dict(
        color='rgb(0, 0, 255)',
        width=4,
        dash='dash')
)

trace3 = go.Scatter(
    x=green_voltage1,
    y=green_log_current,
    name='Green LED',
    line=dict(
        color='rgb(0, 255, 0)',
        width=4,
        dash='dash')
)

trace4 = go.Scatter(
    x=red_orange_voltage1,
    y=red_orange_log_current,
    name='Red Orange LED',
    line=dict(
        color='rgb(255, 165, 0)',
        width=4,
        dash='dash')
)

trace5 = go.Scatter(
    x=red_voltage1,
    y=red_log_current,
    name='Red LED',
    line=dict(
        color='rgb(255, 0, 0)',
        width=4,
        dash='dash')
)

trace6 = go.Scatter(
    x=royal_blue_voltage1,
    y=royal_blue_log_current,
    name='Royal Blue LED',
    line=dict(
        color='rgb(65, 105, 255)',
        width=4,
        dash='dash')
)

trace7 = go.Scatter(
    x=white_voltage1,
    y=white_log_current,
    name='White LED',
    line=dict(
        color='rgb(0, 0, 0)',
        width=4,
        dash='dash')
)

trace8 = go.Scatter(
    x=warm_white_voltage1,
    y=warm_white_log_current,
    name='Warm White LED',
    line=dict(
        color='rgb(0, 0, 0)',
        width=4,
        dash='dot')
)

data = [trace1, trace2, trace3, trace4, trace5, trace6, trace7, trace8]
layout = dict(title="Log Current vs Voltage LEDs",
              xaxis={'title': "Voltage (V)", 'gridcolor': '#bdbdbd'},
              yaxis={'title': "Current (A)", 'gridcolor': '#bdbdbd'},
              paper_bgcolor='rgba(255,255,255,1)',
              plot_bgcolor='rgba(255,255,255,1)',
              font={'color': "#000", 'size': 16})
fig = dict(data=data, layout=layout)
# py.plot(fig, filename="Lab 2.1.1: LED Log Current Plots")
