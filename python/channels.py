import csv


def get_channels(filename):
  channels={}

  #read channels from config file
  with open(filename, mode='r') as file:
    # Create a CSV reader object
    csv_reader = csv.reader(file)
    
    # Iterate through each row in the CSV file
    for row in csv_reader:
        # Extract the IP address and channel name from the row
        ip_address, channel_name = row
        channels[ip_address] = channel_name
    return channels
