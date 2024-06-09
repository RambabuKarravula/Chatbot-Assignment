import streamlit as st
from transformers import BertForMaskedLM, BertTokenizer

# Load the fine-tuned model
model = BertForMaskedLM.from_pretrained('./finetuned_model')
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

# Function to generate a response
def generate_response(input_text):
    input_ids = tokenizer.encode(input_text, return_tensors='pt')
    output = model.generate(input_ids, max_length=100, do_sample=True, top_k=50, top_p=0.95, num_return_sequences=1)
    response = tokenizer.decode(output[0], skip_special_tokens=True)
    return response

# Streamlit app
def app():
    st.title("Chatbot")
    st.write("Welcome to the chatbot! Ask me anything related to the knowledge domain.")

    user_input = st.text_input("You: ", key="input")
    if user_input:
        response = generate_response(user_input)
        st.write(f"Chatbot: {response}")

if __name__ == "__main__":
    app()