# Linux Network Troubleshooting

## Basic Connectivity

When investigating Linux network problems, check:

- IP address
- subnet mask
- default route
- DNS
- gateway connectivity
- external connectivity

## IP Address

Use the following command to inspect network interfaces:

ip addr

## Routing

Use:

ip route

The default route should point to the expected gateway.

## Connectivity

Gateway connectivity can be tested with:

ping <gateway>

External IP connectivity can be tested with:

ping <external-ip>

DNS can be tested with:

nslookup <hostname>

or:

dig <hostname>

## Troubleshooting Order

A basic troubleshooting sequence is:

1. Check interface state
2. Check IP configuration
3. Check default route
4. Check gateway connectivity
5. Check DNS
6. Check external connectivity
7. Check firewall
8. Check NAT