from __future__ import annotations

from pathlib import Path
from typing import List, Dict, Any

import streamlit as st


# ---------------------------
# Configuration
# ---------------------------
st.set_page_config(page_title="Portfolio", layout="wide")

PAGE_TITLE = "TITRE"

PRESENTATION_TEXT = ("test")

# Path for CV
CV_FR_PATH = Path("assets/cv/cv_fr.pdf")
CV_EN_PATH = Path("assets/cv/cv_en.pdf")

# Path image
PROJECT_IMAGES: Dict[str, List[str]] = {
    "project_1": [],
    "project_2": [],
    "project_3": [],
}


def inject_css(css: str) -> None:
    """Inject CSS into the Streamlit app.

    Args:
        css: CSS string to inject.
    """
    html = f"<style>{css}</style>"
    if hasattr(st, "html"):
        st.html(html)
    else:
        st.markdown(html, unsafe_allow_html=True)


@st.cache_data(show_spinner=False)
def read_bytes(path: Path) -> bytes:
    """Read file content as bytes.

    Args:
        path: File path.

    Returns:
        File content in bytes.
    """
    return path.read_bytes()


def truncate_text(text: str, max_chars: int = 360) -> str:
    """Truncate text to a maximum number of characters.

    Args:
        text: Input text.
        max_chars: Maximum number of characters.

    Returns:
        Truncated text.
    """
    text = text.strip()
    if len(text) <= max_chars:
        return text
    cut = text[:max_chars]
    if " " in cut:
        cut = cut.rsplit(" ", 1)[0]
    return cut + "…"


def toggle_presentation() -> None:
    """Toggle presentation state in session."""
    st.session_state.presentation_expanded = not st.session_state.presentation_expanded


def try_uui_carousel(items: List[Dict[str, Any]], key: str) -> bool:
    """Try to render a UUI carousel.

    Args:
        items: Carousel items.
        key: Unique component key.

    Returns:
        True if carousel is used, False otherwise.
    """
    try:
        from streamlit_carousel_uui import uui_carousel  # type: ignore
    except Exception:
        return False

    uui_carousel(items=items, variant="md", key=key)
    return True


# ---------------------------
# State init
# ---------------------------
if "presentation_expanded" not in st.session_state:
    st.session_state.presentation_expanded = False


