import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.prompts.chat import ChatPromptTemplate
import os

# OpenAIのAPIキーを環境変数から取得
chat = ChatOpenAI(api_key=openai_api_key, model="gpt-3.5-turbo")

prompt = ChatPromptTemplate.from_template(
    "Translate this text from {source_lang} to {target_lang}: {text}"
)

st.title("超シンプル翻訳アプリ")

source_lang = st.selectbox("翻訳元の言語", ["Japanese", "English", "French", "Spanish"])
target_lang = st.selectbox("翻訳先の言語", ["Japanese", "English", "French", "Spanish"])
text = st.text_area("翻訳したい文章を入力してください")

if st.button("翻訳する"):
    prompt_message = prompt.format_prompt(
        source_lang=source_lang,
        target_lang=target_lang,
        text=text
    ).to_messages()
    response = chat(prompt_message)
    st.write("翻訳結果:")
    st.success(response.content)
