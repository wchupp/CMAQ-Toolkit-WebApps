# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 14:52:47 2022

@author: william.chupp
"""

# importing modules
import streamlit as st
from utils.SetContainerStyle import *
st.set_page_config(page_title="CMAQ Tools", layout="wide")

st.image('CMAQToolkitLogo.png')
with st.container():
    SetContainerStyle('''
                      background-color:rgb(0 0 242);
                      border-style: solid;
                      border-width: 4px;
                      border-radius: 0px;
                      padding: 2% 2% 2% 2%;
                      ''')
    
    col1, col2 = st.columns([2, 1])
    with col1:

        SetContainerStyle('''
                          background-color:rgb(255 251 242);border-style: solid;
                          border-width: 3px;
                          border-radius: 15px;
                          padding: 1% 1% 1% 1%;
                          ''')    
        
        st.markdown(
        '''
        
        # Welcome to the CMAQ Toolkit
        
        ---
        
        ## Introduction to the CMAQ Toolkit
        
        The Federal Highway Administration (FHWA) Office of Natural Environment 
        developed a series of tools to provide technical support and resources for the
        implementation of the Congestion Mitigation and Air Quality Improvement (CMAQ)
        Program.
        
        CMAQ project justification as well as annual reporting require the development 
        of reliable air quality benefit estimates. Realizing that every potential 
        project sponsor may not have the capacity for developing independent air 
        quality benefit estimates, the FHWA has undertaken the initiative of developing 
        a series of spreadsheet based tools to facilitate the calculation of 
        representative air quality benefit data.
        
        This CMAQ Emissions Calculator Toolkit is only 
        offered as an additional resource to assist DOTs, MPOs and project sponsors in 
        the project justification process. Agencies and individuals using a preferred 
        methodology to generate air quality benefit information are welcome to continue 
        their current practice. The tool kit will be released in modules by project 
        type.
        
        **CMAQ Toolkit Video Series**: FHWA is developing short 3–4-minute videos for each 
        tool or set of related tools in the CMAQ Toolkit. See an overview video here 
        and tool-specific videos on the cards below. New videos will be added as they 
        are completed.
        
        **The CMAQ Input Data Dictionary** provides important details related to various inputs
        associated with emissions estimation processes for CMAQ project eligibility 
        categories including inputs associated with the CMAQ Emissions Calculator 
        Tools.
        
        Choose a link from the list of tools to the right or use the navigation
        bar to the left to go to explore the tools, documentation, and training.
        ''')
    with col2:
        st.markdown('''
                    
                    <div 
                        style="background-color:rgb(255 251 242);border-style: solid;
                        border-width: 3px;
                        border-radius: 15px;
                        padding: 2% 2% 2% 2%;">
                    
                    #### Available Tools
                    - Adaptive Traffic Control Systems (ATCS)
                    - Alternative Fuel Vehicles and Infrastructure
                    - <a href="/Bicycle_and_Pedestrian_Infrastructure" target="_self">Bicycle and Pedestrian Improvements</a>
                    - Carpooling and Vanpooling
                    - <a href="/Traffic_Flow_Improvements" target="_self">Congestion Reduction and Traffic Flow Improvements</a>
                    - Diesel Idle Reduction Strategies
                    - Diesel Truck and Engine Retrofit & Replacement
                    - Dust Mitigation
                    - Electronic Open-Road Tolling (EORT)
                    - Electric Vehicles and EV Charging Infrastructure
                    - Locomotive & Marine Engine Retrofit and Replacement
                    - Managed Lanes
                    - Non-Road Construction and Intermodal Equipment
                    - Transit Bus Upgrades & System Improvements
                    - Transit Bus Service and Fleet Expansion
                    - Travel Advisories
                    </div>
                    ''', unsafe_allow_html=True)

        
        
