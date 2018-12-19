#!/usr/bin/python3
########################################################################################################################
#                                           Stratoscale - Monitoring Script                                            #
# -------------------------------------------------------------------------------------------------------------------- #
#                                                                                                                      #
# INTRODUCTION:                                                                                                        #
#   This script is part of a toolset which is being developed to help monitor and maintain a customer's                #
#   Stratoscale environment. It will monitor multiple components in the Stratoscale stack, which are otherwise         #
#   not monitored.                                                                                                     #
#                                                                                                                      #
# -------------------------------------------------------------------------------------------------------------------- #
#                                                                                                                      #
# MODULE DETAILS:                                                                                                      #
#   This module is for TODO                                                                                            #
#                                                                                                                      #
# -------------------------------------------------------------------------------------------------------------------- #
#                                                                                                                      #
# CHANGELOG                                                                                                            #
# v0.1 - 18 December 2018 (Richard Raymond)                                                                            #
#   - Template                                                                                                         #
# v0.2 - 18 December 2018 (Richard Raymond)                                                                            #
#   - YAML Config file handling.                                                                                       #
#   - Added deeper error message customization (define error types in config.yaml)                                     #
# v0.3 - 19 December 2018 (Richard Raymond)                                                                            #
#   - Added better directory & error handling (directories are defined in the config.yml                               #
#                                                                                                                      #
########################################################################################################################
import sys
import yaml

# PARAMETERS
# 1 - Script name, 2 - Root path of calling script, 3 - Report filename

# CONFIG VARIABLES
rootpath = sys.argv[2]
config = yaml.load(open( rootpath + '/config.yml', 'r'))                    # Pull in config information from YML file.
testdirectory = rootpath + config['framework']['directory']['test']         # Generate directory string for test
reportdirectory = rootpath + config['framework']['directory']['report']     # Generate directory string for reports
workingdirectory = rootpath + config['framework']['directory']['working']   # Generate directory string for working dir
scriptdirectory = rootpath + config['framework']['directory']['script']     # Generate directory string for sub scripts

# SCRIPT VARIABLES
result = 4                                                                  # Initialize OK/NOK marker
error_message = "*UPDATE ME*"                                               # Error message to provide overview
error_data = "*UPDATE ME*"                                                  # Full error contents
# ----------------------------------------------------------------------------------------------------------------------
# TEST SCRIPT DATA GOES HERE










# ----------------------------------------------------------------------------------------------------------------------
# UPDATE REPORT FILE
reportfile = open(reportdirectory + sys.argv[3] + '.txt', "a")              # Open the current report file
reportfile.write('TEST:         ' + sys.argv[1] + '\n')                     # Open test section in report file
reportfile.write('RESULT:       ' + config['errortypes'][result])           # Add test status to report
if result != 0:                                                             # Check if test wasn't successful
    errorfilename = sys.argv[3] + "_" + sys.argv[1]                         # Create a error_reportfile
    errorfile = open(reportdirectory + errorfilename + '.txt', "w+")        # Create error report file
    errorfile.write(error_data)                                             # Write error data to error file
    errorfile.close()                                                       # Close error file
    reportfile.write(" : " + error_message + '\n')                          # Add error message to report
    reportfile.write(" Please look at [" + errorfilename + ".txt] for further details.")
reportfile.write('\n' + config['formatting']['linebreak'] + '\n')           # Add line break to report file, after test
reportfile.close()                                                          # Close report file
