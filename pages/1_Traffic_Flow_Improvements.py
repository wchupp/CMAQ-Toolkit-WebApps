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

st.set_page_config(page_title="CMAQ Tools", layout="wide")
st.image('CMAQToolkitLogo.png')
with st.container():
    '''
    # Congestion and Traffic Flow Improvements
    
    
    '''
    
tab1, tab2, tab3, tab4 = st.tabs(['Signal Synchronization', 'Intersection Improvements', 'Roundabouts', 'Two Way Left Turn Lanes'])