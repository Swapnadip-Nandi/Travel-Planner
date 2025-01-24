import streamlit as st
from datetime import datetime
import random


st.set_page_config( page_title="Travel Itinerary Planner", page_icon="🌍")
def add_background():
    background_images = [
        'https://source.unsplash.com/1920x1080/?travel,nature',
        'https://source.unsplash.com/1920x1080/?beach,sunset',
        'https://source.unsplash.com/1920x1080/?mountains,adventure',
        'https://source.unsplash.com/1920x1080/?city,landscape',
        'https://source.unsplash.com/1920x1080/?forest,waterfall'
    ]
    selected_image = random.choice(background_images)
    background_style = f"""
    <style>
    .stApp {{
        background-image: url('{selected_image}');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    .reportview-container .main .block-container {{
        padding: 2rem;  /* Increased padding for more spacing */
        max-width: 95%;  /* Allow wider content area */
        margin: auto;
    }}
    </style>
    """
    st.markdown(background_style, unsafe_allow_html=True)

def collect_user_inputs():
    st.title("🌍 Personalized Travel Itinerary Planner")
    st.markdown("Plan your perfect trip by providing some basic details below:")

    with st.container():
        destination = st.text_input("📍 Where are you traveling to?", "Paris")
        trip_duration = st.slider("🗓️ How many days is your trip?", min_value=1, max_value=30, value=5)
        budget = st.selectbox("💰 What is your budget?", ["Low", "Moderate", "Luxury"])
        purpose = st.text_area("🎯 What's the purpose of your trip?", "Leisure")

    preferences = st.multiselect("✨ What are your preferences?", 
                                  ["Famous landmarks", "Museums", "Hidden gems", "Scenic walks", "Food experiences", "Relaxation"],
                                  default=["Famous landmarks", "Food experiences"])

    dietary_preferences = st.selectbox("🍽️ Any dietary preferences?", ["None", "Vegetarian", "Vegan", "Gluten-free"])
    walking_tolerance = st.slider("🚶 How much walking are you comfortable with daily (in km)?", 1, 20, 10)
    accommodation = st.selectbox("🏨 Preferred accommodation type:", ["Budget", "Moderate", "Luxury", "Central Location"])

    return {
        "destination": destination,
        "trip_duration": trip_duration,
        "budget": budget,
        "purpose": purpose,
        "preferences": preferences,
        "dietary_preferences": dietary_preferences,
        "walking_tolerance": walking_tolerance,
        "accommodation": accommodation
    }

def refine_inputs(user_inputs):
    if user_inputs['budget'] == "Moderate" and "Hidden gems" not in user_inputs['preferences']:
        user_inputs['preferences'].append("Hidden gems")
    if user_inputs['purpose'].lower().startswith("adventure") and "Scenic walks" not in user_inputs['preferences']:
        user_inputs['preferences'].append("Scenic walks")
    return user_inputs

def generate_itinerary(user_inputs):
    destination = user_inputs['destination']
    duration = user_inputs['trip_duration']
    preferences = user_inputs['preferences']

    itinerary = []
    for day in range(1, duration + 1):
        activities = []
        if "Famous landmarks" in preferences:
            activities.append(f"🏰 Visit a top landmark in {destination}.")
        if "Museums" in preferences:
            activities.append(f"🖼️ Spend time at a popular museum in {destination}.")
        if "Hidden gems" in preferences:
            activities.append(f"🔍 Explore a hidden gem or less-known spot in {destination}.")
        if "Scenic walks" in preferences:
            activities.append(f"🌳 Take a scenic walk around a famous park or area in {destination}.")
        if "Food experiences" in preferences:
            activities.append(f"🍴 Enjoy a meal at a local {user_inputs['dietary_preferences']} friendly restaurant.")
        if "Relaxation" in preferences:
            activities.append(f"🛌 Spend a relaxing evening at your accommodation.")

        itinerary.append(f"### Day {day}\n" + "\n".join(activities))

    return itinerary

def main():
    add_background()
    user_inputs = collect_user_inputs()
    user_inputs = refine_inputs(user_inputs)

    if st.button("🧳 Generate Itinerary"):
        itinerary = generate_itinerary(user_inputs)
        st.header("Your Personalized Itinerary")
        for day_plan in itinerary:
            with st.expander(day_plan.split("\n")[0]): 
                st.markdown(day_plan)

if __name__ == "__main__":
    main()
