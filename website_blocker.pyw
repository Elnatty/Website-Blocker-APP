import time
from datetime import datetime as dt
#host_path = 'hosts'             # if using pycharm or any other editor, pass in the file path here.
host_main_path = 'c:/Windows/System32/drivers/etc/hosts'        # the actual path for windows.
redirects = '127.0.0.1'         # redirects all traffic here to block internet access to specific sites.
# few list of websites to block, you can add more.
website_list = ['www.facebook.com','facebook.com','yahoomail.com','www.twitter.com']

while True:
    # specifying conditional statements
    # this blocks access to websites during working hours ie: between 8am to 4pm.
    if dt(dt.now().year, dt.now().month, dt.now().day,8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,16):
        print('Working hours...')
        with open(host_main_path, 'r+') as file:         # open file for read and write (r+).
            content = file.read()
            for website in website_list:            # iterating through the list of websites to block.
                if website in content:
                    pass
                else:
                    file.write(redirects+' '+ website+'\n')
    else:
        with open(host_main_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)                            # brings cusor to the beginning of the file.
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print('Fun hours...')
    time.sleep(5)                                   # updates/checks every 5seconds.

# to run script in windows background, you need to run as admin or have admin priviledges.
# make sure script is .pyw extension to remain running in background.
# use task scheduler.
