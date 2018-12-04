import plotly
import math
import numpy
import plotly.plotly as py
import plotly.graph_objs as go
plotly.tools.set_credentials_file(username='Dantide', api_key='yxopUzjN78CLtRZ5Kl0i')


def parse_data(file_name):
    """Parse through a data file for singleport data for ECE 2100 lab 5."""
    assert (isinstance(file_name, str))
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

R_L_SER: float = 3  # Ohms
L: float = 1.246 * (10 ** -3)  # Henry's
ind_break_freq: float = 383.198  # Hz
C: float = 1.4246 * (10 ** -9)  # Farads
R: float = 959  # Ohms


def impedance_model(freq_list):
    magnitude = []
    phase = []
    for freq in freq_list:
        omega = 2 * math.pi * freq
        if True:
            denom: float = (R + R_L_SER) ** 2 + (omega * L - (1 / (omega * C))) ** 2
            real: float = (R * (R_L_SER ** 2 + (omega * L) ** 2) +
                           R_L_SER * (R ** 2 + (1 / ((omega * C) ** 2)))) / denom
            imaj: float = (omega * (R ** 2) * L -
                           (R_L_SER ** 2 / (omega * C)) -
                           (L / C) * (omega * L - (1 / (omega * C)))) / denom
            mag: float = math.sqrt(real ** 2 + imaj ** 2)
            ang: float = (math.atan(imaj / real) / (2 * math.pi)) * 360

            magnitude.append(mag)
            phase.append(ang)
    return [freq_list, magnitude, phase]


freq_sweep = numpy.logspace(1, 6, num=100)
modeled_data = impedance_model(freq_sweep)
modeled_magnitude = modeled_data[1]
modeled_phase = modeled_data[2]


trace1 = go.Scatter(
    x=single_box_freq,
    y=single_box_impedance,
    name='Single Box Response',
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
    x=freq_sweep,
    y=modeled_magnitude,
    name='Modelled Circuit',
    mode='lines',
    line=dict(
        color='rgb(200,0,0)',
        width=4,
    ),
)

data = [trace1, trace2]
layout = dict(title="Log Impedance Magnitude vs Log Frequency",
              xaxis=dict(
                  title="Log Input Frequency",
                  gridcolor='#bdbdbd',
                  type='log',
                  dtick="D1",
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
                  title="Log Impedance Magnitude (Ohms)",
                  gridcolor='#bdbdbd',
                  type='log',
                  exponentformat='power',
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
              font={'color': "#000", 'size': 16})
fig = dict(data=data, layout=layout)
# py.plot(fig, filename="Lab 5: Single Box Impedance Magnitude")

trace1 = go.Scatter(
    x=single_box_freq,
    y=single_box_phase,
    name='Single Box Response',
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

trace2 = go.Scatter(
    x=freq_sweep,
    y=modeled_phase,
    name='Modelled Circuit',
    mode='lines',
    line=dict(
        color='rgb(200,0,0)',
        width=4,
    ),
)

data = [trace1, trace2]
layout = dict(title="Impedance Phase vs Log Frequency",
              xaxis=dict(
                  title="Log Input Frequency",
                  gridcolor='#bdbdbd',
                  type='log',
                  dtick="D1",
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
                  title="Impedance Phase",
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
              font={'color': "#000", 'size': 16})
fig = dict(data=data, layout=layout)
# py.plot(fig, filename="Lab 5: Single Box Impedance Phase")


trace1 = go.Scatter(
    x=single_box_freq,
    y=single_box_impedance,
    name='Single Box Response',
    mode='lines+markers',
    line=dict(
        color='rgb(0,0,0)',
        width=4,
        dash='solid'
    ),
    marker=dict(
        size=7,
        color='rgb(0,0,0)'
    )
)

trace2 = go.Scatter(
    x=freq_sweep,
    y=modeled_magnitude,
    name='Modelled Circuit',
    mode='lines',
    line=dict(
        color='rgb(200,0,0)',
        width=4,
        dash='solid'
    ),
)

trace3 = go.Scatter(
    x=single_box_freq,
    y=single_box_phase,
    name='Single Box Response',
    mode='lines+markers',
    line=dict(
        color='rgb(0,0,0)',
        width=4,
        dash='dot'
    ),
    marker=dict(
        size=7,
        color='rgb(0,0,0)'
    ),
    yaxis='y2'
)

trace4 = go.Scatter(
    x=freq_sweep,
    y=modeled_phase,
    name='Modelled Circuit',
    mode='lines',
    line=dict(
        color='rgb(200,0,0)',
        width=4,
        dash='dot'
    ),
    yaxis='y2'
)

data = [trace1, trace2, trace3, trace4]
layout = dict(title="Measured and Model Data",
              xaxis=dict(
                  title="Log Input Frequency",
                  gridcolor='#bdbdbd',
                  type='log',
                  dtick="D1",
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
                  title="Log Impedance Magnitude (Ohms)",
                  gridcolor='#bdbdbd',
                  type='log',
                  exponentformat='power',
                  autorange=True,
                  linecolor='black',
                  linewidth=1,
                  mirror=True,
                  titlefont=dict(
                      size=24
                  )
              ),
              yaxis2=dict(
                  title="Impedance Phase",
                  gridcolor='#bdbdbd',
                  autorange=True,
                  linecolor='black',
                  linewidth=1,
                  mirror=True,
                  titlefont=dict(
                      size=24
                  ),
                  overlaying='y',
                  side='right'
              ),
              paper_bgcolor='rgba(255,255,255,1)',
              plot_bgcolor='rgba(255,255,255,1)',
              font={'color': "#000", 'size': 16})
fig = dict(data=data, layout=layout)
py.plot(fig, filename="Lab 5: Single Box Everything")
