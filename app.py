from __future__ import annotations

from pathlib import Path
from typing import Dict, List, Optional

import streamlit as st


# =========================
# CONFIG
# =========================
st.set_page_config(page_title="Portfolio", layout="wide")

PAGE_TITLE = "Data Scientist – Business & Economic Analytics"
PRESENTATION_TEXT = """I am a Data Scientist specializing in business analytics, with a strong focus on transforming data into actionable business insights.

During my experience at EDF, I worked autonomously on critical data quality challenges related to HR data, directly impacting the reliability of key business indicators. I developed outlier detection and indicator classification models, which helped improve data consistency and made it easier for teams to use data for operational decision-making.

I also designed a proof of concept for a database aimed at structuring and historizing key indicators, with the goal of improving data reliability over time and reducing inconsistencies caused by manual processes. This work contributed to establishing a more robust and scalable data management approach.

As part of the project, I supported the handover to industrialization teams by clearly presenting both technical and functional choices, ensuring a smooth transition and minimizing risks during the move to production.

In parallel, I develop personal projects based on real-world use cases, particularly in forecasting, where I have improved model accuracy by significantly reducing prediction error, supporting better demand planning decisions.

I am also continuously improving my skills through certifications in machine learning and MLOps, strengthening my ability to build reliable, high-performance solutions that can be effectively used in business environments.

Today, I am looking to contribute to projects where data drives tangible business impact, combining analytical rigor, business understanding, and the ability to deliver operational solutions.
"""

CV_FR_PATH = Path("assets/cv/CV_MAYEUR_Nicolas.pdf")
CV_EN_PATH = Path("assets/cv/cv_en.pdf")

PROJECT_IMAGES: Dict[str, List[Path]] = {
    "project_1": [
        Path("assets/cv/slide/project_1_Slide_1.png"),
        Path("assets/cv/slide/project_1_Slide_2.png"),
    ],
    "project_2": [],
    "project_3": [
        Path("assets/cv/slide/project_3_Slide_1.png"),
        Path("assets/cv/slide/project_3_Slide_2.png"),
        Path("assets/cv/slide/project_3_Slide_3.png"),
    ],
}

PROJECT_LINKS: Dict[str, str] = {
    "project_1": "https://your-project-1.streamlit.app",
    "project_2": "https://featurestore-egfooc83xdtxubsfvyivyp.streamlit.app/",
    "project_3": "https://your-project-3.streamlit.app",
}

PROJECT_TITLES: Dict[str, str] = {
    "project_1": "Project 1",
    "project_2": "Project 2",
    "project_3": "Project 3",
}


# =========================
# HELPERS
# =========================
def inject_css(css: str) -> None:
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)


@st.cache_data(show_spinner=False)
def read_bytes(path: Path) -> bytes:
    return path.read_bytes()


def truncate_text(text: str, max_chars: int = 360) -> str:
    text = text.strip()
    if len(text) <= max_chars:
        return text

    cut = text[:max_chars]
    if " " in cut:
        cut = cut.rsplit(" ", 1)[0]
    return cut + "…"


def toggle_presentation() -> None:
    st.session_state.presentation_expanded = not st.session_state.presentation_expanded


def render_section_label(label: str) -> None:
    st.markdown(
        f'<div class="section-label">{label}</div>',
        unsafe_allow_html=True,
    )


def render_project_carousel(
    container_key: str,
    project_title: str,
    images: List[Path],
    key_prefix: str,
    project_url: Optional[str] = None,
) -> None:
    with st.container(key=container_key):
        st.markdown(
            f'<div class="project-title">{project_title}</div>',
            unsafe_allow_html=True,
        )

        if project_url:
            btn_left, btn_center, btn_right = st.columns([2, 3, 2])
            with btn_center:
                st.link_button(
                    "Open project",
                    project_url,
                    use_container_width=True,
                )

        valid_images = [img for img in images if img.exists()]

        if not valid_images:
            st.markdown(
                '<div class="empty-box">Aucune image disponible</div>',
                unsafe_allow_html=True,
            )
            return

        if len(valid_images) == 1:
            st.image(str(valid_images[0]), use_container_width=True)
            return

        state_key = f"{key_prefix}_index"
        if state_key not in st.session_state:
            st.session_state[state_key] = 0

        current_idx = st.session_state[state_key]

        nav_col_left, nav_col_center, nav_col_right = st.columns([1, 8, 1])

        with nav_col_left:
            if st.button("⬅️", key=f"{key_prefix}_prev"):
                st.session_state[state_key] = (
                    st.session_state[state_key] - 1
                ) % len(valid_images)
                current_idx = st.session_state[state_key]

        with nav_col_right:
            if st.button("➡️", key=f"{key_prefix}_next"):
                st.session_state[state_key] = (
                    st.session_state[state_key] + 1
                ) % len(valid_images)
                current_idx = st.session_state[state_key]

        with nav_col_center:
            st.image(str(valid_images[current_idx]), use_container_width=True)
            st.markdown(
                f"""
                <div class="carousel-counter">
                    Image {current_idx + 1} / {len(valid_images)}
                </div>
                """,
                unsafe_allow_html=True,
            )


