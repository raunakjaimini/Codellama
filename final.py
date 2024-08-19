import requests
import json
import gradio as gr

# Replace with your actual API endpoint
url = "http://localhost:11434/api/generate"

headers = {
    'Content-Type': 'application/json'
}

history = []

def generate_response(prompt):
    history.append(prompt)
    final_prompt = "\n".join(history)

    data = {
        "model": "codeguru",
        "prompt": final_prompt,
        "stream": False
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        response_data = response.json()
        actual_response = response_data.get('response')
        return actual_response
    else:
        return f"Error: {response.status_code} - {response.text}"

# Create a Gradio interface with enhanced styling
interface = gr.Interface(
    fn=generate_response,
    inputs=gr.Textbox(
        lines=4, 
        placeholder="Enter your prompt here...",
        label="Prompt",
        elem_id="prompt-box"
    ),
    outputs="text",
    title="CodeGuru..Your Trusted Tutor",
    description="Enter your prompts to interact with the CodeGuru model. Get responses based on your input.",
    theme="default",  # Use the default theme or you can customize it further
    css="""
        #prompt-box {
            border-radius: 8px;
            border: 2px solid #4a90e2;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
        .input-container {
            padding: 20px;
        }
        .output-container {
            padding: 20px;
            background-color: #f9f9f9;
            border-radius: 8px;
            border: 1px solid #ddd;
        }
    """
)

# Launch the interface
interface.launch()
