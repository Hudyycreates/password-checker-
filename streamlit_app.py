import streamlit as st
import math

# --- STEP 1: UI SETUP ---
st.title("🛡️ Cyber-Santa Password Grader")
st.write("Is your password on the Naughty or Nice list? Let's check the math.")

# User inputs: We don't need the actual password, just the stats
length = st.number_input("Password Length", min_value=0, value=8)

col1, col2 = st.columns(2)
with col1:
    use_lower = st.checkbox("Lowercase (a-z)", value=True)
    use_upper = st.checkbox("Uppercase (A-Z)")
with col2:
    use_number = st.checkbox("Numbers (0-9)")
    use_symbol = st.checkbox("Symbols (!@#$)")

# --- STEP 2: CALCULATING THE CHARACTER POOL (R) ---
# 'R' represents the number of possible characters for each 'slot' in the password.
r_value = 0
if use_lower: r_value += 26
if use_upper: r_value += 26
if use_number: r_value += 10
if use_symbol: r_value += 32

# --- STEP 3: THE CORE MATH (ENTROPY & COMBINATIONS) ---
if r_value > 0 and length > 0:
    # Entropy (E) formula: E = L * log2(R)
    # This tells us how many 'bits' of randomness the password contains.
    entropy = length * math.log2(r_value)
    
    # Total Combinations: R raised to the power of L
    # This represents every possible variation a hacker would have to guess.
    total_combinations = r_value ** length
    
    # --- STEP 4: ESTIMATING CRACK TIME ---
    # We assume a high-end cracking rig doing 100 Billion guesses per second.
    guesses_per_sec = 100_000_000_000
    seconds = total_combinations / guesses_per_sec
    
    # --- STEP 5: THE "VERDICT" LOGIC ---
    st.subheader(f"Entropy Score: {entropy:.2f} bits")
    
    if entropy < 40:
        st.error("Verdict: 🎅 NAUGHTY (Very Weak)")
    elif entropy < 60:
        st.warning("Verdict: 🌙 GETTING BETTER (Decent)")
    else:
        st.success("Verdict: 🌟 NICE (Strong Password)")

    # Convert seconds into a human-readable format
    if seconds < 60:
        st.write(f"Time to crack: {seconds:.2f} seconds")
    elif seconds < 3600:
        st.write(f"Time to crack: {seconds/60:.2f} minutes")
    elif seconds < 86400:
        st.write(f"Time to crack: {seconds/3600:.2f} hours")
    else:
        st.write(f"Time to crack: {seconds/86400:,.0f} days")
else:
    st.info("Select character types to calculate strength.")
