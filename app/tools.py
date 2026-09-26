import json
from pathlib import Path

from agents import function_tool


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"


def load_json(filename: str):
    """Load JSON data from the data directory."""
    with open(DATA_DIR / filename, "r", encoding="utf-8") as f:
        return json.load(f)


@function_tool
def get_vm_status(vm_name: str) -> str:
    """
    Get VM status and basic configuration.

    Args:
        vm_name: Name of the VM, for example web-001.
    """
    data = load_json("vm_data.json")

    vm = data.get(vm_name)

    if not vm:
        return f"VM '{vm_name}' was not found."

    return json.dumps(
        {
            "vm_name": vm_name,
            **vm
        },
        ensure_ascii=False,
        indent=2
    )


@function_tool
def get_network_info(vm_name: str) -> str:
    """
    Get VMware and NSX-T network information for a VM.

    Args:
        vm_name: Name of the VM, for example web-001.
    """
    data = load_json("network_data.json")

    network = data.get(vm_name)

    if not network:
        return f"Network information for '{vm_name}' was not found."

    return json.dumps(
        {
            "vm_name": vm_name,
            **network
        },
        ensure_ascii=False,
        indent=2
    )


@function_tool
def check_firewall(vm_name: str) -> str:
    """
    Check NSX-T Distributed Firewall and NAT information.

    Args:
        vm_name: Name of the VM, for example web-001.
    """
    data = load_json("firewall_data.json")

    firewall = data.get(vm_name)

    if not firewall:
        return f"Firewall information for '{vm_name}' was not found."

    return json.dumps(
        {
            "vm_name": vm_name,
            **firewall
        },
        ensure_ascii=False,
        indent=2
    )