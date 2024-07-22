import streamlit as st
import openai

# Streamlit application
def main():
    st.title("Indoor Tennis Courts Finder")

    # API Connection
    openai_api_key = st.sidebar.text_input("Enter your OpenAI API key")
    if openai_api_key:
        openai.api_key = openai_api_key

        # User input
        location = st.text_input("Enter your location")

        if st.button("Find Courts"):
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": f"find indoor tennis courts near {location}"},
                ],
            )
            message_content = response["choices"][0]["message"]["content"].strip()
            st.write(message_content)
    else:
        st.warning("Please enter your OpenAI API key.")

if __name__ == "__main__":
    main()