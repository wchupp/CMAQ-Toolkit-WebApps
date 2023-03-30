import streamlit as st
import pandas as pd
import numpy as np
from st_aggrid_cmaq import AgGrid
from st_aggrid_cmaq import GridOptionsBuilder, JsCode, GridUpdateMode, ColumnsAutoSizeMode
from utils.SetContainerStyle import *

def introduction():
    st.markdown(
        '''
        <style>
        #IntroMain{
        background-color: rgba(254,255,197,255);
        border-style: solid;
        border-width: 3px;
        padding: 10px 10px 10px 10px;
        }
        #IntroMain .element-container, #IntroMain .stMarkdown {
            width: auto !important;
        }
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
    
    with st.container():
        SetContainerID('IntroMain')
        st.markdown(
            '''
            # Bicycle and Pedestrian Improvements
            
            ------
            
            This tool provides estimates of emission reductions for CMAQ-funded projects 
            that reduce emissions by diverting passenger vehicle trips to non-motorized modes.
            													
            The tool uses emission rates based on a national-scale run of the EPA MOVES 
            model. Emission estimates from tools in the CMAQ Toolkit are not intended for 
            use in State Implementation Plans (SIPs) or transportation conformity analyses 
            and do not meet the same requirements necessary for SIP and conformity reporting.
            																						
            Choose the tab below to calculate emissions benefits for a 
            traffic flow improvements project.
            ''')