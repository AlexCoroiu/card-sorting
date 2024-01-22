# Card Sorting

## INSTALLATION for the program:

Make sure you have the following packages installed on your computer in order to be able to use this program. 
Links are provided from where you can download the needed packages. 

- Python 3.8.3 and its standard libraries: https://www.python.org/downloads/
- Pygame: https://www.pygame.org/wiki/GettingStarted
- Pandas: https://pandas.pydata.org/

The anaconda package contains all of the above mentioned items. 
You can download anaconda from: https://www.anaconda.com/products/individual

You need all the main files from the .zip of the program. 
This category includes: 
- card_sorting.py
- data_manager.py
- event_handler.py
- painter.py
- program_variables.py
- UI_objects.py
- instructions.txt

## RUNNING the program:

In addition to the main python files listed above, you need an input file to run the program. 
This file needs to have a csv format and has to be named cards_file.csv. 
This file should contain the cards you want to sort. Each card should be on a new raw.
An example cards_file.csv is provided in the .zip.

To run the program you need to run the card_sorting.py file.
Open your prefered IDE and run it from there, or run it from the command line:

- open the command line in the source code directory
- run the following command: "python card_sorting.py"

Make sure that the run enviornment you use has the correct installation packages needed for this program. 

## Addiitonal notes:

The .zip of the program also example output files: matrix_file.csv and results_file.txt.
These files get updated after you run and complete a card sorting experiment.

You can test the data_manager.py module by using the test files in the zip.

- test_cards_file.csv
- test_data_manager.py

To run the test you need to run the test_data_manager.py. 
Run the test through your IDE or the command line ("python test_data_manager.py")
The test output is saved in test_matrix_file.csv and test_results_file.txt. 
This test checks the reading and writing to files of the tree data structure used in the program.

Lastly, the .zip also contains the design_document.pdf which explains the program in more detail.



