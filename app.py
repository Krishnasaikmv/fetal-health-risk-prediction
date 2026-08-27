import streamlit as st
import numpy as np
import tensorflow as tf
from PIL import Image

st.set_page_config(
    page_title="Fetal Health Risk Prediction System",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="collapsed"
)

if "page" not in st.session_state:
    st.session_state.page = "home"

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

:root{
    --bg:#f4f7fb;
    --bg2:#eaf1fb;
    --card:rgba(255,255,255,0.80);
    --card-border:rgba(255,255,255,0.58);
    --text:#14213d;
    --muted:#5b6b82;
    --primary:#2563eb;
    --primary2:#1d4ed8;
    --accent:#0ea5a4;
    --danger:#dc2626;
    --warn:#d97706;
    --success:#16a34a;
    --shadow:0 18px 50px rgba(31,41,55,0.10);
    --radius:22px;
}

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp{
    background:
        radial-gradient(circle at top left, rgba(37,99,235,0.14), transparent 28%),
        radial-gradient(circle at top right, rgba(14,165,164,0.12), transparent 24%),
        linear-gradient(135deg, var(--bg), var(--bg2));
    color: var(--text);
}

.block-container{
    padding-top: 1.5rem;
    padding-bottom: 2rem;
    max-width: 1200px;
}

header[data-testid="stHeader"] {
    background: transparent;
}

#MainMenu, footer {
    visibility: hidden;
}

h1, h2, h3{
    color: var(--text);
    letter-spacing: -0.02em;
}

.hero-box{
    position: relative;
    overflow: hidden;
    padding: 2.8rem 2.3rem;
    border-radius: 30px;
    background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 55%, #0ea5a4 100%);
    color: white;
    box-shadow: 0 22px 60px rgba(15,23,42,0.28);
    margin-bottom: 1.5rem;
}

.hero-box::before{
    content: "";
    position: absolute;
    width: 320px;
    height: 320px;
    right: -80px;
    top: -80px;
    background: rgba(255,255,255,0.10);
    border-radius: 50%;
}

.hero-box::after{
    content: "";
    position: absolute;
    width: 220px;
    height: 220px;
    left: -50px;
    bottom: -80px;
    background: rgba(255,255,255,0.08);
    border-radius: 50%;
}

.hero-title{
    font-size: 2.5rem;
    font-weight: 800;
    margin-bottom: 0.75rem;
    position: relative;
    z-index: 2;
}

.hero-sub{
    font-size: 1.03rem;
    line-height: 1.8;
    max-width: 760px;
    color: rgba(255,255,255,0.92);
    position: relative;
    z-index: 2;
}

.hero-tags{
    display:flex;
    flex-wrap:wrap;
    gap:10px;
    margin-top: 1.1rem;
    position: relative;
    z-index: 2;
}

.hero-tag{
    padding: 8px 14px;
    border-radius: 999px;
    background: rgba(255,255,255,0.14);
    border: 1px solid rgba(255,255,255,0.16);
    font-size: 0.92rem;
    backdrop-filter: blur(8px);
}

.glass-card{
    background: var(--card);
    border: 1px solid var(--card-border);
    backdrop-filter: blur(14px);
    border-radius: var(--radius);
    box-shadow: var(--shadow);
    padding: 1.25rem;
    margin-top: 1rem;
}

.section-title{
    font-size: 1.1rem;
    font-weight: 700;
    color: var(--text);
    margin-bottom: 0.25rem;
}

.section-subtitle{
    color: var(--muted);
    font-size: 0.95rem;
    margin-bottom: 0.9rem;
}

.dashboard-card{
    background: linear-gradient(180deg, rgba(255,255,255,0.92), rgba(246,249,255,0.92));
    border: 1px solid rgba(220,228,240,0.85);
    padding: 22px;
    border-radius: 22px;
    box-shadow: 0 14px 34px rgba(15,23,42,0.08);
    text-align: center;
}

.dashboard-card h4{
    margin-bottom: 12px;
    color: var(--muted);
    font-weight: 600;
}

.risk-badge{
    padding: 10px 18px;
    border-radius: 999px;
    font-weight: 800;
    letter-spacing: 0.03em;
    display: inline-block;
    min-width: 110px;
    font-size: 0.92rem;
}

