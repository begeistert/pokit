import asyncio
from bleak import BleakScanner, BleakClient


def __getDevices__():
    async def run():
        devices = await BleakScanner.discover()
        data = devices[1].address
        print(data)
        return devices

    loop = asyncio.get_event_loop()
    return loop.run_until_complete(run())


def __selectDevice__(devices):
    select = 0
    for d in devices:
        print(str(select) + ". " + d.__repr__())
    identifier = int(input("Select your device: ").strip())
    return devices[identifier].address if identifier < len(devices) else ""


def connectDevice():
    async def run(device):
        async with BleakClient(device) as client:
            model_number = await client.read_gatt_char(device[1])
            print("Model Number: {0}".format("".join(map(chr, model_number))))

    loop = asyncio.get_event_loop()
    loop.run_until_complete(run(__selectDevice__(__getDevices__())))
