import streamlit as st
from PIL import Image
import requests
from io import BytesIO
from llmGenerator import llmGenerator
from uzzinator_nltk import Uzzinator

def main():
    # Page Config
    st.set_page_config(
        page_title="UzzInator",
        page_icon="🐝",
        layout="centered"
    )

    # Custom CSS
    st.markdown("""
        <style>
        .main-header {
            font-size: 3.5rem;
            font-weight: 700;
            text-align: center;
            color: #FF6B6B;
            margin-bottom: 0;
        }
        .sub-header {
            font-size: 1.2rem;
            text-align: center;
            color: #4A4A4A;
            font-style: italic;
            margin-bottom: 2rem;
        }
        .response-container {
            color: black;
            background-color: #f0f2f6;
            padding: 20px;
            border-radius: 10px;
            height: 100%;
        }
        .response-label {
            font-weight: bold;
            font-size: 1.2rem;
            color: #4A4A4A;
        }
        footer {
            text-align: center;
        }
        </style>
    """, unsafe_allow_html=True)

    # Headers
    st.markdown('<h1 class="main-header">UzzInator 🐝</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Transform your boring text into the freshest -uzz slang!</p>', unsafe_allow_html=True)

    # Image Row using columns
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.image("images/huzzex-1.png", use_container_width=True)
    with col2:
        st.image("images/huzzex-2.png", use_container_width=True)
    with col3:
        st.image("images/huzzex-3.png", use_container_width=True)

    st.text("")

    # Text Input
    user_text = st.text_area("Enter text to uzzIfy:", 
                            placeholder="I am so proud of bro for the Amazon offer!",
                            height=100)

    # Centering button using columns
    col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
    with col4:
        generate_button = st.button("UzzIfy!", type="primary")
    
    if generate_button:
        if user_text:
            # llmResponse = llmGenerator(user_text)
            nltk_uzzinartor = Uzzinator()
            nltkResponse = nltk_uzzinartor.transform(user_text)

            st.success("Here's your uzzIfied text:")
            
            # Create two columns for responses
            # left_col, right_col = st.columns(2)
            
            # LLama response in left column
            # with left_col:
            #     st.markdown('<p class="response-label">LLama</p>', unsafe_allow_html=True)
            #     st.markdown(f"""
            #         <div class="response-container">
            #             {llmResponse}
            #         </div>
            #     """, unsafe_allow_html=True)
            
            # Heuristics response in right column
            # with right_col:
            # st.markdown('<p class="response-label">Heuristics</p>', unsafe_allow_html=True)
            st.markdown(f"""
                <div class="response-container">
                    {nltkResponse}
                </div>
            """, unsafe_allow_html=True)

        else:
            st.warning("Please enter some text to uzz-ify!")

    st.markdown("""
            ---
            <footer> Made with 💛 by <a href="https://x.com/muskanmahajan_">Muskan Mahajan</a> </footer>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()