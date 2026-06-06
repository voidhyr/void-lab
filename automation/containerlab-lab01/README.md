# containerlab-lab01

3-router FRR lab using Containerlab + Docker.
Automated with Netmiko over SSH.

## Topology
R1 -- R2 -- R3

## Stack
- Containerlab + FRRouting (Alpine)
- Netmiko for SSH automation
- Python 3

## Run
```bash
# Deploy lab
sudo containerlab deploy -t lab01.yml

# Activate venv
source ~/netauto-env/bin/activate

# Run script
python3 first_connect.py
```
