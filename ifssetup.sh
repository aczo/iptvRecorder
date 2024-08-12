sudo route add -net 224.0.0.0/4 dev $INTERFACE
sudo ifconfig $INTERFACE allmulti
