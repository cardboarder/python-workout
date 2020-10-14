# Write function myxml that produces a tag name, taking optional content and name-value pairs 

def myxml(tag, content='', **kwargs):

    #unpack keyword-value arguments
    attributes = ' '.join([f'{key}={value}' for key, value in kwargs.items()])

    return f'<{tag} {attributes}>{content}</{tag}>'



# Below are some illustrative functions to help with understanding *args vs **kwargs
def print_args(*args):
    print( args )

def print_kwargs(**kwargs):
    print( kwargs )


if __name__ == "__main__":
    print_args(1, 2, 0, 'b', 'monkeywrench')
    print_kwargs(a=1, b=2, c=0)

    print(myxml('p', 'fish', a=1, b=2, c='elephant'))
