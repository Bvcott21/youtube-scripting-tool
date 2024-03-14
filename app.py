import streamlit as st
from utils import generate_script
from dotenv import load_dotenv

load_dotenv()

### Applying styling ###
st.markdown(
    """
    <style>
        siv.stButton > button:first-child {
            background-color: #0099ff;
            color: #ffffff;
        }
        
        div.stButton > button:hover {
            background-color: #00ff00;
            color: #FFFFFF
        }
    </style>
    """,
    unsafe_allow_html = True
)

### Creating session state variable ###
if 'API_Key' not in st.session_state:
    st.session_state['API_Key'] = ''
    
st.title("❤ YouTube Script Writing Tool")

# ### Sidebar to capture the OpenAI API Key ###
# st.sidebar.title("🗝")
# st.session_state['API_Key'] = st.sidebar.text_input(
#     "What's your API Key?",
#     type='password')

# st.sidebar.image("./youtube.jpg", width=300, use_column_width=True)

### Capture user inputs ###
prompt = st.text_input(
    'Please provide the topic of the video.', 
    key='prompt')   # The box for the text prompt 
video_length = st.text_input(
    'Expected video length (in minutes)',
    key = 'video_length') # The box for length
creativity = st.slider(
    'Creativity level - (0 LOW || 1 HIGH)', 
    0.0,
    1.0,
    0.2,
    step = 0.1
)

submit = st.button("Generate script for me")

if submit:
    
    search_result, title, script = generate_script(prompt, 
                                                video_length, 
                                                creativity)
    # Generate the script
    st.success("Here's your script")
    
    # Display Title
    st.subheader('Title: ')
    st.write(title)
    
    # Display script
    st.subheader('Your video script: ')
    st.write(script)
        
        
    # Display Search Engine Result
    st.subheader('Check Out - DuckDuckGo Search:')
    with st.expander('Show me'):
        st.info(search_result)    
else:
    st.error('Oops! Something went wrong!')
        