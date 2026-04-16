from pox.core import core
import pox.openflow.libopenflow_01 as of
from datetime import datetime

log = core.getLogger()

# Dictionary to store port states
port_status_dict = {}

def _handle_PortStatus(event):
    port = event.ofp.desc.port_no
    reason = event.ofp.reason

    if reason == of.OFPPR_ADD:
        state = "PORT ADDED"
    elif reason == of.OFPPR_DELETE:
        state = "PORT DELETED"
    elif reason == of.OFPPR_MODIFY:
        state = "PORT MODIFIED"
    else:
        state = "UNKNOWN"

    message = f"{datetime.now()} | Port {port} | {state}"

    # Store status
    port_status_dict[port] = state

    # 🚨 Alert
    print("\n🚨 ALERT:", message)

    # 📊 Display all ports
    print("📊 Current Port Status:")
    for p, s in port_status_dict.items():
        print(f"Port {p} -> {s}")

    # 📝 Log to file
    with open("port_log.txt", "a") as f:
        f.write(message + "\n")


def launch():
    core.openflow.addListenerByName("PortStatus", _handle_PortStatus)
    log.info("Port Monitoring Tool Started 🚀")
