from transformers import AutoTokenizer, AutoModelForCausalLM

# Load the model and tokenizer globally
model_name = "mukulvyas99/LawChatTinyLlama2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

def get_model():
    return model

def get_tokenizer():
    return tokenizer

