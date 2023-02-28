import streamlit as st
import pandas as pd
import numpy as np
from st_aggrid_cmaq import AgGrid
from st_aggrid_cmaq import GridOptionsBuilder, JsCode, GridUpdateMode, ColumnsAutoSizeMode

def sigsync():
    st.markdown(
'''
# Traffic Signal Synchronization						

This calculator will estimate the emission reductions resulting from synchronizing the traffic signals along a previously unsynchronized corridor.

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