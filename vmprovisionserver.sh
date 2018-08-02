#!/bin/bash

## cleanups

echo "cleaning up known_hosts"
> ~/.ssh/known_hosts
echo "cleaning up inventory"
> inventory
echo "recreating inventory"
./createinv.py
echo "running playbook"
ansible-playbook vmprov.yaml -k