# ---------------------------
# Theme
# ---------------------------
CSS = """
/* =========================
   GLOBAL THEME
========================= */
.stApp {
    background:
        radial-gradient(circle at top left, rgba(0, 255, 255, 0.08), transparent 25%),
        radial-gradient(circle at top right, rgba(255, 0, 255, 0.08), transparent 25%),
        linear-gradient(180deg, #050816 0%, #090d1f 100%);
    color: #EAFBFF;
}

div.block-container {
    padding-top: 1.5rem;
    padding-bottom: 3rem;
    max-width: 1400px;
}

/* Optional: hide Streamlit header spacing a bit */
header[data-testid="stHeader"] {
    background: transparent;
}

/* =========================
   TYPOGRAPHY
========================= */
html, body, [class*="css"] {
    font-family: "Segoe UI", "Inter", sans-serif;
}

/* Left labels */
.section-label {
    font-size: 1.3rem;
    font-weight: 700;
    color: #7DF9FF;
    letter-spacing: 0.5px;
    padding-top: 8px;
    text-shadow: 0 0 8px rgba(125, 249, 255, 0.55);
}

/* =========================
   TITLE BAR
========================= */
.st-key-title_bar {
    background: linear-gradient(90deg, #111a3a 0%, #1b1f5e 50%, #0f1d46 100%);
    border: 1px solid rgba(0, 255, 255, 0.55);
    border-radius: 18px;
    padding: 18px 24px;
    box-shadow:
        0 0 12px rgba(0, 255, 255, 0.18),
        0 0 28px rgba(123, 44, 255, 0.22),
        inset 0 0 16px rgba(255, 255, 255, 0.03);
}

.st-key-title_bar h1 {
    margin: 0;
    text-align: center;
    font-size: 2rem;
    font-weight: 800;
    letter-spacing: 2px;
    color: #7DF9FF;
    text-transform: uppercase;
    text-shadow:
        0 0 8px rgba(125, 249, 255, 0.8),
        0 0 18px rgba(125, 249, 255, 0.45),
        0 0 28px rgba(255, 0, 255, 0.25);
}

/* =========================
   PRESENTATION BOX
========================= */
.st-key-presentation_box {
    background: linear-gradient(135deg, rgba(20, 20, 40, 0.95), rgba(10, 15, 30, 0.98));
    border: 1px solid rgba(255, 0, 255, 0.45);
    border-radius: 18px;
    padding: 18px 22px;
    box-shadow:
        0 0 12px rgba(255, 0, 255, 0.14),
        0 0 28px rgba(0, 255, 255, 0.10);
}

.st-key-presentation_box p {
    color: #EAFBFF;
    line-height: 1.7;
    font-size: 1rem;
}

/* =========================
   CV BOXES
========================= */
.st-key-cv_fr_wrap,
.st-key-cv_en_wrap {
    background: linear-gradient(135deg, rgba(8, 18, 28, 0.95), rgba(10, 22, 35, 0.98));
    border: 1px solid rgba(57, 255, 20, 0.55);
    border-radius: 16px;
    padding: 16px;
    box-shadow:
        0 0 10px rgba(57, 255, 20, 0.16),
        inset 0 0 10px rgba(57, 255, 20, 0.04);
}

/* =========================
   PROJECT BOXES
========================= */
.st-key-project_1,
.st-key-project_2,
.st-key-project_3 {
    background: linear-gradient(180deg, rgba(10, 16, 28, 0.98), rgba(7, 10, 20, 1));
    border: 1px solid rgba(0, 255, 255, 0.50);
    border-radius: 18px;
    padding: 16px;
    box-shadow:
        0 0 14px rgba(0, 255, 255, 0.14),
        0 0 26px rgba(123, 44, 255, 0.12);
    min-height: 360px;
}

/* =========================
   BUTTONS
========================= */
.stButton > button,
.stDownloadButton > button {
    width: 100%;
    border-radius: 12px !important;
    border: 1px solid rgba(0, 255, 255, 0.65) !important;
    background: linear-gradient(90deg, #091427 0%, #111f3f 100%) !important;
    color: #7DF9FF !important;
    font-weight: 700 !important;
    letter-spacing: 0.4px;
    box-shadow:
        0 0 8px rgba(0, 255, 255, 0.18),
        inset 0 0 8px rgba(255, 255, 255, 0.03);
    transition: all 0.25s ease-in-out;
}

.stButton > button:hover,
.stDownloadButton > button:hover {
    transform: translateY(-1px);
    border: 1px solid rgba(255, 0, 255, 0.85) !important;
    color: #FF7AF6 !important;
    box-shadow:
        0 0 10px rgba(255, 0, 255, 0.28),
        0 0 22px rgba(0, 255, 255, 0.18);
}

/* Presentation toggle button spacing */
.st-key-presentation_toggle button {
    margin-top: 10px;
}

/* =========================
   SLIDER FALLBACK
========================= */
[data-baseweb="slider"] {
    padding-top: 0.8rem;
    padding-bottom: 0.6rem;
}

/* =========================
   CAPTIONS / INFO TEXT
========================= */
.stCaption, .stAlert {
    color: #CDEEFF;
}

/* =========================
   IMAGES
========================= */
img {
    border-radius: 14px;
}

/* =========================
   OPTIONAL CYBER LINES EFFECT
========================= */
.st-key-title_bar::before,
.st-key-presentation_box::before,
.st-key-project_1::before,
.st-key-project_2::before,
.st-key-project_3::before,
.st-key-cv_fr_wrap::before,
.st-key-cv_en_wrap::before {
    content: "";
    display: block;
    height: 1px;
    width: 100%;
    background: linear-gradient(90deg, transparent, rgba(0,255,255,0.7), transparent);
    margin-bottom: 12px;
    box-shadow: 0 0 8px rgba(0,255,255,0.4);
}
"""
inject_css(CSS)


