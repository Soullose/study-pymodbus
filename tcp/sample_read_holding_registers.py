import logging
from pymodbus.exceptions import ModbusIOException
import tcp_async

_logger = logging.getLogger()
_logger.setLevel("DEBUG")


async def read_holding_register(address: int, quantity: int, slaveID: int):
    host = "127.0.0.1"
    port = 5020
    try:
        client = tcp_async.setup_async_client(host, port)
        _logger.info("### Client starting")
        await client.connect()
        assert client.connected
        while True:
            response = await client.read_holding_registers(
                address=address, count=quantity, slave=slaveID
            )
            if response.isError():
                print(
                    f"### 读取错误 - IP: {host}, 端口: {port}, 地址: {address}, 错误信息: {response}"
                )
            else:
                values = response.registers
                print(
                    f"### 读取的值 - IP: {host}, 端口: {port}, 地址: {address},数量: {quantity} 值: {values}"
                )
    except ModbusIOException as e:
        _logger.error(
            f"通信错误 - IP: {client.host}, 端口: {client.port}, 地址: {address}, 错误信息: {e}"
        )
