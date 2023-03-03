import streamlit as st
import pandas as pd
import numpy as np
from st_aggrid_cmaq import AgGrid
from st_aggrid_cmaq import GridOptionsBuilder, JsCode, GridUpdateMode, ColumnsAutoSizeMode

def sigsync():
   
    st.markdown(
'''
# Traffic Signal Synchronization						

This calculator will estimate the emission reductions resulting from synchronizing 
the traffic signals along a previously unsynchronized corridor.

------					
    ''')

    st.markdown(
        '''
        <style>
        p {
            font-size: large;
            word-break: break-word;
        }
        li {
            word-break: break-word;
            }
        </style>
        ''',unsafe_allow_html=True
        )
    

    # Put all new code here
    if 'InputData' not in st.session_state:
        st.session_state.InputData = [1,2,1,0,90,6,0,0,0,4]
    
    def reset():
        st.session_state['year'] = 'Select'
        st.session_state['area'] = 'Select'
        st.session_state.InputData = [1,2,1,0,90,6,0,0,0,4]


    st.markdown(
        '''
        ## INPUTS								
        ''')


    with st.container():

        resetPressed = st.button('Reset Inputs', on_click=reset, disabled = False)
        yearSelect = pd.Series(['Select']).append(pd.Series(range(2018, 2041)))
        areaSelect = pd.Series(['Select','Urban','Rural'])
        col1, col2 = st.columns(2)
    
        ## Variables with dropdowns
        with col1:
            st.markdown(
                '''
                Project Evaluation Year
                 
                Area Type
                
                ''')
        with col2:
            year = st.selectbox('Project Evaluation Year', yearSelect, label_visibility='collapsed', key = 'year')
            area = st.selectbox('Area Type', areaSelect, label_visibility='collapsed', key = 'area')
        
        inputdata = {'Description':['Corridor Length (miles)',
                                 'Number of Signalized Intersections',
                                 'Number of Lanes (one direction)',
                                 'Posted Speed Limit (mph) (1-75 mph)',
                                 'Average Cycle Length in seconds',
                                 'Truck Percentage (%)',
                                 'Annual Average Daily Traffic (AADT) (both directions) in veh/day',
                                 'Peak-hour Volume (both directions) in veh/hr',
                                 'Existing Corridor Travel Time in minutes',
                                 'Total peak hours per day (AM+PM)'],
                'Input':[1,2,1,0,90,6,0,0,0,4]}
       
        input_df = pd.DataFrame(data=inputdata)
        
        reload_data = False
        if resetPressed:
            reload_data = True
        
        builder = GridOptionsBuilder.from_dataframe(input_df)
        builder.configure_columns(["Description", "Input"], editable=True, enterMovesDown=True)
        go = builder.build()
        gridData = AgGrid(input_df, fit_columns_on_grid_load=True, gridOptions=go, reload_data=True, 
                          update_mode = GridUpdateMode.MODEL_CHANGED, enable_enterprise_modules=False)
    
     #   new_data = gridData['data']
    #    if resetPressed:
   #         new_data = pd.DataFrame({'Before':[st.session_state.BeforeAfterTrips[0]], 'After':[st.session_state.BeforeAfterTrips[1]]})
  #      else:
 #           new_data['Change'] = int(new_data['Before']) -  int(new_data['After'])
    
#        st.session_state.BeforeAfterTrips = [int(new_data['Before']), int(new_data['After'])]

    
        st.markdown(
            '''
            ## Output								
            ''')
            
        calculate = st.button('Calculate')
        
        st.markdown(
            '''
            ### PERFORMANCE								
            ''')
            
        net_df = pd.DataFrame(data={'Metric': ['Volume (both directions) (veh/hr)',
                                      'Existing Average Speed (mph)',
                                      'Travel Time Savings (min)',
                                      'Proposed Average Speed (mph)',],
                                      'PEAK-HOUR': [0,0,0,0],
                                      'OFF-PEAK':[0,0,0,0]})
            
        builder = GridOptionsBuilder.from_dataframe(net_df)
        builder.configure_default_column(resizable=False, filterable=False, 
                                         sortable=False, suppressMenu=True, 
                                         editable=False, enterMovesDown=True)
        go = builder.build()
        netGrid = AgGrid(net_df, fit_columns_on_grid_load=True, gridOptions=go, reload_data=True, enable_enterprise_modules=False, key="net_grid")
                    
            
            
        st.markdown(
            '''
            ### EMISSION REDUCTIONS								
            ''')
        
        emissions_df = pd.DataFrame(data={'Pollutant': ['Carbon Monoxide (CO) (kg/day)',
                                      'Particulate Matter <2.5 μm (PM2.5) (kg/day)',
                                      'Particulate Matter <10 μm (PM10) (kg/day)',
                                      'Nitrogen Oxide (NOx) (kg/day)',
                                      'Volatile Organic Compounds (VOC) (kg/day)',
                                      'Carbon Dioxide (CO2) (kg/day)',
                                      'Carbon Dioxide Equivalent (CO2e) (kg/day)',
                                      'Total Energy Consumption (MMBTU/day)'],
                                          'PEAK-HOUR': [0,0,0,0,0,0,0,0],
                                          'OFF-PEAK': [0,0,0,0,0,0,0,0],
                                          'TOTAL': [0,0,0,0,0,0,0,0]})
        
        builder = GridOptionsBuilder.from_dataframe(emissions_df)
        #builder.configure_columns(["Pollutant", "PEAK-HOUR","OFF-PEAK","TOTAL"], editable=False, enterMovesDown=True)
        builder.configure_default_column(resizable=False, filterable=False, 
                                         sortable=False, suppressMenu=True, 
                                         editable=False, enterMovesDown=True)
        go = builder.build()
        outputGrid = AgGrid(emissions_df, fit_columns_on_grid_load=True, gridOptions=go, reload_data=True, enable_enterprise_modules=False, key="output_grid")
                