import asyncio
import tcp_async
from tcp import sample_read_holding_registers


if __name__ == "__main__":
    host = "127.0.0.1"
    port = 5020
    client = tcp_async.setup_async_client(host, port)
    asyncio.run(sample_read_holding_registers.read_holding_register(client, 4, 2, 1))
