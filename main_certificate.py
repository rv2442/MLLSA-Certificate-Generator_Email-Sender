
import os

os.system("pip install -r requirements.txt")

import csv
from certificate import *
from docx import Document
from docx2pdf import convert

# create output folder if not exist
try:
    os.makedirs("Output/Doc")
    os.makedirs("Output/PDF")
except OSError:
    pass

def get_participants(f):
    data = [] # create empty list
    with open(f, mode="r", encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data.append(row) # append all results
    return data

def create_docx_files(filename, list_participate):

    event = input("Enter the event name: ")
    ambassador = input("Enter Ambassador Name: ")

    for index, participate in enumerate(list_participate):
        # use original file everytime
        doc = Document(filename)

<<<<<<< HEAD
        name = participate["Name"].rstrip() # remove
        email = participate["Email"].rstrip() #
=======
        name = participate["Name"].rstrip()
        email = participate["Email"].rstrip()
>>>>>>> 1ad22dc1ca8eb2ea4c651046cd118e55a8fb4642

        replace_participant_name(doc, name)
        replace_event_name(doc, event)
        replace_ambassador_name(doc, ambassador)

        doc.save('Output/Doc/{}.docx'.format(name))

        doc.save('Output/Doc/{}.docx'.format(name))

        # ! if your program working slowly, comment this two line and open other 2 line.
        print("Output/{}.pdf Creating".format(name))
        convert('Output/Doc/{}.docx'.format(name), 'Output/Pdf/{}.pdf'.format(name))

        filepath = os.path.abspath('Output/Pdf/{}.pdf'.format(name))

    
# get certificate template path
certificate_file = "Data/Event Certificate Template.docx"
# get participants path
participate_file = "Data/"+("Participant List.csv" if (input("Test Mode (Y/N): ").lower())[0]=="n" else "temp.csv")

# get participants
list_participate = get_participants(participate_file);

# process data
create_docx_files(certificate_file, list_participate)



