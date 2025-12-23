mport streamlit as st
import math

st.set_page_config(page_title="Password Strength Advisor", page_icon="🛡️")

st.title("🛡️ Password Strength Advisor")
st.write("Calculate the 'entropy' of your password without ever typing it.")

# User Inputs via Sidebar or Main Page
length = st.number_input("How many characters long is the password?", min_value=1, max_value=128, value=8)

st.subheader("Which character sets are included?")
col1, col2 = st.columns(2)
with col1:
    has_lower = st.checkbox("Lowercase (a-z)", value=True)
    has_upper = st.checkbox("Uppercase (A-Z)")
with col2:
    has_digits = st.checkbox("Numbers (0-9)")
    has_symbols = st.checkbox("Special Symbols (!@#$)")

# Logic
pool_size = 0
if has_lower: pool_size += 26
if has_upper: pool_size += 26
if has_digits: pool_size += 10
if has_symbols: pool_size += 32

if pool_size > 0:
    entropy = length * math.log2(pool_size)
    combinations = pool_size ** length

    st.divider()
    st.metric(label="Entropy Score", value=f"{entropy:.2f} bits")
    
    if entropy < 40:
        st.error("Strength: VERY WEAK. A modern GPU could crack this in seconds.")
    elif entropy < 60:
        st.warning("Strength: WEAK. Vulnerable to targeted dictionary attacks.")
    elif entropy < 80:
        st.info("Strength: STRONG. This is safe for most personal accounts.")
    else:
        st.success("Strength: VERY STRONG. This is excellent!")
    
    st.write(f"Total possible combinations: `{combinations:,.0f}`")
else:
    st.info("Please select at least one character set above.")
