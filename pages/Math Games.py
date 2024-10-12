import streamlit as st

st.title("Math Games")

st.header("Addition & Subraction Games")
# HTML for the Scratch iframe
scratch_iframe = '''
<iframe src="https://scratch.mit.edu/projects/1080362940/embed" 
        allowtransparency="true" 
        width="485" 
        height="402" 
        frameborder="0" 
        scrolling="no" 
        allowfullscreen></iframe>
'''

# Display the iframe in the Streamlit app
st.components.v1.html(scratch_iframe, height=402)

st.header("Muliplication Game")
# HTML for the Scratch iframe
scratch_iframe = '''
<iframe src="https://scratch.mit.edu/projects/1080401665/embed" 
        allowtransparency="true" 
        width="485" 
        height="402" 
        frameborder="0" 
        scrolling="no" 
        allowfullscreen></iframe>
'''

# Display the iframe in the Streamlit app
st.components.v1.html(scratch_iframe, height=402)