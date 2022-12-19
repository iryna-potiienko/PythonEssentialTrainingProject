from termcolor import *

# Note: If you are on Windows,
# you may need to use Colorama (https://pypi.org/project/colorama/)

import colorama
colorama.init()

print(colored('~~~RAINBOW~~~', 'red'))
print(colored('~~~RAINBOW~~~', 'yellow'))
print(colored('~~~RAINBOW~~~', 'green'))
print(colored('~~~RAINBOW~~~', 'cyan'))
print(colored('~~~RAINBOW~~~', 'blue'))
print(colored('~~~RAINBOW~~~', 'magenta'))

cprint("Hello, World!", "green", "on_cyan")
print(colored("My colored string", "yellow", "on_red", ["bold", "dark", "concealed"]))
cprint("Hi Ukraine", "yellow", "on_blue", ["bold", "blink"])
