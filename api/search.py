import google.generativeai as genai

def get_google_search_tool():
    """
    Returns the Google Search tool configuration for Gemini.
    Handles different ways of instantiating the tool based on available protobuf classes.
    """
    try:
        gs_tool = genai.protos.Tool.GoogleSearch()
        tool_config = genai.protos.Tool(google_search=gs_tool)
        return tool_config
    except AttributeError:
        tool_config = genai.protos.Tool(google_search={})
        return tool_config
