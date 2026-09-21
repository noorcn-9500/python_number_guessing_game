import random
import streamlit as st

# ---------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------

st.set_page_config(
    page_title="Guess the Number",
    page_icon="🎯",
    layout="centered"
)

st.title("🎯 Guess the Number")
st.write("Can you guess the number I'm thinking of?")
st.caption("The secret number is between 1 and 100.")


# ---------------------------------------
# INITIAL SESSION STATE
# ---------------------------------------

if "game_started" not in st.session_state:
    st.session_state.game_started = False

if "random_number" not in st.session_state:
    st.session_state.random_number = None

if "attempt" not in st.session_state:
    st.session_state.attempt = 1

if "max_attempt" not in st.session_state:
    st.session_state.max_attempt = 7

if "your_guesses" not in st.session_state:
    st.session_state.your_guesses = []

if "game_over" not in st.session_state:
    st.session_state.game_over = False

if "won" not in st.session_state:
    st.session_state.won = False

if "message" not in st.session_state:
    st.session_state.message = ""


# ---------------------------------------
# START GAME
# ---------------------------------------

if not st.session_state.game_started:

    st.subheader("🎮 Start a New Game")

    attempts = st.number_input(
        "Challenge the Number of Attempts:",
        min_value=1,
        max_value=20,
        value=7,
        step=1
    )

    if st.button(
        "🚀 Start Game",
        use_container_width=True,
        type="primary"
    ):
        st.session_state.random_number = random.randint(1, 100)
        st.session_state.max_attempt = int(attempts)
        st.session_state.attempt = 1
        st.session_state.your_guesses = []
        st.session_state.game_over = False
        st.session_state.won = False
        st.session_state.message = ""
        st.session_state.game_started = True

        st.rerun()


# ---------------------------------------
# GAME
# ---------------------------------------

else:

    number = st.session_state.random_number
    attempt = st.session_state.attempt
    max_attempt = st.session_state.max_attempt

    # Progress
    st.write(
        f"### Attempt {attempt} / {max_attempt}"
    )

    progress = (attempt - 1) / max_attempt
    st.progress(progress)

    # Previous guesses
    if st.session_state.your_guesses:
        guesses = " → ".join(
            str(x) for x in st.session_state.your_guesses
        )

        st.write("**Your Guesses:**")
        st.info(guesses)

    # ---------------------------------------
    # HINT
    # ---------------------------------------

    # Based on your original game's hint logic
    if attempt >= 4 and not st.session_state.game_over:

        if number % 2 == 0:
            st.info("💡 Hint: It is an EVEN number.")
        else:
            st.info("💡 Hint: It is an ODD number.")

    # ---------------------------------------
    # ACTIVE GAME
    # ---------------------------------------

    if not st.session_state.game_over:

        guessed = st.number_input(
            "Enter your guess:",
            min_value=1,
            max_value=100,
            value=50,
            step=1,
            key=f"guess_{attempt}"
        )

        if st.button(
            "🎯 Submit Guess",
            use_container_width=True,
            type="primary"
        ):

            guessed = int(guessed)

            st.session_state.your_guesses.append(guessed)

            # Your original lambda logic
            check_guess = lambda x, y: (
                "Correct"
                if x == y
                else ("Less" if x < y else "High")
            )

            result = check_guess(
                guessed,
                st.session_state.random_number
            )

            # CORRECT
            if result == "Correct":

                st.session_state.won = True
                st.session_state.game_over = True

                st.session_state.message = (
                    f"Congratulations! You found "
                    f"{st.session_state.random_number} "
                    f"in {st.session_state.attempt} attempt(s)."
                )

            # LAST ATTEMPT - WRONG
            elif st.session_state.attempt >= st.session_state.max_attempt:

                st.session_state.game_over = True
                st.session_state.won = False

                st.session_state.message = (
                    "Game Over. Better luck next time!"
                )

            # GUESS IS LOWER
            elif result == "Less":

                st.session_state.message = (
                    "⬆️ Guess Higher Number!"
                )

                st.session_state.attempt += 1

            # GUESS IS HIGHER
            elif result == "High":

                st.session_state.message = (
                    "⬇️ Guess Lower Number!"
                )

                st.session_state.attempt += 1

            st.rerun()


        # ---------------------------------------
        # DISPLAY FEEDBACK
        # ---------------------------------------

        if st.session_state.message:

            if "Higher" in st.session_state.message:
                st.warning(st.session_state.message)

            elif "Lower" in st.session_state.message:
                st.warning(st.session_state.message)


    # ---------------------------------------
    # GAME FINISHED
    # ---------------------------------------

    if st.session_state.game_over:

        if st.session_state.won:

            st.success(
                f"🎉 {st.session_state.message}"
            )

            st.balloons()

        else:

            st.error(
                f"😢 {st.session_state.message}"
            )

            st.write(
                f"### 🔢 The Number Was: "
                f"{st.session_state.random_number}"
            )

        st.write("### Your Guesses")

        guesses = " → ".join(
            str(x) for x in st.session_state.your_guesses
        )

        st.info(guesses)

        # PLAY AGAIN
        if st.button(
            "🔄 Play Again",
            use_container_width=True
        ):

            st.session_state.game_started = False
            st.session_state.random_number = None
            st.session_state.attempt = 1
            st.session_state.your_guesses = []
            st.session_state.game_over = False
            st.session_state.won = False
            st.session_state.message = ""

            st.rerun()