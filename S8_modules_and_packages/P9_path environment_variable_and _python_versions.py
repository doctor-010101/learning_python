# ### Environment Variable PATH
# The PATH environment variable is an operating system variable that specifies a list of directories where the system should look for executable files. When you enter a command in the terminal, the system searches through the directories listed in the PATH variable in order to find the executable file corresponding to that command. If the executable file is found in one of these directories, the system runs it.

# Example:
# Let's say you enter the python command in the terminal. The operating system will check each directory listed in the PATH variable to see if a file named python exists there. If it finds such a file, that file will be executed.

# ### Switching Python Versions from the Terminal
# If you have multiple versions of Python installed on your system and you want to use a specific version, there are several ways to do this:

# 1. Using the Full Path Command: You can specify the full path to the desired Python version to execute it. For example:
  
#    /usr/bin/python3.8
   
# 2. **Modifying the PATH Variable:** By placing the path of the desired Python version at the beginning of the PATH variable, you can set that version as the default.
  
#    export PATH="/usr/local/bin/python3.8:$PATH"
#    Using Python Version Management Tools:s:**
#    - **pyenv:** This is one of the best tools for managing multiple Python versions on a system. It allows you to set a default Python version or specify a different version for a particular project.
    
#      pyenv install 3.8.0
#      pyenv global 3.8.0
     
#    - **Using alias:** You can define an alias for different Python versions. For example:
    
#      alias python=python3.8
     
# With these methods, you can easily switch between different Python versions and use the version you need.