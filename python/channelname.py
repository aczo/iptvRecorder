import sys
import channels

chlist = channels.get_channels('channels.csv')

print(chlist[sys.argv[1]])
