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
import extra_streamlit_components as stx
from pages.TFITools import Introduction, SigSync, IntImp, Roundabouts, TWLTL

st.set_page_config(page_title="CMAQ Tools", layout="wide")
st.image('CMAQToolkitLogo.png')

st.markdown(
    '''
    <style>
    .css-1hiobrh p {
        font-size: large;
        word-break: break-word;
    }
    li {
        word-break: break-word;
        }
    </style>
    ''',unsafe_allow_html=True
)

with st.container():
    chosen_id = stx.tab_bar(data=[
    stx.TabBarItemData(id="TFITab", title="Introduction", description=""),
    stx.TabBarItemData(id="SigSyncTab", title="Signal Synchronization", description=""),
    stx.TabBarItemData(id="IntImpTab", title="Intersection Improvements", description=""),
    stx.TabBarItemData(id="RoundTab", title="Roundabouts", description=""),
    stx.TabBarItemData(id="TWLTLTab", title="Two Way Left Turn Lanes", description="")],
    default="TFITab")
    
    print(chosen_id)
    ActiveTab = st.container()
                       
    #TFITab, SigSyncTab, IntImpTab, RoundTab, TWLTLTab = st.tabs(['Introduction', 'Signal Synchronization', 'Intersection Improvements', 'Roundabouts', 'Two Way Left Turn Lanes'])
    if chosen_id is None:
        Introduction.introduction()
    if chosen_id == "TFITab":
        with ActiveTab:
            Introduction.introduction()
    elif chosen_id == "SigSyncTab":
        with ActiveTab:
            SigSync.sigsync()
    elif chosen_id == "IntImpTab":
        with ActiveTab:
            IntImp.intimp()
    elif chosen_id == "RoundTab":
        with ActiveTab:
            Roundabouts.roundabouts()
    elif chosen_id == "TWLTLTab":
        with ActiveTab:
            TWLTL.twltl()