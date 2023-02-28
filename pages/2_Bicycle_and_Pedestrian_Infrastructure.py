# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 14:52:47 2022

@author: william.chupp
"""

# importing modules
import streamlit as st
import pandas as pd
import numpy as np
from st_aggrid_cmaq import AgGrid
from st_aggrid_cmaq import GridOptionsBuilder, JsCode, GridUpdateMode, ColumnsAutoSizeMode

EmissionsData = pd.read_csv('EmissionsData.csv')

if 'BeforeAfterTrips' not in st.session_state:
    st.session_state.BeforeAfterTrips = [0, 0]

def reset():
    st.session_state['year'] = 'Select'
    st.session_state.BeforeAfterTrips = [0, 0]
    st.session_state.tripDistanceSource = 'Select'
    
def natDefaultsClick():
    st.session_state['aveTripDistance'] = 2.013

st.set_page_config(page_title="CMAQ Tools", layout="wide")
st.image('CMAQToolkitLogo.png')
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
    
    gridData = AgGrid(df, gridOptions=go, theme='balham', height=94, fit_columns_on_grid_load=True,\
                      columns_auto_size_mode = ColumnsAutoSizeMode.FIT_CONTENTS,\
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
            natDefaults = st.button('Fill National Default Values', on_click=natDefaultsClick)
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

                aveTripDistance = st.number_input('Trip Distance', label_visibility='collapsed', key="aveTripDistance" )
        elif distSource == 'Distribution':
            '**(3b)** Enter the typical distribution of one-way trip distances.'
            if natDefaults:
                distData = [[20.651, 37.262, 20.426, 13.468, 8.193]]
                dist = pd.DataFrame(data = distData, columns = ['x < 1', '1 < x < 2', '2 < x < 3', '3 < x < 4', '4 < x < 5'])
                #st.session_state.distDistribution.data = dist.to_dict()
            if 'distDistribution' not in st.session_state:
                distData = [[0, 0, 0, 0, 0]]
                dist = pd.DataFrame(data = distData, columns = ['x < 1', '1 < x < 2', '2 < x < 3', '3 < x < 4', '4 < x < 5'])
            else:
                dist = pd.DataFrame(st.session_state.distDistribution.data)
                
            builder = GridOptionsBuilder.from_dataframe(dist)
            builder.configure_default_column(resizable=False, filterable=False, 
                                             sortable=False, suppressMenu=True, 
                                             editable=True, enterMovesDown=True,
                                             valueFormatter='value + "%"')
            builder.configure_column("Sum", 
                                     valueGetter='Number(data["x < 1"])+Number(data["1 < x < 2"])+Number(data["2 < x < 3"])+Number(data["3 < x < 4"])+Number(data["4 < x < 5"])', 
                                     type='rightAligned', editable=False)
            go = builder.build()
            
            distGridData = AgGrid(dist, theme='balham', height=63, fit_columns_on_grid_load=True, key = 'distDistribution', gridOptions=go, enable_enterprise_modules=False, reload_data=True)
            newDist = distGridData['data']
            aveTripDistance = 0
            for med, dist in zip([0.5,1.5,2.5,3.5,4.5], newDist.iloc[0]):
                aveTripDistance = aveTripDistance + float(med)*(float(dist)/100)
            st.session_state
            
            
            
            
    '## Output'
    calculate = st.button('Calculate')
    output_df = pd.DataFrame(data={'Pollutant': ['Carbon Monoxide (CO)',
                                    'Particulate Matter <2.5 μm (PM2.5)',
                                    'Particulate Matter <10 μm (PM10)',
                                    'Nitrogen Oxide (NOx)',
                                    'Volatile Organic Compounds (VOC)',
                                    'Carbon Dioxide (CO2)',
                                    'Carbon Dioxide Equivalent (CO2e)',
                                    'Total Energy Consumption (MMBTU/day)'],
                                    'Total': [0,0,0,0,0,0,0,0]})
    if calculate:
        runningRates = EmissionsData.loc[(EmissionsData['yearID']==year)&(EmissionsData['processID']==1)][['pollutantID', 'emissionRate']]
        runningRates.set_index('pollutantID', inplace=True)
        stoppedRates = EmissionsData.loc[(EmissionsData['yearID']==year)&(EmissionsData['processID']==2)][['pollutantID', 'emissionRate']]
        stoppedRates.set_index('pollutantID', inplace=True)
        Emissions = (stoppedRates+runningRates*aveTripDistance)*(st.session_state.BeforeAfterTrips[0]-st.session_state.BeforeAfterTrips[1])
        outputList = [Emissions['emissionRate'][2], 
                      Emissions['emissionRate'][110],
                      Emissions['emissionRate'][100],
                      Emissions['emissionRate'][3],
                      Emissions['emissionRate'][87],
                      Emissions['emissionRate'][90],
                      Emissions['emissionRate'][98],
                      Emissions['emissionRate'][91]]
        output_df = pd.DataFrame(data={'Pollutant': ['Carbon Monoxide (CO)',
                                        'Particulate Matter <2.5 μm (PM2.5)',
                                        'Particulate Matter <10 μm (PM10)',
                                        'Nitrogen Oxide (NOx)',
                                        'Volatile Organic Compounds (VOC)',
                                        'Carbon Dioxide (CO2)',
                                        'Carbon Dioxide Equivalent (CO2e)',
                                        'Total Energy Consumption (MMBTU/day)'],
                                        'Total': outputList})
        
        
    builder = GridOptionsBuilder.from_dataframe(output_df)
    builder.configure_default_column(resizable=False, filterable=False, 
                                     sortable=False, suppressMenu=True, 
                                     editable=False, enterMovesDown=True)
    go = builder.build()
    outputGrid = AgGrid(output_df, fit_columns_on_grid_load=True, gridOptions=go, reload_data=True, enable_enterprise_modules=False, key="output_grid")
            