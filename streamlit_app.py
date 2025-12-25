import streamlit as st
import math

# Page config
st.set_page_config(page_title="Cyber-Santa's Password Grader", page_icon="🎄")

st.title("🎄 Cyber-Santa's Password Grader")
st.write("Is your password a gift to hackers or a fortress of joy?")

# 1. Inputs
length = st.number_input("How many characters long is it?", min_value=1, max_value=128, value=8)

st.subheader("What's inside?")
col1, col2 = st.columns(2)
with col1:
    has_lower = st.checkbox("Lowercase letters (a-z)", value=True)
    has_upper = st.checkbox("Uppercase letters (A-Z)")
with col2:
    has_digits = st.checkbox("Numbers (0-9)")
    has_symbols = st.checkbox("Special Symbols (!@#$)")

# 2. Logic
pool_size = 0
if has_lower: pool_size += 26
if has_upper: pool_size += 26
if has_digits: pool_size += 10
if has_symbols: pool_size += 32

if pool_size > 0:
    entropy = length * math.log2(pool_size)
    combinations = pool_size ** length
    
    # Cracking Speed (100 Billion per sec)
    seconds_to_crack = combinations / 100_000_000_000
    
    st.divider()

    # 3. THE FUNNY RANKING SECTION
    st.subheader("🎅 Cyber-Santa's Verdict:")

    if entropy < 40:
        st.error("🚨 NAUGHTY LIST DETECTED!")
        st.write("**Verdict:** Your password is like leaving your front door open with a 'Welcome' mat for hackers. Even the Grinch could crack this in seconds. **You need to improve!**")
    elif entropy < 70:
        st.warning("⚠️ GETTING WARMER...")
        st.write("**Verdict:** It's okay, but a determined elf with a laptop could still break in. Add more length to get a better gift from Santa next year!")
    else:
        st.success("🎁 NICE LIST! MERRY CHRISTMAS!")
        st.write("**Verdict:** Ho Ho Holy Security! This password is a fortress. It would take centuries to crack. Stay frosty and keep those accounts safe!")

    # 4. The Stats (For the Geeks)
    with st.expander("See the nerdy security math"):
        st.write(f"**Entropy:** {entropy:.2f} bits")
        if seconds_to_crack < 60:
            st.write(f"**Estimated Crack Time:** {seconds_to_crack:.2f} seconds")
        else:
            years = seconds_to_crack / 31536000
            st.write(f"**Estimated Crack Time:** {years:,.0f} years")
else:
    st.info("Check some boxes to let Santa check your work!")
