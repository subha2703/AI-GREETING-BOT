import streamlit as st
from sms_sender import send_sms
from telegram_bot import send_telegram_message
from greetings import greetings

st.set_page_config(page_title="Cube AI Greeting Bot", layout="centered")

st.title("🤖 Cube AI Greeting Bot")
st.write("Select a greeting message to send via SMS and Telegram.")

greeting_type = st.selectbox("Choose a greeting type:", list(greetings.keys()))
custom_message = st.text_area("Or write your own custom message:", "")

phone_number = st.text_input("Enter client's phone number:")
telegram_user_id = st.text_input("Enter client's Telegram user ID:")

if st.button("Send Greeting"):
    message = custom_message.strip() if custom_message else greetings[greeting_type]
    if not phone_number or not telegram_user_id:
        st.error("Phone number and Telegram user ID are required.")
    else:
        sms_status = send_sms(phone_number, message)
        tg_status = send_telegram_message(telegram_user_id, message)
        st.success("Greeting sent successfully!" if sms_status and tg_status else "Failed to send message.")