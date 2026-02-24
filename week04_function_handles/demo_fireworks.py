"""Example of function handles."""


def red_firework():
    return "red"

def blue_firework():
    return "blue"

def light_firework(func):
    color = func()  # invoke the function to get color
    return f"BOOOOOOM! What a beautiful {color} firework!"

if __name__ == '__main__':
    # example from slide
    print(red_firework)

