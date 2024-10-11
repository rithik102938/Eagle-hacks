import streamlit as st
import random

# Game title
st.title("Number Guessing Game")

# Game parameters
max_number = st.slider("Select the maximum number:", 1, 100, 50)
secret_number = random.randint(1, max_number)

# User input
guess = st.number_input("Enter your guess:", min_value=1, max_value=max_number)

# Game logic
if st.button("Submit Guess"):
    if guess < secret_number:
        st.write("Too low! Try again.")
    elif guess > secret_number:
        st.write("Too high! Try again.")
    else:
        st.write("Congratulations! You've guessed the number!")
        st.balloons()  # Show balloons when guessed correctly

# Option to reset the game
if st.button("Restart Game"):
    secret_number = random.randint(1, max_number)
    # st.experimental_rerun()
