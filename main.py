import datetime
import envs
import os
import time

envs.init()
_interval = envs.INTERVAL
_nics = envs.NICS

if not os.path.exists("./logs/"):
    os.makedirs("./logs/")


def log(msg):
    print(msg)
    with open("./logs/traffic-usage", "a") as file:
        file.write(
            "{} | {}\n".format(
                datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), msg
            )
        )


def get_rx_tx(nic):
    lines = []
    with open("/proc/net/dev", "r") as file:
        lines = file.readlines()
    for line in lines:
        if line.strip().startswith(nic):
            return int(line.split()[1]), int(line.split()[9])
    return 0, 0


def main():
    log("Starting script...")
    log(f"Network interface(s): {_nics}")

    store = {}
    sum_rx = 0
    sum_tx = 0
    for nic in _nics:
        nic_rx, nic_tx = get_rx_tx(nic)
        store[nic] = {"rx": nic_rx, "tx": nic_tx}
        sum_rx += nic_rx
        sum_tx += nic_tx
        log(
            "{:>5} | Initial RX value: {:>10,.3f} GB , TX value: {:>10,.3f} GB".format(
                nic, nic_rx / 1000000000, nic_tx / 1000000000
            )
        )

    if len(_nics) > 1:
        log(
            "{:>5} | Initial RX value: {:>10,.3f} GB , TX value: {:>10,.3f} GB".format(
                "SUM", sum_rx / 1000000000, sum_tx / 1000000000
            )
        )
        log(
            "---------------------------------------------------------------------------------"
        )

    while True:
        time.sleep(_interval)
        sum_rx = 0
        sum_tx = 0
        sum_rx_change = 0
        sum_tx_change = 0
        for nic in _nics:
            new_rx, new_tx = get_rx_tx(nic)
            rx_change = new_rx - store[nic]["rx"]
            tx_change = new_tx - store[nic]["tx"]
            store[nic] = {"rx": new_rx, "tx": new_tx}
            sum_rx += new_rx
            sum_tx += new_tx
            sum_rx_change += rx_change
            sum_tx_change += tx_change
            log(
                "{:>5} | RX: {:>10,.3f} GB , TX: {:>10,.3f} GB | ΔRX: {:>7,.3f} MB , ΔTX: {:>7,.3f} MB".format(
                    nic,
                    new_rx / 1000000000,
                    new_tx / 1000000000,
                    rx_change / 1000000,
                    tx_change / 1000000,
                )
            )

        if len(_nics) > 1:
            log(
                "{:>5} | RX: {:>10,.3f} GB , TX: {:>10,.3f} GB | ΔRX: {:>7,.3f} MB , ΔTX: {:>7,.3f} MB".format(
                    "SUM",
                    sum_rx / 1000000000,
                    sum_tx / 1000000000,
                    sum_rx_change / 1000000,
                    sum_tx_change / 1000000,
                )
            )
            log(
                "---------------------------------------------------------------------------------"
            )


if __name__ == "__main__":
    main()
