# Import hello module (hello.py file)
import hello

# Put main code that runs into a function.
def main():
    hello.world()   # Call world function within module hello.
    
    # Alternative way to call the function
    # from hello import world
    # world()

    # Print variable
    print(hello.love)

    # Call class Athlete within hello module. 
    roger = hello.Athlete("Roger","tennis")

    # Call function within the class Athlete.
    roger.about_the_athlete()

# The if statement determines how this module (main_program) was called: 
#  directly from the command line OR indirectly through import in another file/module. 
if __name__ == "__main__":  # if statement true if called directly. False if imported.
    print(__name__)
    main()
