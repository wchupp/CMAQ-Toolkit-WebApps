import streamlit as st
from utils.SetContainerStyle import *
import utils.PageSetup

def setup():
    st.markdown('''
        <style>
        #MainMenu, header, footer {
            visibility: hidden;
        }
        .block-container {
            padding: 0 0 0 0;
        }
        </style>
        ''', unsafe_allow_html=True)
    st.markdown('''
        <style>
        div[data-testid="stSidebarNav"] {
            order: 3;
            }
        </style>
                ''', unsafe_allow_html=True)
    with st.sidebar:
        with st.container():
            SetContainerID('sidebarInfo')
            st.markdown('''
                        <style>
                        #sidebarInfo {
                            display: grid;
                            border-color: rgba(1,83,98,255);
                            border-style: solid;
                            background-color: rgba(1,83,98,255);
                            color: white !important;
                        }
                        #sidebarInfo .stMarkdown, #sidebarInfo .element-container {
                            width: auto !important;
                        }
                        #sidebarInfo h1 {
                            color: white !important;
                            width: auto;
                            text-align: center;
                        }
                        #sidebarInfo p {
                            background-color: white;
                            color: rgb(38, 39, 48);
                            padding: 10px;
                            text-align: center;
                            
                        }
                        </style>
                        ''', unsafe_allow_html=True)
            st.markdown('''
                        # Useful Information
                        
                        CMAQ Help Email: <CMAQ_toolkit_help@dot.gov>
                                ''')

from PIL import Image

dotHead = Image.open('./DOT_heading.png')
ToolkitLogo = Image.open('./CMAQToolkitLogo.png')

def introHeader():
    with st.container():
        SetContainerID('introHeader')
        st.markdown('''
                        <style>
                        #sidebarInfo {
                            display: grid;
                            border-color: rgba(1,83,98,255);
                            border-style: solid;
                            background-color: rgba(1,83,98,255);
                            color: white !important;
                        }
                        #introHeader_child {
                            width: auto !important;
                        }
                        </style>
                        ''', unsafe_allow_html=True)
        i1, i2, i3 = st.columns([1, 1, 1])
        i1.image(dotHead, width=400)
        i2.image(ToolkitLogo, width=400)
        i3.markdown('''
                Questions or Feedback?	
                <CMAQ_toolkit_help@dot.gov>
                ''')
