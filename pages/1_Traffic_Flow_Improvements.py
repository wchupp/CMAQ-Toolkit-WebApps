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
import TabBar_cmaq as tabs 
from pages.TFITools import Introduction, SigSync, IntImp, Roundabouts, TWLTL
from utils.SetContainerStyle import *
from utils.PageSetup import *

#Always include these lines at the start of a new tool page
st.set_page_config(page_title="CMAQ Tools", layout="wide")
setup()



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

c1, c2, c3 = st.columns([1, 30, 1])
with c2:
    introHeader()
    ActiveTab = st.container()

    
with st.container():
    SetContainerID('tabsCont')
    st.markdown('''
        <style>
        #tabsCont {
            position: fixed;
            bottom: 0;
            color: white;
            border-style: solid;
            border-color: black;
            border-width: 3px;
            background-color: rgb(131, 179, 224)
        }
        #tabsCont .element-container {
        width: auto !important;
        }
        #tabsCont iframe {
        width: 100% !important;
        }
        </style>''', unsafe_allow_html=True)
    
    chosen_id = tabs.tab_bar(data=[
    tabs.TabBarItemData(id="TFITab", title="Introduction", description=""),
    tabs.TabBarItemData(id="SigSyncTab", title="Signal Synchronization", description=""),
    tabs.TabBarItemData(id="IntImpTab", title="Intersection Improvements", description=""),
    tabs.TabBarItemData(id="RoundTab", title="Roundabouts", description=""),
    tabs.TabBarItemData(id="TWLTLTab", title="Two Way Left Turn Lanes", description="")],
    default="TFITab",)


                   
if chosen_id is None:
    with ActiveTab:
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