# =========================
# SESSION STATE
# =========================
if "presentation_expanded" not in st.session_state:
    st.session_state.presentation_expanded = False


# =========================
# CSS
# =========================
CSS = """
/* =========================
   GLOBAL BACKGROUND
========================= */
.stApp {
    background:
        radial-gradient(circle at 10% 20%, rgba(0,255,255,0.08), transparent 25%),
        radial-gradient(circle at 90% 10%, rgba(255,0,255,0.08), transparent 25%),
        radial-gradient(circle at 50% 100%, rgba(0,150,255,0.08), transparent 35%),
        linear-gradient(180deg, #03060f 0%, #050816 100%);
    color: #EAFBFF;
}

div.block-container {
    max-width: 1200px;
    padding-top: 1.5rem;
    padding-bottom: 3rem;
}

header[data-testid="stHeader"] {
    background: transparent;
}

html, body, [class*="css"] {
    font-family: "Inter", "Segoe UI", sans-serif;
}

/* =========================
   SECTION LABELS CENTERED
========================= */
.section-label {
    text-align: center;
    font-size: 1.35rem;
    font-weight: 800;
    color: #00F5FF;
    letter-spacing: 0.8px;
    margin: 0.4rem 0 0.9rem 0;
    text-shadow:
        0 0 6px #00F5FF,
        0 0 14px rgba(0,245,255,0.6);
}

/* =========================
   TITLE BOX
========================= */
.st-key-title_box {
    background: linear-gradient(90deg, #0b1025, #111a3a, #0b1025);
    border: 1px solid rgba(0,255,255,0.6);
    border-radius: 20px;
    padding: 28px;
    margin-bottom: 2rem;
    box-shadow:
        0 0 15px rgba(0,255,255,0.35),
        0 0 40px rgba(123,44,255,0.25),
        inset 0 0 20px rgba(255,255,255,0.03);
    transition: all 0.3s ease;
}

.st-key-title_box:hover {
    box-shadow:
        0 0 25px rgba(0,255,255,0.6),
        0 0 60px rgba(255,0,255,0.3);
}

.st-key-title_box h1 {
    margin: 0;
    text-align: center;
    font-size: 2.2rem;
    font-weight: 900;
    letter-spacing: 3px;
    color: #00F5FF;
    text-transform: uppercase;
    text-shadow:
        0 0 10px #00F5FF,
        0 0 25px rgba(0,245,255,0.7),
        0 0 45px rgba(255,0,255,0.4);
}

/* =========================
   MAIN CARDS
========================= */
.st-key-presentation_box,
.st-key-cv_box,
.st-key-project_1_box,
.st-key-project_2_box,
.st-key-project_3_box {
    background: linear-gradient(180deg, rgba(8, 12, 25, 0.95), rgba(5, 8, 18, 1));
    border-radius: 18px;
    padding: 22px;
    margin-bottom: 1.6rem;
    border: 1px solid rgba(0,255,255,0.35);
    box-shadow:
        0 0 12px rgba(0,255,255,0.18),
        0 0 28px rgba(123,44,255,0.12),
        inset 0 0 12px rgba(255,255,255,0.02);
    transition: all 0.25s ease;
}

.st-key-presentation_box:hover,
.st-key-cv_box:hover,
.st-key-project_1_box:hover,
.st-key-project_2_box:hover,
.st-key-project_3_box:hover {
    transform: translateY(-3px);
    border: 1px solid rgba(255,0,255,0.7);
    box-shadow:
        0 0 20px rgba(0,255,255,0.4),
        0 0 50px rgba(255,0,255,0.25),
        inset 0 0 14px rgba(255,255,255,0.04);
}

/* =========================
   TEXT
========================= */
.presentation-text {
    font-size: 1.02rem;
    line-height: 1.75;
    color: #DFFBFF;
    margin-bottom: 1rem;
}

.project-title {
    text-align: center;
    font-size: 1.15rem;
    font-weight: 700;
    color: #00F5FF;
    margin-bottom: 0.9rem;
    text-shadow: 0 0 6px rgba(0,245,255,0.6);
}

.carousel-counter {
    text-align: center;
    color: #8bdcff;
    margin-top: 0.55rem;
    font-size: 0.95rem;
}

/* =========================
   EMPTY BOX
========================= */
.empty-box {
    border: 1px dashed rgba(0,255,255,0.4);
    border-radius: 14px;
    padding: 1rem;
    text-align: center;
    color: #8bdcff;
    background: rgba(0,255,255,0.02);
}

/* =========================
   BUTTONS (UNIFIED STYLE)
========================= */
.stButton > button,
.stDownloadButton > button {
    width: 100%;
    border-radius: 14px !important;
    border: 1px solid rgba(0,255,255,0.6) !important;
    background: linear-gradient(90deg, #061225, #0d1f3f) !important;
    color: #00F5FF !important;
    font-weight: 700 !important;
    letter-spacing: 0.4px;
    box-shadow:
        0 0 10px rgba(0,255,255,0.3),
        inset 0 0 10px rgba(255,255,255,0.04);
    transition: all 0.25s ease;
}

a[data-testid="stLinkButton"] {
    display: inline-flex !important;
    justify-content: center;
    align-items: center;
    width: 100% !important;
    padding: 0.6rem 1rem !important;
    border-radius: 14px !important;
    border: 1px solid rgba(0,255,255,0.6) !important;
    background: linear-gradient(90deg, #061225, #0d1f3f) !important;
    color: #00F5FF !important;
    font-weight: 700 !important;
    letter-spacing: 0.4px;
    text-decoration: none !important;
    box-shadow:
        0 0 10px rgba(0,255,255,0.3),
        inset 0 0 10px rgba(255,255,255,0.04);
    transition: all 0.25s ease;
}

.stButton > button:hover,
.stDownloadButton > button:hover,
a[data-testid="stLinkButton"]:hover {
    transform: translateY(-1px) scale(1.02);
    border: 1px solid rgba(255,0,255,0.9) !important;
    color: #FF4DFF !important;
    box-shadow:
        0 0 18px rgba(255,0,255,0.5),
        0 0 35px rgba(0,255,255,0.4);
    text-decoration: none !important;
}

/* =========================
   ARROW BUTTONS
========================= */
div[data-testid="column"] .stButton > button {
    min-height: 56px;
    font-size: 1.25rem !important;
}

/* =========================
   IMAGES
========================= */
img {
    border-radius: 14px;
    box-shadow: 0 0 10px rgba(0,255,255,0.2);
}
"""
inject_css(CSS)


