import logging


from pymodbus.client import AsyncModbusTcpClient
from pymodbus.transaction import ModbusSocketFramer


_logger = logging.getLogger()
_logger.setLevel("DEBUG")


def setup_async_client(host, port):
    client = AsyncModbusTcpClient(host=host, port=port, framer=ModbusSocketFramer)
    return client


def close_modbus_client(client):
    # 关闭Modbus连接
    client.close()
