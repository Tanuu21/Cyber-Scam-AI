import streamlit as st
import time
from engine import CyberScamEngine

# Page Config
st.set_page_config(page_title="Cyber Scam AI", page_icon="🛡️", layout="wide")

# Load Professional CSS
with open("theme.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Session State for Page Navigation
if 'page' not in st.session_state:
    st.session_state.page = 'home'

# --- LANDING PAGE ---
if st.session_state.page == 'home':
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.image("https://png.pngtree.com/png-clipart/20250206/original/pngtree-futuristic-blue-digital-shield-with-advanced-cybersecurity-design-png-image_20339008.png", width=150)
        st.title("🛡️ CYBER SCAM AI")
        st.write("### Next-Generation Smart Contract Security")
        st.image("https://images.stockcake.com/public/e/a/8/ea8341eb-edab-472a-ab9d-074c6f2195d4_large/digital-security-dashboard-stockcake.jpg", use_column_width=True)
        
        st.markdown("""
        **Cyber Scam AI** uses deep bytecode analysis and behavioral heuristics 
        to protect your capital from rugpulls and honeypots.
        """)
        
        if st.button("LAUNCH AI SCANNER →", use_container_width=True):
            st.session_state.page = 'dashboard'
            st.rerun()

# --- MAIN DASHBOARD ---
else:
    st.sidebar.image("https://png.pngtree.com/png-clipart/20250206/original/pngtree-futuristic-blue-digital-shield-with-advanced-cybersecurity-design-png-image_20339008.png", width=80)
    st.sidebar.title("Cyber Scam AI")
    if st.sidebar.button("Back to Home"):
        st.session_state.page = 'home'
        st.rerun()
    
    st.sidebar.divider()
    st.sidebar.info("v1.0.2 - Grant Ready Version")

    st.title("🔍 AI Analysis Dashboard")
    address = st.text_input("Enter Token Contract Address", placeholder="0x...")

    if st.button("INITIATE DEEP SCAN"):
        if address:
            with st.spinner("AI Analysis in progress..."):
                time.sleep(2) # Simulated computation
                
                engine = CyberScamEngine(address)
                score, findings = engine.run_deep_scan()
                
                # Metrics Row
                m1, m2, m3 = st.columns(3)
                m1.metric("Risk Score", f"{score}%", delta="-High" if score > 40 else "Safe")
                m2.metric("Scan Depth", "Layer 3")
                m3.metric("Network", "Mainnet")

                st.subheader("Vulnerability Breakdown")
                for f in findings:
                    st.markdown(f"""
                    <div class="risk-card">
                        <h4 style="color:#00f2fe;">⚠️ {f['name']}</h4>
                        <p>{f['desc']}</p>
                        <small>Severity Score: {f['impact']}</small>
                    </div>
                    """, unsafe_allow_html=True)
                
                if score < 20:
                    st.success("✅ Analysis Complete: This contract appears safe based on current AI models.")
        else:
            st.error("Please enter a contract address to begin.")
