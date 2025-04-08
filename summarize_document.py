import openai

def summarize_text(content: str, prompt_template: str) -> str:
    prompt = prompt_template.replace("{{ document_text }}", content)
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that summarizes documents."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        raise RuntimeError(f"Error generating summary: {e}")
