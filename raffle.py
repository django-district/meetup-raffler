import csv
import random
import sys
import time

class Attendee(object):
    """A small class to represent an attendee"""

    def __init__(self, name, profile_url):
        self.name = name
        self.profile_url = profile_url

# Get the filename of the CSV of attendees (already converted from XLS)
meetup_csv = sys.argv[1]

# Read the attendees out of the file
attendees = []
with open(meetup_csv, 'rb') as csvfile:
    reader = csv.reader(csvfile)

    # Skip the header row
    reader.next()

    # Iterate over the attendees
    for row in reader:
        attendee = Attendee(name=row[0], profile_url=row[-1])
        attendees.append(attendee)

# WHO'S GONNA WIN?!?!?
print "AND THE WINNER IS..."

# time.sleep for dramatic effect
time.sleep(2)

# Pick the winner
winner = random.choice(attendees)
print "{0} ({1})".format(winner.name, winner.profile_url)
