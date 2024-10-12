import streamlit as st


st.title("Vocab Game")


st.header("Vocab Game")
# HTML for the Scratch iframe
scratch_iframe = '''
<iframe src="https://scratch.mit.edu/projects/1079926517/embed" 
        allowtransparency="true" 
        width="485" 
        height="402" 
        frameborder="0"
        scrolling="no" 
        allowfullscreen></iframe>
'''

# Display the iframe in the Streamlit app
st.components.v1.html(scratch_iframe, height=402)