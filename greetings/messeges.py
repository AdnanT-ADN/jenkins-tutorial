"""Functions that can be used to output custom greeting messages."""

def hi(name: str, message: str) -> None:
    """Outputs a message in the form 'Hi {name}! {message}'"""
    print(
        f"Hi {name.title()}! {message}"
    )

def welcome(name: str, message: str) -> None:
    """Outputs a message in the form 'Welcome {name}! {message}'"""
    print(
        f"Welcome {name.title()}! {message}"
    )

def hello(name: str, message: str) -> None: 
    """Outputs a message in the form 'Hello {name}! {message}'"""
    print(
        f"Hello {name.title()}! {message}"
    )