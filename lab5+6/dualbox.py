import plotly
import math
import numpy
import plotly.plotly as py
import plotly.graph_objs as go
plotly.tools.set_credentials_file(username='Dantide', api_key='yxopUzjN78CLtRZ5Kl0i')

R_1 = 369.42633 * (10 ** 3) # Ohms
R_2 = 68.566569 * (10 ** 3) # Ohms
R_3 = 25.0 * (10 ** 3) # Ohms
R_4 = 475.0 * (10 ** 3) # Ohms
R_5 = 419.06241 * (10 ** 3) # Ohms
R_6 = 60.445164 * (10 ** 3) # Ohms
R_7 = 25.0 * (10 ** 3) # Ohms
R_8 = 475.0 * (10 ** 3) # Ohms
C_1 = C_2 = C_3 = C_4 = C = 1.0 * (10 ** -9) # Farads


def transfer_function(freq_list) :
    magnitude = []
    phase = []
    for freq in freq_list:
        o = 2 * math.pi * freq
        R_EQ = (2 * R_2 * R_3) / (2 * R_1 * R_3 - R_2 * R_4)
        H = ((R_3 + R_4) / R_3) * (-o ** 2 / (-(o ** 2))
                                   + complex((o * (2 / (R_EQ * C)) + 1 / (R_1 * R_2 * (C ** 2)))))
        print(H)
        magnitude.append(abs(H))
        phase.append(1)
    [magnitude, phase]


def parse_data(file_name):
    """Parse through a data file for dualport data for ECE 2100 lab 5."""
    assert (isinstance(file_name, str))
    file_path = open(file_name, 'r')
    file_path.readline()
    frequency = []
    voltage_in = []
    voltage_out = []
    voltage_transfer = []
    phase = []
    for line in file_path:
        data_list = line.split()
        if len(data_list) == 6:
            frequency.append(float(data_list[0]))
            voltage_in.append(float(data_list[1]))
            voltage_out.append(float(data_list[2]))
            voltage_transfer.append(float(data_list[3]))
            phase.append(float(data_list[4]))
    file_path.close()
    return [frequency, voltage_in, voltage_out, voltage_transfer, phase]


dual_port_lists = parse_data("dualbox.txt")
dual_port_freq = dual_port_lists[0]
dual_port_transfer = dual_port_lists[3]
dual_port_phase = dual_port_lists[4]

freq_list = numpy.logspace(1, 5, num=100)
modeled_data = transfer_function(freq_list)
model_mag = modeled_data[0]
model_phs = modeled_data[1]


trace1 = go.Scatter(
    x=dual_port_freq,
    y=dual_port_transfer,
    name="Dual Port Response",
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

trace2 = go.Scatter(
    x=freq_list,
    y=modeled_mag,
    name="Modelled Response",
    mode='lines',
    line=dict(
        color='rgb(200,0,0)',
        width=4
    )
)

data = [trace1, trace2]
layout = dict(
    title="Voltage Transfer Function vs Log Frequency",
    xaxis=dict(
        title="Log Input Frequency",
        gridcolor='#bdbdbd',
        type='log',
        dtick='D1',
        ticks='outside',
        autorange=True,
        exponentformat='power',
        linecolor='black',
        linewidth=1,
        mirror=True,
        titlefont=dict(
            size=24
        )
    ),
    yaxis=dict(
        title="Voltage Transfer Function",
        gridcolor='#bdbdbd',
        autorange=True,
        linecolor='black',
        linewidth=1,
        mirror=True,
        titlefont=dict(
            size=24
        )
    ),
    paper_bgcolor='rgba(255,255,255,1)',
    plot_bgcolor='rgba(255,255,255,1)',
    font=dict(
        color='#000',
        size=16
    )
)
fig = dict(data=data, layout=layout)
py.plot(fig, filename="Lab 5: Dual Port Voltage Transger Function")


trace1 = go.Scatter(
    x=dual_port_freq,
    y=dual_port_phase,
    name='Dual Port Response',
    mode='lines+markers',
    line=dict(
        color='rgb(0,0,0)',
        width=4
    ),
    marker=dict(
        color='rgb(0,0,0)',
        size=7
    )
)

trace2 = go.Scatter(
    x=freq_list,
    y=modeled_phs,
    name="Modelled Response",
    mode='lines',
    line=dict(
        color='rgb(200,0,0)',
        width=4
    )
)

data = [trace1, trace2]
layout = dict(
    title="Transfer Function Phase vs Log Frequency",
    xaxis=dict(
        title="Log Input Freqency",
        gridcolor='#bdbdbd',
        type='log',
        dtick='D1',
        ticks='outside',
        autorange=True,
        exponentformat='power',
        linecolor='black',
        linewidth=1,
        mirror=True,
        titlefont=dict(
            size=24
        )
    ),
    yaxis=dict(
        title="Transfer Function Phase",
        gridcolor='#bdbdbd',
        autorange=True,
        linecolor='black',
        linewidth=1,
        mirror=True,
        titlefont=dict(
            size=24
        )
    ),
    paper_bgcolor='rgba(255,255,255,1)',
    plot_bgcolor='rgba(255,255,255,1)',
    font=dict(
        color='#000',
        size=16
    )
)
fig = dict(
    data=data,
    layout=layout
)
py.plot(fig, filename="Lab 5: Dual Box Voltage Transfer Function Phase")
