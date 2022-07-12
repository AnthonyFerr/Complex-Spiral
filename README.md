# Complex-Spiral
Produces a graph given a complex number multiplied by a complex number over several iterations, producing a spiral. README for help resolving setup.

Must clone the cartesius library. Then move the complex-spiral.py file to the /src/ folder of the package. 
> $ git clone https://github.com/tkrajina/cartesius

Then clone the PIL/Pillow library,
> $ git clone https://github.com/python-pillow/Pillow

main.py of cartesius will have issues accessing PIL (no module named PIL.Image, etc)
You may need to use sys.path.append('[PATH of PIL modules') to resolve this.
A number of other errors I'm too lazy to fix show up due to installation, just go around and remove wherever cartesius tries to import a module by doing
> from .[path]
