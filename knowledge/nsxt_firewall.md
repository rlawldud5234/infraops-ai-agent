# NSX-T Distributed Firewall Troubleshooting

## Distributed Firewall

NSX-T Distributed Firewall (DFW) provides distributed traffic filtering
at the workload level.

DFW policies can control traffic between workloads and external networks.

## Outbound Internet Connectivity

When a VM cannot access the external Internet, check the following:

1. VM network interface connectivity
2. Default gateway reachability
3. Routing configuration
4. Distributed Firewall policy
5. NAT/SNAT configuration
6. External connectivity

## DFW Rule Priority

NSX-T firewall rules are evaluated according to policy and rule order.

A deny rule that matches the traffic can prevent the traffic from reaching
the external network.

When troubleshooting a blocked connection, check:

- Source
- Destination
- Service/Protocol
- Applied groups
- Rule order
- Rule action
- Rule hit count

## Rule Hit Count

A non-zero rule hit count indicates that traffic has matched the rule.

A high hit count on a DENY rule can be an important indicator when
investigating connectivity problems.

## NAT

SNAT can translate private source IP addresses to an address that can be
used for external communication.

If the VM can reach its gateway but cannot reach the Internet, verify:

- SNAT policy exists
- SNAT policy is enabled
- Source network matches the policy
- Destination matches the policy
- Firewall policy does not block the traffic before NAT processing