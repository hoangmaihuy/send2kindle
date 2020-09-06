# send2kindle
Python script to send ebooks to Kindle devices

# Usage
``` bash
git clone https://github.com/hoangmaihuy/send2kindle.git && cd send2kindle
```

Change ```config_template.json``` to your email address and kindle address. Command to send books to kindle:
``` bash
./send2kindle {first_path_to_your_book} {second_path_to_your_book} 
```

You can use send2kindle as a command line by adding it to alias. Open your ```.bashrc``` or ```.zshrc``` file and add following line:
``` bash
alias s2k="python3 {path_to_send2kindle_directory}/send2kindle.py"
```

Now send books to kindle is as simple as
``` bash
s2k ~/Documents/example_book.pdf 
```

# FAQ
### How do I know my kindle email?
Refer [here](https://www.amazon.com/gp/help/customer/display.html?nodeId=G7NECT4B4ZWHQ8WV) for more information.


### I can't log in my Gmail. Error: Application-specific password required
If you turn on 2-step verification, you need to create an App Password for your Gmail to log in. Refer [here](https://support.google.com/mail/?p=InvalidSecondFactor) for more information.