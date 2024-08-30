# bluetooth_ble_connection.py

import asyncio
from bleak import BleakClient

class ELM327BLE:
    def __init__(self, address):
        self.address = address
        self.client = None

    async def connect(self):
        try:
            self.client = BleakClient(self.address)
            await self.client.connect()
            if self.client.is_connected:
                print("Connected to ELM327 via BLE")
                await self.initialize_elm327()
            else:
                print("Failed to connect to ELM327")
        except Exception as e:
            print(f"BLE connection failed: {e}")

    async def initialize_elm327(self):
        await self.send_command("ATZ")  # Reset ELM327
        await self.send_command("ATE0")  # Echo Off
        await self.send_command("ATSP0")  # Set Protocol to Auto
        print("ELM327 Initialized")

    async def send_command(self, command):
        if self.client and self.client.is_connected:
            await self.client.write_gatt_char("<CHARACTERISTIC_UUID>", f"{command}\r".encode())
            response = await self.client.read_gatt_char("<CHARACTERISTIC_UUID>")
            return response.decode('utf-8').strip()
        return None

    async def disconnect(self):
        if self.client:
            await self.client.disconnect()
            print("BLE connection closed")