.high{
    background: rgba(220,38,38,0.12);
    color: #b91c1c;
    border: 1px solid rgba(220,38,38,0.22);
}

.medium{
    background: rgba(217,119,6,0.12);
    color: #b45309;
    border: 1px solid rgba(217,119,6,0.22);
}

.low{
    background: rgba(22,163,74,0.12);
    color: #15803d;
    border: 1px solid rgba(22,163,74,0.22);
}

.data-grid{
    display:grid;
    grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
    gap: 12px;
    margin-top: 12px;
}

.data-pill{
    background: rgba(37,99,235,0.05);
    border: 1px solid rgba(37,99,235,0.10);
    border-radius: 16px;
    padding: 12px 14px;
}

.data-pill span{
    display:block;
}

.data-pill .label{
    color: var(--muted);
    font-size: 0.82rem;
    margin-bottom: 2px;
}

.data-pill .value{
    color: var(--text);
    font-size: 1rem;
    font-weight: 700;
}

.food-list{
    display:grid;
    grid-template-columns: repeat(auto-fit,minmax(220px,1fr));
    gap: 12px;
    margin-top: 12px;
}

.food-item{
    padding: 12px 14px;
    border-radius: 16px;
    background: linear-gradient(180deg, #ffffff, #f7fbff);
    border: 1px solid #e6eef8;
    color: var(--text);
    font-weight: 600;
    box-shadow: 0 8px 18px rgba(37,99,235,0.06);
}

.nav-btn .stButton > button,
.stButton > button{
    width: 100%;
    border: none;
    border-radius: 16px;
    min-height: 52px;
    font-weight: 700;
    font-size: 1rem;
    color: white;
    background: linear-gradient(135deg, var(--primary), var(--primary2));
    box-shadow: 0 12px 26px rgba(37,99,235,0.26);
    transition: 0.25s ease;
}

.stButton > button:hover{
    transform: translateY(-2px);
    box-shadow: 0 16px 30px rgba(37,99,235,0.32);
}

.secondary-btn .stButton > button{
    background: white;
    color: var(--text);
    border: 1px solid #d8e2f0;
    box-shadow: 0 10px 24px rgba(15,23,42,0.06);
}

.stNumberInput, .stSelectbox, .stFileUploader{
    margin-bottom: 0.5rem;
}

div[data-baseweb="input"] > div,
div[data-baseweb="select"] > div{
    border-radius: 14px !important;
    border: 1px solid #d8e2f0 !important;
    background: rgba(255,255,255,0.85) !important;
}

[data-testid="stFileUploader"] section{
    border-radius: 18px !important;
    border: 2px dashed rgba(37,99,235,0.28) !important;
    background: rgba(255,255,255,0.70) !important;
    padding: 1.1rem !important;
}

[data-testid="stFileUploaderDropzone"]{
    background: transparent !important;
}

.small-note{
    font-size: 0.9rem;
    color: var(--muted);
    margin-top: 6px;
}

.topbar{
    display:flex;
    justify-content:space-between;
    align-items:center;
    gap:1rem;
    margin-bottom: 0.6rem;
}

.page-title{
    font-size: 1.4rem;
    font-weight: 800;
    color: var(--text);
}

.page-subtitle{
    color: var(--muted);
    font-size: 0.95rem;
}

@media (max-width: 768px){
    .hero-title{
        font-size: 1.8rem;
    }
    .hero-sub{
        font-size: 0.95rem;
    }
    .block-container{
        padding-top: 1rem;
    }
}
</style>
""", unsafe_allow_html=True)

try:
    ultra_model = tf.saved_model.load("final_saved_model")
    infer = ultra_model.signatures["serving_default"]
    model_loaded = True
except Exception:
    infer = None
    model_loaded = False

class_labels = {
    0: "Fetal abdomen",
    1: "Fetal brain",
    2: "Fetal femur",
    3: "Fetal thorax",
    4: "Maternal cervix",
    5: "Other"
}

RISK_MAPPING = {
    "Fetal brain": "HIGH",
    "Maternal cervix": "HIGH",
    "Fetal thorax": "MEDIUM",
    "Fetal abdomen": "MEDIUM",
    "Fetal femur": "LOW",
    "Other": "LOW"
}

CONF_THRESHOLD = 0.90


def go_to_assessment():
    st.session_state.page = "assessment"


def go_to_home():
    st.session_state.page = "home"


def predict_plane(image):
    img = image.resize((224, 224))
    img = np.array(img) / 255.0
    img = np.expand_dims(img, axis=0)
    preds = infer(tf.convert_to_tensor(img, dtype=tf.float32))
    preds = list(preds.values())[0].numpy()[0]

    if np.max(preds) < CONF_THRESHOLD:
        return "NON-FETAL"

    return class_labels[np.argmax(preds)]


def aggregate_ultrasonic_risk(risks):
    if not risks:
        return "LOW"
    if "HIGH" in risks:
        return "HIGH"
    elif risks.count("MEDIUM") >= risks.count("LOW"):
        return "MEDIUM"
    return "LOW"


def predict_nutrition_risk(age, systolic, diastolic, blood_sugar, body_temp,
                           bmi, prev, pre, gest, mental, heart):
    score = 0

    if bmi >= 30 or bmi < 18.5:
        score += 2
    elif bmi >= 25:
        score += 1

    if systolic >= 140 or diastolic >= 90:
        score += 2
    elif systolic >= 120:
        score += 1

    if blood_sugar >= 140:
        score += 2
    elif blood_sugar >= 110:
        score += 1

    if age >= 35 or age < 20:
        score += 1

    if body_temp >= 100:
        score += 1

    if heart >= 110 or heart < 55:
        score += 1

    score += prev + pre + gest + mental

    if score >= 6:
        return "HIGH"
    elif score >= 3:
        return "MEDIUM"
    return "LOW"


def calculate_final_risk(u, n):
    if u == "HIGH" or n == "HIGH":
        return "HIGH"
    elif u == "MEDIUM" or n == "MEDIUM":
        return "MEDIUM"
    return "LOW"


def map_risk_to_food_level(risk):
    if risk == "HIGH":
        return "HIGH"
    if risk == "MEDIUM":
        return "MID"
    return "LOW"


def get_condition_label(bmi, blood_sugar, systolic, diastolic):
    if bmi >= 30:
        return "OBESE"
    elif bmi < 18.5:
        return "UNDERWEIGHT"
    elif blood_sugar >= 140:
        return "HIGH_SUGAR"
    elif systolic >= 140 or diastolic >= 90:
        return "HIGH_BP"
    return "NORMAL"


def get_food_plan(final_risk, condition):
    food_plan = []
    risk_level = map_risk_to_food_level(final_risk)

    if risk_level == "LOW":
        food_plan += [
            "Balanced home-cooked food",
            "Fresh fruits and vegetables"
        ]
    elif risk_level == "MID":
        food_plan += [
            "High-protein foods",
            "Iron-rich foods",
            "Folic acid sources"
        ]
    else:
        food_plan += [
            "Doctor-advised nutrition plan",
            "Strict diet monitoring"
        ]

    if condition == "OBESE":
        food_plan += [
            "Low-calorie foods",
            "High fiber diet",
            "Avoid fried and sugary foods"
        ]
    elif condition == "UNDERWEIGHT":
        food_plan += [
            "Calorie-dense healthy foods",
            "Milk, nuts, bananas",
            "Small frequent meals"
        ]
    elif condition == "HIGH_SUGAR":
        food_plan += [
            "Low glycemic index foods",
            "Avoid sweets and refined carbohydrates",
            "More vegetables and pulses"
        ]
    elif condition == "HIGH_BP":
        food_plan += [
            "Low salt diet",
            "Potassium-rich foods (banana, spinach)",
            "Avoid packaged food"
        ]
    else:
        food_plan += [
            "Adequate hydration",
            "Maintain current healthy diet"
        ]

    return food_plan


def get_class(risk):
    return "high" if risk == "HIGH" else "medium" if risk == "MEDIUM" else "low"


def render_home_page():
    st.markdown("""
    <div class="hero-box">
        <div class="hero-title">🩺 Fetal Health Risk Prediction System</div>
        <div class="hero-sub">
            Smart prenatal screening dashboard that combines fetal ultrasound image analysis
            and maternal clinical indicators to estimate overall health risk through a clean,
            modern, hospital-style interface.
        </div>
        <div class="hero-tags">
            <div class="hero-tag">AI Powered</div>
            <div class="hero-tag">Ultrasound Classification</div>
            <div class="hero-tag">Clinical Risk Analysis</div>
            <div class="hero-tag">Diet Recommendation</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("""
        <div class="glass-card">
            <div class="section-title">Upload Scan Images</div>
            <div class="section-subtitle">Add fetal ultrasound images for plane validation and ultrasonic risk assessment.</div>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown("""
        <div class="glass-card">
            <div class="section-title">Enter Clinical Data</div>
            <div class="section-subtitle">Provide BP, sugar, BMI, temperature, and maternal history details.</div>
        </div>
        """, unsafe_allow_html=True)
    with c3:
        st.markdown("""
        <div class="glass-card">
            <div class="section-title">Get Final Risk</div>
            <div class="section-subtitle">View ultrasound risk, nutrition risk, final risk level, and diet suggestions.</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="glass-card">
        <div class="section-title">System Overview</div>
        <div class="section-subtitle">
            This application is a decision-support system for prenatal screening workflows.
            Click the button below to begin the assessment process on the next page.
        </div>
    </div>
    """, unsafe_allow_html=True)

    left, center, right = st.columns([1, 1.2, 1])
    with center:
        st.button("Start Process", on_click=go_to_assessment, use_container_width=True)


def render_assessment_page():
    top1, top2 = st.columns([5, 1.4])
    with top1:
        st.markdown("""
        <div class="topbar">
            <div>
                <div class="page-title">Assessment & Result Dashboard</div>
                <div class="page-subtitle">Provide the required inputs and view the complete risk summary below.</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    with top2:
        st.markdown('<div class="secondary-btn">', unsafe_allow_html=True)
        st.button("← Back Home", on_click=go_to_home, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    if not model_loaded:
        st.warning("Model folder 'final_saved_model' was not found or could not be loaded. Predictions will work only after the model is available.")

    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Ultrasound Image Input</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-subtitle">Upload the exact number of fetal ultrasound images required for analysis.</div>', unsafe_allow_html=True)
    num_images = st.number_input("Number of Ultrasound Images", min_value=1, step=1)
    uploaded = st.file_uploader("Upload Images", accept_multiple_files=True, type=["png", "jpg", "jpeg"])
    st.markdown('<div class="small-note">Accepted formats: PNG, JPG, JPEG</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    planes = []
    ultra_risks = []
    valid_uploads = True

    if uploaded:
        if len(uploaded) != num_images:
            st.warning("Please upload the exact number of images selected above.")
            valid_uploads = False
        else:
            st.markdown('<div class="glass-card">', unsafe_allow_html=True)
            st.markdown('<div class="section-title">Uploaded Image Preview</div>', unsafe_allow_html=True)
            cols = st.columns(len(uploaded))
            for i, file in enumerate(uploaded):
                img = Image.open(file).convert("RGB")
                cols[i].image(img, use_container_width=True)
                if model_loaded:
                    plane = predict_plane(img)
                    if plane == "NON-FETAL":
                        st.error(f"Image {i+1} appears invalid or confidence is below the threshold. Please upload a valid fetal ultrasound image.")
                        valid_uploads = False
                    else:
                        planes.append(plane)
                        ultra_risks.append(RISK_MAPPING[plane])
                        cols[i].caption(f"Detected: {plane}")
            st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Maternal Clinical Data</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-subtitle">Enter maternal parameters for risk evaluation.</div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.number_input("Age", min_value=0, step=1)
        systolic = st.number_input("Systolic BP", min_value=0, step=1)
        diastolic = st.number_input("Diastolic BP", min_value=0, step=1)
        blood_sugar = st.number_input("Blood Sugar", min_value=0, step=1)
    with col2:
        body_temp = st.number_input("Body Temp", min_value=0, step=1)
        bmi = st.number_input("BMI", min_value=0.0, step=0.1)
        heart = st.number_input("Heart Rate", min_value=0, step=1)
    with col3:
        prev = st.selectbox("Previous Complications", [0, 1])
        pre = st.selectbox("Preexisting Diabetes", [0, 1])
        gest = st.selectbox("Gestational Diabetes", [0, 1])
        mental = st.selectbox("Mental Health", [0, 1])
    st.markdown('</div>', unsafe_allow_html=True)

    if st.button("Find Final Risk"):
        if not uploaded:
            st.warning("Please upload ultrasound images before predicting risk.")
        elif not valid_uploads:
            st.warning("Please correct the uploaded images and try again.")
        elif not model_loaded:
            st.error("Model is not loaded. Place the TensorFlow SavedModel inside 'final_saved_model' and rerun the app.")
        else:
            ultra_final = aggregate_ultrasonic_risk(ultra_risks)
            nutri = predict_nutrition_risk(
                age, systolic, diastolic, blood_sugar,
                body_temp, bmi, prev, pre, gest, mental, heart
            )
            final = calculate_final_risk(ultra_final, nutri)
            condition = get_condition_label(bmi, blood_sugar, systolic, diastolic)
            foods = get_food_plan(final, condition)

            c1, c2, c3 = st.columns(3)
            c1.markdown(f"""
            <div class="dashboard-card">
                <h4>Ultrasound Risk</h4>
                <div class="risk-badge {get_class(ultra_final)}">{ultra_final}</div>
            </div>
            """, unsafe_allow_html=True)
            c2.markdown(f"""
            <div class="dashboard-card">
                <h4>Nutrition Risk</h4>
                <div class="risk-badge {get_class(nutri)}">{nutri}</div>
            </div>
            """, unsafe_allow_html=True)
            c3.markdown(f"""
            <div class="dashboard-card">
                <h4>Final Risk</h4>
                <div class="risk-badge {get_class(final)}">{final}</div>
            </div>
            """, unsafe_allow_html=True)

            if planes:
                plane_items = "".join(
                    f"<div class='food-item'>{idx + 1}. {plane}</div>"
                    for idx, plane in enumerate(planes)
                )
                st.markdown('<div class="glass-card">', unsafe_allow_html=True)
                st.markdown('<div class="section-title">Detected Ultrasound Planes</div>', unsafe_allow_html=True)
                st.markdown('<div class="section-subtitle">The model identified the following ultrasound views from the uploaded images.</div>', unsafe_allow_html=True)
                st.markdown(f"<div class='food-list'>{plane_items}</div>", unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)

            st.markdown('<div class="glass-card">', unsafe_allow_html=True)
            st.markdown('<div class="section-title">Patient Summary</div>', unsafe_allow_html=True)
            st.markdown(f"""
            <div class="data-grid">
                <div class="data-pill"><span class="label">Age</span><span class="value">{age}</span></div>
                <div class="data-pill"><span class="label">Systolic BP</span><span class="value">{systolic}</span></div>
                <div class="data-pill"><span class="label">Diastolic BP</span><span class="value">{diastolic}</span></div>
                <div class="data-pill"><span class="label">Blood Sugar</span><span class="value">{blood_sugar}</span></div>
                <div class="data-pill"><span class="label">Body Temp</span><span class="value">{body_temp}</span></div>
                <div class="data-pill"><span class="label">BMI</span><span class="value">{bmi}</span></div>
                <div class="data-pill"><span class="label">Heart Rate</span><span class="value">{heart}</span></div>
                <div class="data-pill"><span class="label">Previous Complications</span><span class="value">{prev}</span></div>
                <div class="data-pill"><span class="label">Preexisting Diabetes</span><span class="value">{pre}</span></div>
                <div class="data-pill"><span class="label">Gestational Diabetes</span><span class="value">{gest}</span></div>
                <div class="data-pill"><span class="label">Mental Health</span><span class="value">{mental}</span></div>
                <div class="data-pill"><span class="label">Condition</span><span class="value">{condition}</span></div>
            </div>
            """, unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

            st.markdown('<div class="glass-card">', unsafe_allow_html=True)
            st.markdown('<div class="section-title">Recommended Diet Plan</div>', unsafe_allow_html=True)
            st.markdown('<div class="section-subtitle">Diet suggestions are generated using final risk level and maternal condition.</div>', unsafe_allow_html=True)
            food_html = "".join(
                f"<div class='food-item'>{idx + 1}. {food}</div>"
                for idx, food in enumerate(foods)
            )
            st.markdown(f"<div class='food-list'>{food_html}</div>", unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)


if st.session_state.page == "home":
    render_home_page()
else:
    render_assessment_page()