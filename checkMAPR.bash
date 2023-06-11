#!/bin/bash
print 1,2,3,4,5,6,7
# Define the nodes of the cluster
NODES=( node1 node2 node3 node4 node5 node6 node7 node8 node9 node10 )

# Iterate over the nodes and check if the disks are mounted
for NODE in "${NODES[@]}"
do
  echo "Checking disks on node $NODE..."
  ssh $NODE df -h | grep /dev/sd
done
