import streamlit as st
from PIL import Image
import requests
from io import BytesIO
from llmGenerator import llmGenerator

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
    
    # Method 1: Using local images (uncomment if using local files)
    with col1:
        st.image("images/huzzex-1.png", use_container_width=True)
    with col2:
        st.image("images/huzzex-2.png", use_container_width=True)
    with col3:
        st.image("images/huzzex-3.png", use_container_width=True)
    
    # Method 2: Using placeholder images (for development)
    # placeholder_url = "https://via.placeholder.com/200"
    # with col1:
    #     st.image(placeholder_url, use_column_width=True)
    # with col2:
    #     st.image(placeholder_url, use_column_width=True)
    # with col3:
    #     st.image(placeholder_url, use_column_width=True)

    st.text("")

    # Text Input
    user_text = st.text_area("Enter text to uzzIfy:", 
                            placeholder="I am so proud of bro for the Google offer!",
                            height=100)

    

    # Centering button using columns
    col1, col2, col3, col4, col5, col6, col7 = st.columns(7)  # Adjust proportions for centering
    # Button
    with col4:
        generate_button = st.button("UzzIfy!", type="primary")
    
    if generate_button:
        if user_text:
            st.success("Here's your uzzIfied text:")
            st.markdown(f"""
                <div style="
                    color: black;
                    background-color: #f0f2f6;
                    padding: 20px;
                    border-radius: 10px;
                    margin-top: 20px;
                ">
                    {llmGenerator(user_text)}
                </div>
            """, unsafe_allow_html=True)
        else:
            st.warning("Please enter some text to uzz-ify!")


    st.markdown("""
            ---
            <footer> Made with 💛 by the Uzz-inator team </footer>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()