### Script author:
### Script created on: 
### Script last modified on:

####################################################################################################################
                                            ### Import libraries ###
####################################################################################################################

import argparse

####################################################################################################################
                                        ### Function Definition Area ###
####################################################################################################################

""" This function will allow us to take variables as input
"""
def getArguments():
    # Set up the command line parser
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=""
    )

    # Indicate where the zipped file is located
    parser.add_argument(
        "path",
        help="Indicate the full path to the zipped CSV file."
    )
    
   
    
    # Verbosity flag
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Run the program in verbose mode.")

    # Parse the command line arguements.
    options = parser.parse_args()
    return options


####################################################################################################################
                                            ### Main Function Area ###
####################################################################################################################

if __name__ == "__main__":
    
    # Get arguments
    options = getArguments()
    path_to_csv = options.path

    
    # Your code here 