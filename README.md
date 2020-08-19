# Hack13-44-SpamBot
Based on electoral district, automatically emails your elected representatives

## Background
[represent.opennorth.ca](https://represent.opennorth.ca/demo/) provides name and contact information for elected officials in Canada based on your location. Since this already exists, we can use their API to easily get this info instead of searching for it ourselves. Initial researched showed that nothing on this level (of ease of use) exists for the USA, so we will just focus on Canada.

## Initial Goal
Given a text file conataining the email body and an address/geolocation, our hack will compile a list of elected officials and send out the same email (individually addressed to each representative). It will be simplest to call the program from the command line.

## Stretch Goal
1. Add a UI that makes it easier/more convenient to use
1. Remove the email composition step! Based on a topic (police reform, increased property taxes, ect) and a stance (for or against), autogenerate the email text for the user.

## Running
To run, this first involves setting up credentials to access a Gmail account through the Gmail API. After this is set up, create/activate a python virtual environment. Install the dependencies in requirements.txt and run the following:
```
python main.py
```
Follow the prompts to open a web browser, and fill in the corresponding fields on the form. When submitted, this will email your representatives and you should see the emails in the sent folder of the email account you set this up with.
