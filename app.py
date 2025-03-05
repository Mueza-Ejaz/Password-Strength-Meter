import streamlit as st
from password_checker import check_password_strength
from password_generator import generate_strong_password

# Streamlit Page Config
st.set_page_config(
    page_title="Password Strength Meter",
    page_icon="🔐",
    layout="centered",
)

# Custom CSS for Better Visibility
st.markdown("""
    <style>
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #F3F8FF, #DDEBF7, #BFD7ED);
    /* Soft Sky Blue (#F3F8FF), Light Cool Blue (#DDEBF7), Muted Pastel Blue (#BFD7ED) */
}

/* Header Background */
[data-testid="stHeader"] {
    background-color: transparent;
}

/* Headings */
h1 {
    color: #0D47A1 !important;  /* Deep Navy Blue */
    text-align: center;
}

h3 {
    color: #1B263B !important;  /* Slightly Darker for Subtitles */
}

/* Paragraphs & Labels */
p, label {
    color: #1B263B;  /* Deep Navy */
    text-align: center;
}

/* Input Field */
.stTextInput>div>div>input {
    border: 2px solid #1565C0; /* Bold Blue Border */
    border-radius: 8px;
    padding: 10px;
    background-color: white; /* White Background */
    color: black; /* Black Text for Readability */
}

/* Hide "Press Enter to Apply" */
.stTextInput>div>div>div {
    display: none;
}

/* Button Styling */
.stButton>button {
    background: linear-gradient(90deg, #00C9A7, #005F73); /* Blue-Green Gradient */
    color: white;
    padding: 12px 24px;
    border-radius: 8px;
    font-size: 16px;
    font-weight: bold;
    transition: 0.3s;
}
.stButton>button:hover {
    background: linear-gradient(90deg, #005F73, #00C9A7);
}

/* Footer */
footer p {
    color: #1B263B; /* Deep Navy */
}
</style>
""", unsafe_allow_html=True)

# Logo Image (Ensure it's in the same folder)
st.image("logo.png", width=150)

# Header
st.markdown("<h1> Password Strength Meter</h1>", unsafe_allow_html=True)  #  Styled Heading
st.markdown("<p> Ensure your password is strong and secure!</p>", unsafe_allow_html=True)

# User Input Field
password = st.text_input(" **Enter Your Password**", type="password", placeholder="Type your password here...")

# Check Password Strength
if st.button(" Check Strength"):
    if password:
        score, strength, feedback = check_password_strength(password) 
        
        st.markdown(f"<h3 style='color: #0D47A1;'> Score: {score}/5</h3>", unsafe_allow_html=True)
        
        if strength == "Strong":
            st.success("  **Strong Password!**")
        elif strength == "Moderate":
            st.warning("  **Moderate Password - Consider adding more security features.**")
        else:
            st.error("  **Weak Password - Improve it using these tips:**")
            for tip in feedback:
                st.write(f" - {tip}")
    else:
        st.error("  Please enter a password!")

# Generate Strong Password
if st.button(" Suggest a Strong Password"):
    strong_password = generate_strong_password()
    st.success(f" **Suggested Strong Password:** `{strong_password}`")

# Footer
st.markdown("<p style='text-align: center; font-size: 14px; color: #1B263B;'> Secure your accounts with a strong password!</p>", unsafe_allow_html=True)
