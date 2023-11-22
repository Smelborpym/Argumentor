import streamlit as st

def main():

    if 'show_analysis_result' not in st.session_state:
        st.session_state.show_analysis_result = False

    if 'show_stance_input' not in st.session_state:
        st.session_state.show_stance_input = False

    if 'show_debate_chat' not in st.session_state:
        st.session_state.show_debate_chat = False

    st.title("🎙️🤖 Welcome to Argumentor!")
    st.write("I am your personal debate assistant. I"
             " help you formulate arguments, prepare counterarguments, "
             "check facts, and identify logical fallacies.")

    with st.form(key='context_form'):
        st.subheader("Describe the context of your debate")
        st.markdown('''💡The debate centers on the morality, effectiveness, and legal implications of capital punishment. It includes arguments about justice, deterrence, and human rights.''')
        st.markdown('''💡Our debate is focusing on the balance between the need for gun control laws for public safety and the right to bear arms.''')
        context = st.text_area("Context", max_chars=350, label_visibility="hidden")
        submitted_context = st.form_submit_button("Done")
    
    if submitted_context:
        if context:
                    with st.spinner('Brewing...'):
                        import time
                        time.sleep(10)
                    st.session_state.show_analysis_result = True
        else:
            st.error("Please enter a description of the context of your debate.")


    if st.session_state.show_analysis_result:
        with st.form(key='keywords_form'):
            st.write("Check any relevant keywords")
            # Example list of keywords from context analysis
            keywords = ["Assisted Suicide", "Right to Die", "Ethics", "Paliative Care", "Regulation", "Crime"]

            if 'selected_keywords' not in st.session_state:
                st.session_state.selected_keywords = {keyword: False for keyword in keywords}

            select_all = st.checkbox("Select All")

            if select_all:
                st.session_state.selected_keywords = {keyword: True for keyword in keywords}
            elif not any(st.session_state.selected_keywords.values()):
                st.session_state.selected_keywords = {keyword: False for keyword in keywords}

            for keyword in keywords:
                st.session_state.selected_keywords[keyword] = st.checkbox(keyword, value=st.session_state.selected_keywords[keyword], key=keyword)

            submitted_keywords = st.form_submit_button("Confirm")

        if submitted_keywords:
            # Filter and process only the selected keywords
            selected_keywords_list = [keyword for keyword, is_selected in st.session_state.selected_keywords.items() if is_selected]
            # Use `selected_keywords_list` for further processing
            st.session_state.show_stance_input = True


    if st.session_state.show_stance_input:
        with st.form(key='stance_form'):
            st.subheader("Describe your stance in this debate")
            st.markdown('''💡I believe the current system of capital punishment is flawed and requires significant reform. My stance is that while the death penalty can be justified in some cases, there needs to be stricter safeguards to prevent orange[wrongful executions, biases, and ensure a fair legal process.''')
            st.markdown('''💡In my opinion, the current approach to gun control is inadequate. In fact, I don't think people should be allowed to bear arms designed to kill poeple. Public safety must be the priority. Therefore, there should be more rigorous regulations on high-capacity weapons to justify their ownership and prevent their misuse.''')
            stance = st.text_area("Opinion", max_chars=350, label_visibility="hidden")
            submitted_stance = st.form_submit_button("Done")

        if submitted_stance:
            if stance:
                st.success("Got it!")
                st.session_state.show_debate_chat = True
            else:
                st.error("Please enter a description of your stance in this debate.")

    if st.session_state.show_debate_chat:
        st.subheader("🚀 Let's Go!")
        st.write("Here's a synthesis of where we stand in this debate. Based on this, I'll draft a few arguments.")
        # Implement the logic for the engaging debate section here

if __name__ == "__main__":
    main()