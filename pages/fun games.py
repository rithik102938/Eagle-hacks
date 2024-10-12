import streamlit as st

st.title("Lets play Soccer")
# HTML for the Scratch iframe
scratch_iframe = '''
<iframe src="https://scratch.mit.edu/projects/621172683/embed" 
        allowtransparency="true" 
        width="485" 
        height="402" 
        frameborder="0" 
        scrolling="no" 621172683
        allowfullscreen></iframe>
'''

# Display the iframe in the Streamlit app
st.components.v1.html(scratch_iframe, height=402)