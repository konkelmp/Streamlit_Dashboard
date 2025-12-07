import streamlit as st

st.set_page_config(page_title="Professional Bio", page_icon="👤", layout="centered")

st.title("👤 Professional Bio")

# --- Short Professional Summary ---
st.subheader("Summary")
st.write("""
I am a part‑time software support specialist with hands‑on experience in scripting, troubleshooting, and data visualization. 
My background includes nearly completing a Computer Science degree and three years in IT support, where I honed skills in UNIX systems, secure file handling, and workflow optimization. 
I specialize in building interactive dashboards and exploratory data analysis tools using Python, Pandas, Plotly, and Streamlit. 
My interests span systems‑level programming, cryptographic workflows, and sports analytics, with a strong emphasis on clarity and reproducibility.
""")

# --- Profile Image (Optional) ---
st.subheader("Profile")
st.image("profile.jpg", caption="Exploring clarity in code, data, and design.", width=200)  # replace with your image file
st.write("Alt-text: Profile photo of Preston, software support specialist and data visualization enthusiast.")

# --- Highlights ---
st.subheader("Highlights")
st.markdown("""
- 📊 Skilled in Python libraries: **Pandas, Seaborn, Matplotlib, Plotly, Streamlit**
- 🖥️ Strong UNIX background: file systems, permissions, and command‑line troubleshooting
- 🔐 Experience with **cryptographic key generation** and secure file I/O in Java
- 📈 Dashboard storytelling with **Tableau** and calculated fields/LOD expressions
- ⚙️ Methodical troubleshooting across technical, financial, and mechanical systems
""")

# --- Visualization Philosophy ---
st.subheader("Visualization Philosophy")
st.write("""
I believe effective visualization should prioritize **clarity, accessibility, and ethical responsibility**:
- Charts must be intuitive, with scales and encodings that minimize misinterpretation.
- Accessibility means designing for diverse audiences, ensuring readability and inclusivity.
- Ethical visualization requires transparency: data should be represented honestly, without distortion or bias.
- Ultimately, the goal is to empower users to make informed decisions through clear, reproducible insights.
""")
