import asyncio
from tcp import sample_read_holding_registers


if __name__ == "__main__":
    asyncio.run(sample_read_holding_registers.read_holding_register(4, 2, 1))
