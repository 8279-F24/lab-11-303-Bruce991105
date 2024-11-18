# Input list of contacts
contacts_input = input()

# Input the name to search for
search_name = input()

# Split the input into individual pairs
pairs = contacts_input.split()

# Create a dictionary to store contacts
contacts = {}

# Populate the dictionary
for pair in pairs:
    name, phone = pair.split(',')
    contacts[name] = phone

# Output the phone number for the searched name
print(contacts[search_name])
