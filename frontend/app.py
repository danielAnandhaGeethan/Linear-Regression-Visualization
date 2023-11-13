import pickle as pkl 
import streamlit as st
import numpy as np
import plotly.express as px
import time
import matplotlib.pyplot as plt

with open('../backend/model/model.pkl', 'rb') as file:
    model = pkl.load(file)

file.close()

st.set_option('deprecation.showPyplotGlobalUse', False)

def plot(height, slope, intercept):
    height = int(height)
    weight = model.predict(np.array([height]).reshape(-1,1))

    x_line = np.linspace(120, 200, 100)
    y_line = slope * x_line + intercept

    fig = px.scatter(x=x_line, y=y_line, labels={'x': 'X-axis', 'y': 'Y-axis'})
    fig.add_trace(px.scatter(x=[height], y=[weight], color=[5], size=[10]).data[0])  

    st.plotly_chart(fig)
    st.write('(View fullscreen for analysis)')

    return weight

def simulate_long_running_task():
    time.sleep(1)  

def main():
    
    st.markdown("<h1 style='text-align: center;'>Linear Regression Visualization</h1>", unsafe_allow_html = True)

    st.markdown("<h3 style='text-align: center; color: #8f8f8f'>Height vs Weight (NBA Players)</h3>", unsafe_allow_html = True)

    st.write("")

    slope = model.coef_[0]
    intercept = model.intercept_

    height = st.text_input(label = 'Enter Your Height (cm)')
    
    with st.columns(3)[1]:
        button = st.button('Get Weight', use_container_width = True)

    st.write("")

    if button:

        if not height or not height.isdigit():
            st.error('No Input')

        elif int(height) < 120:
            st.info('NBA players have a minimum height of 120 cm')

        else:
            with st.spinner("Running task..."):
                simulate_long_running_task()

                weight = plot(height, slope, intercept)

                weight = round(weight[0], 2)
                st.markdown(f"<h2 style='text-align: center;'>{weight} kg</h2>", unsafe_allow_html = True)

if __name__ == "__main__":
    main()