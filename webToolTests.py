# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 14:52:47 2022

@author: william.chupp
"""

# importing modules
import streamlit as st
import pandas as pd
import numpy as np
from st_aggrid import AgGrid
from st_aggrid import GridOptionsBuilder, JsCode, GridUpdateMode

if 'BeforeAfterTrips' not in st.session_state:
    st.session_state.BeforeAfterTrips = [0, 0]

def reset():
    st.session_state['year'] = 'Select'
    st.session_state.BeforeAfterTrips = [0, 0]
    st.session_state.tripDistanceSource = 'Select'

with st.container():
    '''
    # Bicycle and Pedestrian Improvements
    
    This calculator will estimate the reduction in emissions resulting from 
    improvements to bicycle and pedestrian infrastructure and associated mode
    shift from passenger vehicles to bicycling or walking, including but not 
    limited to sidewalks, dedicated bicycle infrastructure, improved wayfinding, 
    mid-block crossing installations, bike share systems, and bike parking 
    improvements.
    
    ## INPUT										
            
    '''
    resetPressed = st.button('Reset Inputs', on_click=reset, disabled = False)
    yearSelect = pd.Series(['Select']).append(pd.Series(range(2018, 2041)))
    col1, col2 = st.columns(2)
    
    with col1:
        '''
            **(1)** What is your project evaluation year?'''
    
    with col2:
        year = st.selectbox('Project Evaluation Year', yearSelect, label_visibility='collapsed', key = 'year')
    
    '**(2)** Estimate the shift in daily motorized passenger vehicle trips to non-motorized travel due to the bicycle and pedestrian project.'
    '**Daily Passenger Vehicle Trips**'
    
    ############
    ## Before After Input Table
    df = pd.DataFrame({'Before':[st.session_state.BeforeAfterTrips[0]], 'After':[st.session_state.BeforeAfterTrips[1]]})
    
    reload_data = False
    if resetPressed:
        reload_data = True
    
    builder = GridOptionsBuilder.from_dataframe(df)
    builder.configure_columns(["Before", "After"], editable=True, enterMovesDown=True)
    builder.configure_column("Change", valueGetter='Number(data.Before)-Number(data.After)', type='rightAligned')
    builder.configure_columns(["Before", "After", "Change"], resizable=False, filterable=False, sortable=False, suppressMenu=True)
    go = builder.build()

    gridData = AgGrid(df, gridOptions=go, theme='balham', height=63, fit_columns_on_grid_load=True, \
                      reload_data=reload_data, key="beforeAfterGrid", update_mode = GridUpdateMode.MODEL_CHANGED, enable_enterprise_modules=False)
    
    new_data = gridData['data']
    if resetPressed:
        new_data = pd.DataFrame({'Before':[st.session_state.BeforeAfterTrips[0]], 'After':[st.session_state.BeforeAfterTrips[1]]})
    else:
        new_data['Change'] = int(new_data['Before']) -  int(new_data['After'])
    
    st.session_state.BeforeAfterTrips = [int(new_data['Before']), int(new_data['After'])]

 
    ##############
    # Average Trip Distance Inputs
    
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            '**(3a)** Select the data type used for entering the typical one-way \
                trip distance of passenger vehicles. Click the button to fill the select \
                inputs with national default values:'
            ''
        with col2:
            '**Trip Distance Source**'
            distSource = st.selectbox('total trip distance', ['Select', 'Average', 'Distribution'], label_visibility='collapsed', key = 'tripDistanceSource')
            natDefualts = st.button('Fill National Default Values')
    with st.container():
        if distSource == 'Select':
            '**(3b)** If you selected “Average” above, enter the typical one-way trip distance. \
                If you selected “Distribution” above, enter the typical distribution of one-way trip distances.'
        elif distSource == 'Average':
            col1, col2 = st.columns(2)
            with col1:
                '**(3b)** Enter the typical average one-way trip distance.'
            with col2:
                '**Typical Trip Distance (miles one way)**'
                aveTripDistance = st.number_input('Trip Distance', label_visibility='collapsed')
        elif distSource == 'Distribution':
            '**(3b)** Enter the typical distribution of one-way trip distances.'
            dist = pd.DataFrame(data = [[0, 0, 0, 0, 0]], columns = ['x < 1', '1 < x < 2', '2 < x < 3', '3 < x < 4', '4 < x < 5'])
            
            builder = GridOptionsBuilder.from_dataframe(dist)
            builder.configure_default_column(resizable=False, filterable=False, sortable=False, suppressMenu=True, editable=True, enterMovesDown=True)
            builder.configure_column("Sum", 
                                     valueGetter='Number(data["x < 1"])+Number(data["1 < x < 2"])+Number(data["2 < x < 3"])+Number(data["3 < x < 4"])+Number(data["4 < x < 5"])', 
                                     type='rightAligned', editable=False)
            go = builder.build()
            
            gridData = AgGrid(dist, theme='balham', height=63, fit_columns_on_grid_load=True, gridOptions=go, enable_enterprise_modules=False)

            