#Importing a Module from Another Directory
import sys
# Add the 'mymodule' directory to sys.path
sys.path.insert(0, './modules/files')



from files import module #from folder import file
print(module.countdown(int(input('enter a number: '))))
