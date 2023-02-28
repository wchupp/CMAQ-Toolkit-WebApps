import streamlit as st
import pandas as pd
import numpy as np
from st_aggrid_cmaq import AgGrid
from st_aggrid_cmaq import GridOptionsBuilder, JsCode, GridUpdateMode, ColumnsAutoSizeMode

def introduction():
    st.markdown(
        '''
        <style>
        p {
            font-size: x-large;
            word-break: break-word;
        }
        li {
            word-break: break-word;
            }
        </style>
        ''',unsafe_allow_html=True
    )
    st.markdown(
'''
# Congestion and Traffic Flow Improvements

------

This tool provides estimates of emission reductions for CMAQ-funded 
projects that improve traffic flow by implementing intersection 
improvements (i.e. new traffic signals; dedicated phases/lanes for 
turning), signal synchronization, roundabouts, and two way left turn lanes.									

The methodology underlying the development of the tool is based upon 
the Highway Capacity Manual and NCHRP studies. Emissions rates are 
primarily based on a national-scale run of the EPA MOVES model. 
Emission estimates from tools in the CMAQ Toolkit are not intended for 
use in State Implementation Plans (SIPs) or transportation conformity 
analyses and do not meet the same requirements necessary for SIP and 
conformity reporting. 									
									
Choose one of the tabs above to calculate emissions benefits for a 
traffic flow improvements project.
''')