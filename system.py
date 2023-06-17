# CHAPTER 8 - IMPORTING LIBRARIES 
# INSPECTING PYTHON - page 100/101

import sys , keyword

# display the Python version
print('Python Version:' , sys.version)

# display the location on local system of the Python interpreter
print('Python Interpreter Location:' , sys.executable)

# display a list of all the directories whete the Python interpreter looks for module files 
print('Python Module Search Path:')
for folder in sys.path :
    print(folder)

# Display a list of all the python keywords - keyword module already holds a list of these in the kwlist attribute
print('Python Keywords:')
for word in keyword.kwlist :
    print(word)


