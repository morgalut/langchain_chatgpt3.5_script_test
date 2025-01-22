import os
import openai
from langchain.prompts import PromptTemplate

os.environ["LANGSMITH_TRACING"] = "true"
os.environ["LANGSMITH_ENDPOINT"] = "https://api.smith.langchain.com"
os.environ["LANGSMITH_API_KEY"] = "your_langsmith_api_key_here"
os.environ["LANGSMITH_PROJECT"] = "your_langsmith_project_id_here"
os.environ["OPENAI_API_KEY"] = "your_openai_api_key_here"

# Correctly set the API key from the environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize the prompt template
prompt_template = PromptTemplate(template="py code hello word")

# Define a class for handling the interactions
class LangChain:
    def __init__(self, prompt_template):
        self.prompt_template = prompt_template

    def run(self, input_text):
        # Format the input text with the template
        formatted_prompt = self.prompt_template.template.format(input_text=input_text)
        # Make an API call to OpenAI to get the response using chat completions
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo-0125",  # Use the specified model for chat completions
                messages=[{"role": "user", "content": formatted_prompt}],
                max_tokens=150
            )
            return response['choices'][0]['message']['content'].strip()
        except Exception as e:
            return str(e)

# Create the LangChain object using the correct setup
lang_chain = LangChain(prompt_template)

# Define a function to use the AI
def use_ai(input_text):
    response = lang_chain.run(input_text=input_text)
    return response

# Example usage
input_text = "py code hello word"
result = use_ai(input_text)
print(result)
