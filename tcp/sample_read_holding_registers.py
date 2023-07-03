import logging
import time
from pymodbus.exceptions import ModbusIOException

_logger = logging.getLogger()
_logger.setLevel("DEBUG")


# holding_register model
async def read_holding_register(client, address: int, quantity: int, slaveID: int):
    host = "127.0.0.1"
    port = 5020
    try:
        _logger.info("### Client starting")
        await client.connect()
        assert client.connected
        while True:
            response = await client.read_holding_registers(
                address=address, count=quantity, slave=slaveID
            )
            if response.isError():
                print(
                    f"### read error - IP: {host}, port: {port}, address: {address}, errorMessage: {response}"
                )
            else:
                values = response.registers
                print(
                    f"### read values - IP: {host}, port: {port}, address: {address},quantity: {quantity} value: {values}"
                )
            time.sleep(2)
    except ModbusIOException as e:
        print(
            f"communication error  - IP: {host}, 端口: {port}, address: {address}, errorMessage: {e}"
        )
