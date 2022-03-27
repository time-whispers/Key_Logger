# Python Keylogger

Keyloggers are programs that capture your key strokes. They can be used to keep logs of everything you press on the keyboard but on the flip side it can be used for malicious purposes as well.

The keylogger that I've made is a basic keylogger with not much functionality as the ones available in market today. It captures your keystrokes and saves them in a file "keylogger.txt".

## Usage Instructions :

- Download the contents of The Repository as a Zip File or clone the Repository.
- Install Python in your Machine 
- Install the python packages mentioned inside the requirments.txt file by the following command in your terminal:

    ```python3
    >>> pip install -r requirements.txt #for windows
    >>> pip3 install -r requirements.txt #for macos and linux
    ```
 
- Run the key_logger.py file by running <i>python key_logger.py</i> or <i>python3 key_logger.py</i> on it.
- The Keylogger will now gather all of the responses from the keyboard and store them in the keylogger.txt file, completing the majority of the work. 
- Now press the 'esc' key to stop the keylogger from running, and the keystrokes entered will be saved in a file with that date and time stamp till then.
- In addition, the keylogger.txt file will be emailed to the email address specified in the code.
- We can also run this keylogger indefinitely, even if the user has rebooted his or her device, and it will continue to run until the esc key is pressed, and to do so:

	>>> Copy and paste the "script - Shortcut" file into the Startup directory.
	>>> Press 'win+r' to get to that directory, then type "shell:startup" and paste the file here.