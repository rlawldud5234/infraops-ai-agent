# Infrastructure Troubleshooting Methodology

## Internet Connectivity Failure

When a VM cannot access the Internet, investigate the problem
layer by layer.

### Step 1: VM

Check:

- VM power state
- vNIC connection
- IP address
- subnet mask
- default gateway

### Step 2: Network

Check:

- Port group
- VLAN
- gateway reachability
- routing
- Tier-1 router
- Tier-0 router

### Step 3: Firewall

Check:

- Distributed Firewall status
- outbound policy
- source
- destination
- protocol
- rule order
- rule hit count

### Step 4: NAT

Check:

- SNAT policy
- SNAT status
- source network
- destination
- translated address

### Step 5: External Network

Check:

- edge node
- upstream connectivity
- external gateway
- return path

## Evidence-Based Troubleshooting

Do not conclude the root cause from a single configuration value.

Compare multiple pieces of evidence.

For example:

- Gateway reachable
- Internet unreachable
- DFW DENY
- Matching DENY rule
- Non-zero hit count

Together these provide stronger evidence that the firewall rule
is responsible for the connectivity failure.

## Change Management

Do not automatically change firewall or network configuration.

Before making a change:

1. Confirm the affected scope.
2. Verify the required business traffic.
3. Check security requirements.
4. Obtain appropriate approval.
5. Apply the change.
6. Verify connectivity.
7. Monitor the result.