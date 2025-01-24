import os

def get_openai_api_key():
    """
    Retrieves the OpenAI API key from an environment variable or a secure source.
    """
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY is not set in the environment variables.")
    return api_key

def get_serper_api_key():
    """
    Retrieves the Serper API key from an environment variable or a secure source.
    """
    api_key = os.getenv("SERPER_API_KEY")
    if not api_key:
        raise ValueError("SERPER_API_KEY is not set in the environment variables.")
    return api_key
