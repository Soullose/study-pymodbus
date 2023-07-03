import time
import random
import logging

from pymodbus.server.async_io import StartTcpServer, ServerStop
from pymodbus.device import ModbusDeviceIdentification
from pymodbus.server import ModbusTcpServer
from pymodbus.datastore import (
    ModbusSequentialDataBlock,
    ModbusSlaveContext,
    ModbusServerContext,
)

# Enable logging (makes it easier to debug if something goes wrong)
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.DEBUG)

data_block = None  # 全局变量，用于存储数据块


def start_sample_modbus_simulator():
    # Define the Modbus registers
    coils = ModbusSequentialDataBlock(1, [True] * 100)
    discrete_inputs = ModbusSequentialDataBlock(1, [False] * 100)
    # 创建数据块，用于存储寄存器的值
    holding_registers = ModbusSequentialDataBlock(1, [0] * 100)
    input_registers = ModbusSequentialDataBlock(1, [0] * 100)

    temperature_values = [random.randint(1, 200) for _ in range(100)]
    holding_registers.setValues(1, temperature_values)
    print("temperature_values:", temperature_values)

    # 创建从设备上下文，包含一个数据块
    slave_context = ModbusSlaveContext(
        co=coils, di=discrete_inputs, hr=holding_registers, ir=input_registers
    )

    identity = ModbusDeviceIdentification(
        info_name={
            "VendorName": "Pymodbus",
            "ProductCode": "PM",
            "VendorUrl": "https://github.com/pymodbus-dev/pymodbus/",
            "ProductName": "Pymodbus Server",
            "ModelName": "Pymodbus Server",
            "MajorMinorRevision": 1.0,
        }
    )

    # 创建服务器上下文，将从设备上下文添加到服务器上下文中
    server_context = ModbusServerContext(slaves=slave_context, single=True)
    StartTcpServer(
        context=server_context, address=("localhost", 502), identity=identity
    )


if __name__ == "__main__":
    start_sample_modbus_simulator()