# =========================
# TITLE
# =========================
left_spacer, title_col, right_spacer = st.columns([1, 6, 1])

with title_col:
    with st.container(key="title_box"):
        st.markdown(f"<h1>{PAGE_TITLE}</h1>", unsafe_allow_html=True)


# =========================
# PRESENTATION
# =========================
_, center_col, _ = st.columns([1, 6, 1])

with center_col:
    render_section_label("Presentation")

    with st.container(key="presentation_box"):
        text_to_show = (
            PRESENTATION_TEXT
            if st.session_state.presentation_expanded
            else truncate_text(PRESENTATION_TEXT)
        )

        st.markdown(
            f'<div class="presentation-text">{text_to_show}</div>',
            unsafe_allow_html=True,
        )

        st.button(
            "Voir moins" if st.session_state.presentation_expanded else "Voir plus",
            key="presentation_toggle",
            on_click=toggle_presentation,
        )


# =========================
# CV
# =========================
_, center_col, _ = st.columns([1, 6, 1])

with center_col:
    render_section_label("My CVs")

    with st.container(key="cv_box"):
        col1, col2 = st.columns(2, gap="large")

        with col1:
            exists_fr = CV_FR_PATH.exists()
            data_fr = read_bytes(CV_FR_PATH) if exists_fr else b""

            st.download_button(
                "CV français",
                data=data_fr,
                file_name="CV_MAYEUR_Nicolas.pdf",
                mime="application/pdf",
                disabled=not exists_fr,
                key="cv_fr_button",
            )

            if not exists_fr:
                st.caption("Fichier manquant : assets/cv/CV_MAYEUR_Nicolas.pdf")

        with col2:
            exists_en = CV_EN_PATH.exists()
            data_en = read_bytes(CV_EN_PATH) if exists_en else b""

            st.download_button(
                "English CV",
                data=data_en,
                file_name="CV_MAYEUR_Nicolas_EN.pdf",
                mime="application/pdf",
                disabled=not exists_en,
                key="cv_en_button",
            )

            if not exists_en:
                st.caption("Fichier manquant : assets/cv/cv_en.pdf")


# =========================
# PROJECTS
# =========================
_, center_col, _ = st.columns([1, 6, 1])

with center_col:
    render_section_label("My projects")

    render_project_carousel(
        container_key="project_1_box",
        project_title=PROJECT_TITLES["project_1"],
        images=PROJECT_IMAGES.get("project_1", []),
        key_prefix="project_1",
        project_url=PROJECT_LINKS.get("project_1"),
    )

    render_project_carousel(
        container_key="project_2_box",
        project_title=PROJECT_TITLES["project_2"],
        images=PROJECT_IMAGES.get("project_2", []),
        key_prefix="project_2",
        project_url=PROJECT_LINKS.get("project_2"),
    )

    render_project_carousel(
        container_key="project_3_box",
        project_title=PROJECT_TITLES["project_3"],
        images=PROJECT_IMAGES.get("project_3", []),
        key_prefix="project_3",
        project_url=PROJECT_LINKS.get("project_3"),
    )