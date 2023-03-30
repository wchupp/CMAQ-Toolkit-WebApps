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
from pages.BikePedTools import Introduction, BikePed
from utils.PageSetup import *

st.set_page_config(page_title="CMAQ Tools", layout="wide")

setup()

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

c1, c2, c3 = st.columns([1, 6, 1])
with c2:
    
    introHeader()

    ActiveTab = st.container()

with st.container():
    SetContainerID('tabsCont')
    st.markdown('''
        <style>
        section.main {
        margin-bottom: 90px;
        }
        #tabsCont {
            position: fixed;
            bottom: 0;
            color: white;
            border-style: solid;
            border-color: black;
            border-width: 3px;
            background-color: rgb(131, 179, 224);
            overflow: hidden;
        }
        #tabsCont .element-container {
        width: auto !important;
        }
        #tabsCont iframe {
        width: 100% !important;
        }
        </style>''', unsafe_allow_html=True)

    chosen_id = tabs.tab_bar(data=[
    tabs.TabBarItemData(id="IntroTab", title="Introduction", description=""),
    tabs.TabBarItemData(id="BikePedTab", title="Bicycle and Pedestrian Infrastructure", description="")],
    default="IntroTab",)
                       
    if chosen_id is None:
        with ActiveTab:
            Introduction.introduction()
    if chosen_id == "IntroTab":
        with ActiveTab:
            Introduction.introduction()
    elif chosen_id == "BikePedTab":
        with ActiveTab:
            BikePed.bikeped()