import logging

from pymodbus.client import ModbusTcpClient


_logger = logging.getLogger()
_logger.setLevel("DEBUG")


def setup_sync_client(host, port):
    client = ModbusTcpClient(host=host, port=port)
    return client


def close_modbus_client(client):
    # 关闭Modbus连接
    client.close()
