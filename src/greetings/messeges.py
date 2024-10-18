"""Functions that can be used to output custom greeting messages."""

def hi(name: str, message: str) -> str:
    """Returns a message in the form 'Hi {name}! {message}'"""
    return f"Hi {name.title()}! {message}"
    

def welcome(name: str, message: str) -> str:
    """Returns a message in the form 'Welcome {name}! {message}'"""
    return f"Welcome {name.title()}! {message}"

def hello(name: str, message: str) -> str: 
    """Returns a message in the form 'Hello {name}! {message}'"""
    return f"Hello {name.title()}! {message}"