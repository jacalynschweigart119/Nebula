
#### main.py

```python
#!/usr/bin/env python3
import random

facts = [
    "The Milky Way galaxy contains between 100 and 400 billion stars.",
    "A day on Venus is longer than its year.",
    "Neutron stars can spin up to 600 times per second.",
    "There are more trees on Earth than stars in the Milky Way."
]

def get_random_fact():
    return random.choice(facts)

def main():
    print("Welcome to the Nebula Project!")
    print("Here's an astronomy fact for you:")
    print(get_random_fact())

if __name__ == "__main__":
    main()
