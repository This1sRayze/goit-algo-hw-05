import re

def generator_numbers(text: str):
    for match in re.findall(r'\s(-?\d+\.\d+)\s', f' {text} '):
        yield float(match)

def sum_profit(text: str) -> float:
    return sum(generator_numbers(text))