# VMware vSphere Network Troubleshooting

## Virtual Machine Network

When troubleshooting VM connectivity, check:

1. VM power state
2. Virtual NIC connection state
3. Port group
4. VLAN
5. IP address
6. Subnet mask
7. Default gateway
8. DNS configuration

## vNIC

The virtual NIC must be connected for the VM to communicate with
the virtual network.

A disconnected vNIC can cause complete network connectivity failure.

## Port Group

Verify that the VM is connected to the expected port group.

A wrong port group can place the VM into an unexpected network segment.

## VLAN

Verify that the VLAN configuration matches the expected network design.

A VLAN mismatch can prevent communication between the VM and its
expected gateway or network segment.

## Gateway

If the VM can reach its default gateway, basic Layer 2 and Layer 3
connectivity to the gateway is likely working.

If the gateway is unreachable, investigate:

- vNIC
- port group
- VLAN
- IP address
- subnet mask
- gateway configuration