# ---------------------------
# Page organisation
# ---------------------------

# Title
left_spacer, title_col, right_spacer = st.columns([1, 6, 1])
with title_col:
    with st.container(key="title_bar"):
        st.markdown(f"<h1>{PAGE_TITLE}</h1>", unsafe_allow_html=True)

st.write("")

# --- Presentation ---
label_col, content_col = st.columns([1, 6])
with label_col:
    st.markdown('<div class="section-label">Presentation</div>', unsafe_allow_html=True)

with content_col:
    with st.container(key="presentation_box"):
        text_to_show = (
            PRESENTATION_TEXT
            if st.session_state.presentation_expanded
            else truncate_text(PRESENTATION_TEXT)
        )
        st.markdown(text_to_show)
        st.button(
            "Voir moins" if st.session_state.presentation_expanded else "Voir plus",
            key="presentation_toggle",
            on_click=toggle_presentation,
        )

st.write("")

# --- My CV ---
label_col, content_col = st.columns([1, 6])
with label_col:
    st.markdown('<div class="section-label">My CV</div>', unsafe_allow_html=True)

with content_col:
    b1, b2, _ = st.columns([1, 1, 2])

    # CV français
    with b1:
        with st.container(key="cv_fr_wrap"):
            exists = CV_FR_PATH.exists()
            data = read_bytes(CV_FR_PATH) if exists else b""
            st.download_button(
                "CV français",
                data=data,
                file_name="CV_francais.pdf",
                mime="application/pdf",
                key="cv_fr_button",
                on_click="ignore",
                disabled=not exists,
                width="stretch",
            )
            if not exists:
                st.caption("Fichier manquant : assets/cv/cv_fr.pdf")

    # English CV
    with b2:
        with st.container(key="cv_en_wrap"):
            exists = CV_EN_PATH.exists()
            data = read_bytes(CV_EN_PATH) if exists else b""
            st.download_button(
                "English CV",
                data=data,
                file_name="English_CV.pdf",
                mime="application/pdf",
                key="cv_en_button",
                on_click="ignore",
                disabled=not exists,
                width="stretch",
            )
            if not exists:
                st.caption("Fichier manquant : assets/cv/cv_en.pdf")

st.write("")

# --- My projets ---
label_col, content_col = st.columns([1, 6])
with label_col:
    st.markdown('<div class="section-label">Mes projets</div>', unsafe_allow_html=True)

with content_col:
    c1, c2, c3 = st.columns(3, gap="large")

    def render_project_zone(container_key: str, carousel_key: str, images: List[str]) -> None:
        with st.container(key=container_key):

            if not images:
                st.info("Aucune image disponible")
                return

            try:
                from streamlit_carousel_uui import uui_carousel

                items = [
                    {
                        "title": f"Image {i+1}",
                        "img": img,
                    }
                    for i, img in enumerate(images)
                ]

                uui_carousel(
                    items=items,
                    variant="card",   # style moderne
                    key=carousel_key,
                )

            except Exception:
            # fallback si package non installé
                st.warning("Installe streamlit-carousel-uui pour un vrai carrousel")
                idx = st.slider(
                    "Image",
                    1,
                    len(images),
                    1,
                    key=f"{carousel_key}_fallback",
                    label_visibility="collapsed",
                )
                st.image(images[idx - 1], use_container_width=True)


    with c1:
        render_project_zone("project_1", "carousel_1", PROJECT_IMAGES.get("project_1", []))

    with c2:
        render_project_zone("project_2", "carousel_2", PROJECT_IMAGES.get("project_2", []))

    with c3:
        render_project_zone("project_3", "carousel_3", PROJECT_IMAGES.get("project_3", []))