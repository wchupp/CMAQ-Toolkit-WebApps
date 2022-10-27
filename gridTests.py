# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 11:44:15 2022

@author: william.chupp
"""

import streamlit as st
import pandas as pd
import numpy as np
from st_aggrid_cmaq import AgGrid
from st_aggrid_cmaq import GridOptionsBuilder, JsCode, GridUpdateMode

st.session_state

if 'gridData' not in st.session_state:
    df = pd.DataFrame({'a':[0, 1], 'b':[2, 3]})
else:
    df = pd.DataFrame(st.session_state.gridData)
    df
reset = st.button('reset')

reload_data = True
if reset:
    reload_data=True
    df = pd.DataFrame({'a':[100, 100], 'b':[100, 100]})
text = st.text_input('input')
builder = GridOptionsBuilder.from_dataframe(df)

builder.configure_default_column(resizable=False, filterable=False, 
                                 sortable=False, suppressMenu=True, 
                                 editable=True, enterMovesDown=True,
                                 valueFormatter='value + "%"')
go = builder.build()
newGrid = AgGrid(df, gridOptions=go, key="grid", reload_data=reload_data, enable_enterprise_modules=False)

st.session_state.gridData = newGrid.data
st.session_state

