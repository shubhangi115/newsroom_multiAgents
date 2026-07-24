import streamlit as st
import requests
from streamlit_option_menu import option_menu # for the diviison for home about etc navigaiton space

# to import bootstrap icon library
st.markdown("""
<link rel="stylesheet"
href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">
""", unsafe_allow_html=True)

from components.research_front import display_research
from components.fact_check import display_fact_check
from components.seo import display_seo
from components.script import display_script
from components.image_prompt import display_image_prompt
from components.video_prompt import display_video_prompt
from components.headline import display_headline
from components.social_media import display_social_media
from components.validation import display_validation
from components.final import display_final
from downloads import create_pdf

BASE_URL = "https://newsroom-multiagents.onrender.com/"

st.set_page_config(
    page_title="Newsroom AI",
    page_icon="📰",
    layout="wide"
)

st.markdown(
    """
    <style>
        .block-container {
            padding-top: 0.8rem;
        }
    </style>
    """,
    unsafe_allow_html=True
)   


# background

st.markdown(
    """
    <style>

    .stApp {
        background-color: #0e1117;
    }

    div[data-testid="stButton"] button {
        width: 100%;
        height: 48px;
        border-radius: 10px;
        font-size: 16px;
        font-weight: 600;
    }

    div[data-testid="stTextInput"] input {
        border-radius: 10px;
    }

    div[data-testid="stSelectbox"] > div {
        border-radius: 10px;
    }

    div[data-testid="stVerticalBlockBorderWrapper"] {
        border-radius: 14px;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# navigation

selected = option_menu(
    menu_title=None,
    options=["Home", "About", "Features"],
    icons=["house-fill", "info-circle-fill", "rocket-fill"],
    orientation="horizontal",
    default_index=0,
    styles={
        "container": {
            "padding": "0px",
            "margin": "0px",
        },

        "nav-link": {
            "text-align": "center",
            "margin": "0px",
        },

        "nav-link-selected": {
            "background-color": "#f87171",
        },
    }
)

# home

if selected == "Home":

    st.title("Newsroom AI")

    # st.markdown("""
    #     <h1>
    #         <i class="bi bi-journals" style="font-size:45px; margin-right:6px;"></i>
    #         Newsroom AI
    #     </h1>
    #     """, unsafe_allow_html=True)

    st.caption(
        "Multi-agent AI platform for automated news research, "
        "fact-checking, content creation and publication."
    )

    # st.divider()
    st.markdown("""
        <hr style="
            margin-top:5px;
            margin-bottom:5px;
        ">
        """, unsafe_allow_html=True
    )
    
    with st.container(border=True):

        st.header(
            "Transform a news topic into publication-ready content"
        )
        
        # st.markdown(
        #     """
        #    <h2 style="color:#ff4b4b;">
        #         Transform a news topic into publication-ready content
        #     </h2>
        #     """,
        #     unsafe_allow_html=True
        # )

        st.write(
            """
            Newsroom AI uses multiple specialised AI agents to research,
            verify, optimise and prepare news content through one automated
            workflow.
            """
        )

        st.info(
            "Start with a news topic and choose how far the newsroom "
            "pipeline should run."
        )

    st.subheader("Platform Highlights")

    columns = st.columns(4)

    column1 = columns[0]
    column2 = columns[1]
    column3 = columns[2]
    column4 = columns[3]

    with column1:

        with st.container(border=True):

            # st.subheader("10 AI Agents")

            st.markdown("""
                <h4>
                    <i class="bi bi-robot" style="font-size:26px; margin-right:6px; color:#f87171;"></i>
                    10 AI Agents
                </h4>
                """, unsafe_allow_html=True)

            st.write(
                """
                Specialised agents handle research, fact-checking,
                SEO, script writing, visual prompts and publishing.
                """
            )

    with column2:

        with st.container(border=True):

            # st.subheader("Live Web Research")

            st.markdown("""
                <h4>
                    <i class="bi bi-broadcast" style="font-size:26px; margin-right:6px; color:#f87171"></i>
                    Live Web Research
                </h4>
                """, unsafe_allow_html=True)

            st.write(
                """
                Tavily provides current web information and source links
                for research and claim verification.
                """
            )

    with column3:

        with st.container(border=True):

            # st.subheader("Gemini AI")

            st.markdown("""
                <h4>
                    <i class="bi bi-cpu" style="font-size:26px; margin-right:6px; color:#f87171"></i>
                    Gemini AI
                </h4>
                """, unsafe_allow_html=True)

            st.write(
                """
                Gemini processes information and generates structured
                newsroom reports for every pipeline stage.
                """
            )

    with column4:

        with st.container(border=True):

            # st.subheader("Structured Output")
            st.markdown("""
                <h4>
                    <i class="bi bi-braces" style="font-size:26px; margin-right:6px; color:#f87171"></i>
                    Structured Output
                </h4>
                """, unsafe_allow_html=True)

            st.write(
                """
                Schema model that validate the response returned by every
                newsroom agent.
                """
            )

    st.info(
        "Open the Features tab to enter a topic and run the newsroom pipeline."
    )


# about

elif selected == "About":

    st.title("Newsroom AI")

    # st.markdown("""
    #     <h1>
    #         <i class="bi bi-journals" style="font-size:45px; margin-right:6px;"></i>
    #         Newsroom AI
    #     </h1>
    #     """, unsafe_allow_html=True)

    st.caption(
        "Learn how the multi-agent newsroom pipeline works."
    )

    # st.divider() 
    st.markdown("""
        <hr style="
            margin-top:5px;
            margin-bottom:5px;
        ">
        """, unsafe_allow_html=True
    )

    st.header("Overview")
    # st.markdown(    
    #     """
    #     <h2>
    #         Overview
    #     </h2>
    #     """,
    #     unsafe_allow_html=True
    # )

    st.write(
        """
        Newsroom AI is a multi-agent platform that automates the complete
        news production workflow using Large Language Models (LLMs).
        Instead of asking a single AI model to perform every task, the
        platform divides the workflow into multiple specialised agents,
        where each agent is responsible for one stage of the newsroom
        pipeline.

        The platform combines Google Gemini for intelligent content
        generation, Tavily Search for real-time web research and
        verification, FastAPI for the backend API, and Streamlit for
        the user interface. Every agent returns structured outputs
        using Pydantic models, making the pipeline reliable, modular,
        and easy to extend.
        """
    )

    st.subheader("Newsroom Workflow")

    with st.container(border=True):

        workflow_row = st.columns(5)

        workflow_row1 = workflow_row[0]
        workflow_row2 = workflow_row[1]
        workflow_row3 = workflow_row[2]
        workflow_row4 = workflow_row[3]
        workflow_row5 = workflow_row[4]

        with workflow_row1:
            # st.write("### 🔎")
            # st.write("Research")

            # will use <div> now as h4 has its own styling
            st.markdown("""
                <h4>
                    <i class="bi bi-search" style="font-size:26px; margin-right:3px; color:#f87171;"></i> 
                    Research
                </h4>
                """, unsafe_allow_html=True)
            
            st.write(
            "Collects trusted information, facts, statistics, and sources"
        )

        with workflow_row2:
            st.markdown("""
                <h4>
                    <i class="bi bi-patch-check" style="font-size:26px; margin-right:3px; color:#f87171;"></i> 
                    Fact Check
                </h4>
            """, unsafe_allow_html=True)

            st.write(
            "Verifies claims using reliable web sources for the researched information"
        )


        with workflow_row3:
            st.markdown("""
                <h4>
                    <i class="bi bi-graph-up" style="font-size:26px; margin-right:3px; color:#f87171;"></i> 
                    SEO
                </h4>
            """, unsafe_allow_html=True)

            st.write(
            "Generates SEO titles, keywords, and metadata"
        )

        with workflow_row4:
            st.markdown("""
                <h4>
                    <i class="bi bi-pencil-square" style="font-size:26px; margin-right:3px; color:#f87171;"></i> 
                    Script
                </h4>
            """, unsafe_allow_html=True)
            
            st.write(
            "Creates a structured news article from verified research"
        )

        with workflow_row5:
            st.markdown("""
                <h4>
                    <i class="bi bi-image" style="font-size:26px; margin-right:3px; color:#f87171;"></i> 
                    Image Prompt
                </h4>
                """, unsafe_allow_html=True)
            
            st.write(
            "Creates AI image prompts for the news story"
        )

        st.write("")

        workflow_row2 = st.columns(5)

        with workflow_row2[0]:
            st.markdown("""
                <h4>
                    <i class="bi bi-camera-video" style="font-size:26px; margin-right:3px; color:#f87171;"></i> 
                    Video Prompt
                </h4>
                """, unsafe_allow_html=True)
            
            st.write(
            "Generates scene-by-scene prompts for creating AI-powered news videos"
        )

        with workflow_row2[1]:
            st.markdown("""
                <h4>
                    <i class="bi bi-newspaper" style="font-size:26px; margin-right:3px; color:#f87171;"></i> 
                    Headline
                </h4>
                """, unsafe_allow_html=True)
            
            st.write(
            "Creates engaging, and SEO-optimized headlines"
        )

        with workflow_row2[2]:
            st.markdown("""
                <h4>
                    <i class="bi bi-share" style="font-size:26px; margin-right:3px; color:#f87171;"></i> 
                    Social Media
                </h4>
                """, unsafe_allow_html=True)
            
            st.write(
            "Generates captions and hashtags for social platforms"
        )

        with workflow_row2[3]:
            st.markdown("""
                <h4>
                    <i class="bi bi-shield-check" style="font-size:26px; margin-right:3px; color:#f87171;"></i> 
                    Validation
                </h4>
                """, unsafe_allow_html=True)
                
            st.write(
            "Reviews all generated outputs for accuracy, consistency, completeness, and overall quality"
        )

        with workflow_row2[4]:
            st.markdown("""
                <h4>
                    <i class="bi bi-file-earmark-check" style="font-size:26px; margin-right:3px; color:#f87171;"></i>
                    Final Editor
                </h4>
                """, unsafe_allow_html=True)
            
            st.write(
            "Produces the final publication-ready newsroom report"
        )


#features

elif selected == "Features":

    st.title("Newsroom AI")

    # st.markdown("""
    #         <h1>
    #             <i class="bi bi-journals" style="font-size:45px; margin-right:6px;"></i>
    #             Newsroom AI
    #         </h1>
    #         """, unsafe_allow_html=True)

    st.caption(
        "Enter a topic and choose the final agent that should run"
    )

    # st.divider()
    st.markdown("""
        <hr style="
            margin-top:5px;
            margin-bottom:5px;
        ">
        """, unsafe_allow_html=True
    )

    st.header("Generate Newsroom Content")

    with st.container(border=True):

        input_column, agent_column = st.columns([2, 1])

        with input_column:

            topic = st.text_input(
                "Enter topic",
                placeholder="Example: Artificial Intelligence in Healthcare"
            )

        with agent_column:

            agent_options = {
                "Research": "research",
                "Fact Checker": "fact_check",
                "SEO Optimizer": "seo",
                "Script Writer": "script",
                "Image Prompt Generator": "image_prompt",
                "Video Prompt Generator": "video_prompt",
                "Headline Optimizer": "headline",
                "Social Media Agent": "social_media",
                "Quality Validator": "validation",
                "Final Editor": "final"
            }

            selected_agent_name = st.selectbox(
                "Select final agent",
                options=list(agent_options.keys())
            )

            target_agent = agent_options[selected_agent_name]

        generate_button = st.button(
            "Generate Newsroom Output",
            # type="primary"
        )

        st.markdown("""
            <style>
            div.stButton > button {
                background-color: #f87171;
                color: white;
            }

            div.stButton > button:hover {
                background-color: #ef4444;
            }
            </style>
            """, unsafe_allow_html=True)

    if generate_button:

        if topic.strip() == "":

            st.warning(
                "Please enter a news topic."
            )

        else:

            request_data = {
                "topic": topic,
                "target_agent": target_agent
            }

            try:

                with st.spinner(
                    f"Running the newsroom pipeline up to "
                    f"{selected_agent_name}..."
                ):

                    response = requests.post(
                        BASE_URL,
                        json=request_data,
                        timeout=300
                    )

                if response.status_code == 200:

                    result = response.json()
                    

                    st.success(
                        f"Pipeline completed successfully up to "
                        f"{selected_agent_name}."
                    )

                    st.divider()
                    pdf_bytes = create_pdf(result)

                    col1, col2 = st.columns([6, 1])

                    with col1:
                        st.subheader("Generated Output")

                    with col2:
                        st.download_button(
                            label="Download PDF",
                            data=pdf_bytes,
                            file_name="news_report.pdf",
                            mime="application/pdf"
                        )

                    display_research(
                        result.get("research")
                    )

                    display_fact_check(
                        result.get("fact_check")
                    )

                    display_seo(
                        result.get("seo")
                    )

                    display_script(
                        result.get("script")
                    )

                    display_image_prompt(
                        result.get("image_prompt")
                    )

                    display_video_prompt(
                        result.get("video_prompt")
                    )

                    display_headline(
                        result.get("headline")
                    )

                    display_social_media(
                        result.get("social_media")
                    )

                    display_validation(
                        result.get("validation")
                    )

                    display_final(
                        result.get("final")
                    )

                    st.divider()


                else:

                    error_message = response.json().get(
                        "detail",
                        "The request failed."
                    )

                    st.error(
                        f"Request failed: {error_message}"
                    )

            except requests.exceptions.ConnectionError:

                st.error(
                    "Could not connect to the FastAPI backend. "
                    "Make sure the Uvicorn server is running."
                )

            except requests.exceptions.Timeout:

                st.error(
                    "The newsroom pipeline took too long to respond."
                )