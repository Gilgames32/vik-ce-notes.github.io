import re

def define_env(env):
    pass

def add_quotes(text : str) -> str:
    if not text:
        return ''
    
    # in case the text is already quoted
    text = text.strip().removeprefix('"').removesuffix('"').strip()
    return f'"{text}"'

def compatible_admonition(text : str) -> str:
    '''
    Cause Markdown Preview Enhanced parses the admonition
    titles without the quotes, this function adds them.
    '''

    pattern = r'(!!!|\?\?\?\+?)\s*(note|abstract|info|tip|success|question|warning|faliure|danger|bug|example|quote)[^\S\r\n](.*)?'
    return re.sub(pattern, lambda m: f'{m.group(1)} {m.group(2)} {add_quotes(m.group(3))}', text, flags=re.IGNORECASE)

def on_pre_page_macros(env):
    '''
    This function is called before the page macros are processed.
    '''
    text = compatible_admonition(env.markdown)
    
    # * ADD YOUR PREPROCESSING HERE

    env.markdown = text
