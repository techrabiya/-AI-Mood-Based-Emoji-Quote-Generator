import streamlit as st

st.title("🌟 AI Mood-Based Emoji & Quote Generator")
st.write("Tell me how you're feeling right now, and let AI brighten your day!")

mood = st.selectbox("How is your mood today?", ["Happy", "Sad", "Motivated", "Stressed", "Excited"])

if st.button("Generate Magic"):
    if mood == "Happy":
        st.success("🎉 Yay! Keep shining bright!")
        st.markdown("### *'Happiness is not something ready-made. It comes from your own actions.'*")
    elif mood == "Sad":
        st.info("🌧️ Tough times never last, but tough people do. You've got this!")
        st.markdown("### *'Every storm runs out of rain.'*")
    elif mood == "Motivated":
        st.fireworks()
        st.success("🔥 You're unstoppable today! Go crush your goals!")
        st.markdown("### *'The secret of getting ahead is getting started.'*")
    elif mood == "Stressed":
        st.warning("🧘 Take a deep breath. Inhale peace, exhale stress.")
        st.markdown("### *'You don't have to see the whole staircase, just take the first step.'*")
    elif mood == "Excited":
        st.balloons()
        st.success("⚡ Amazing! Channel that energy into something extraordinary!")
        st.markdown("### *'Energy flows where attention goes.'*")
