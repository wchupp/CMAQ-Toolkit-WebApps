import streamlit as st
from streamlit.components.v1 import html

def SetContainerStyle(css):
    css = css.replace("\n", "")
    script = '''
    <script>
        setTimeout(()=> {{

            var iframes = window.parent.document.getElementsByTagName("iframe");
            for(var i=0;i<iframes.length;++i) {{
                if(iframes[i].contentWindow==window) {{
                        iframeTag = iframes[i];
                }}
            }}
            vertBlock = iframeTag.closest("[data-testid=stVerticalBlock]")
            iframeTag.closest("div.element-container").style.display = "none";
            console.log("changing vertBlock style")
            vertBlock.setAttribute("style", "{}");
            elcontainers = vertBlock.querySelectorAll(":scope > div.element-container");
            for(var i=0; i<elcontainers.length; ++i) {{
                console.log("changing elcont style")
                elcontainers[i].style.width = "auto";
                elcontchildren = elcontainers[i].querySelectorAll("div");
                for(var j=0; j<elcontchildren.length; ++j) {{
                        console.log("changing child style")
                        //elcontchildren[j].style = "";
                        elcontchildren[j].setAttribute("style", "width: 100%;");
                        console.log(elcontchildren[j]);
                }}
            }}
        }},500);
    </script>
    '''.format(css)
    
    html(script, height=0, width=0)
    
def SetContainerID(ident):
    script = '''
    <script>
        var iframes = window.parent.document.getElementsByTagName("iframe");
        for(var i=0;i<iframes.length;++i) {{
            if(iframes[i].contentWindow==window) {{
                    iframeTag = iframes[i];
            }}
        }}
        vertBlock = iframeTag.closest("[data-testid=stVerticalBlock]")
        iframeTag.closest("div.element-container").style.display = "none";
        vertBlock.setAttribute("id", "{}");
        children = vertBlock.querySelectorAll(".element-container,.stMarkdown,.row-widget");
        for(var j=0; j<children.length; ++j) {{
                children[j].removeAttribute("style")
        }}
        iframeTag.closest("div.element-container").style.display = "none";
    </script>
    '''.format(ident, ident)
    html(script, height=0, width=0)