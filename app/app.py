import streamlit as st

def main():
    st.title("🎙️🤖 Welcome to Argumentor!")

    st.write("I am your personal debate assistant. I will empower your debates "
             "by helping you formulate arguments, prepare counterarguments, "
             "check facts, and identify logical fallacies.")

    st.subheader("Describe the context of your debate")

    # Text input for debate context with 350 characters limit
    context = st.text_area("💡The debate centers on the morality, effectiveness, and legal implications of capital punishment. "
                           "It includes arguments about justice, deterrence, and human rights", 
                           max_chars=350)

    if st.button("Ingest Context"):
        if context:
            # Placeholder for debate context
            st.success("Interesting topic!")
            # In the future, this will call the logic for context analysis
            # and display the results
        else:
            st.error("Please enter a description of the context of your debate.")
    
    st.subheader("Describe your stance in this debate")

    # Text input for user stance with 350 characters limit
    stance = st.text_area("💡I believe the current system of capital punishment is flawed and requires significant reform. "
                          "My stance is that while the death penalty can be justified in some cases, "
                          "there needs to be stricter safeguards to prevent wrongful executions, biases, and ensure a fair legal process.",
                          max_chars=350)

    if st.button("Ingest Stance"):
        if stance:
            # Placeholder for user stance
            st.success("Got it!")
            # In the future, this will call the logic for stance analysis
            # and display the results
        else:
            st.error("Please enter a description of your position in this debate.")

if __name__ == "__main__":
    main()
