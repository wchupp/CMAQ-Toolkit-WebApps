import streamlit as st
from streamlit.components.v1 import html

def SetContainerStyle(css):
    css = css.replace("\n", "")
    script = '''
    <script>
    var iframes = window.parent.document.getElementsByTagName("iframe")
    iframeTag = iframes[iframes.length - 1]
    iframeTag.closest("[data-testid=stVerticalBlock]").setAttribute("style", "{}");
    </script>
    '''.format(css)
    
    html(script, height=0, width=0)