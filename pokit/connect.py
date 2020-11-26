import asyncio
from bleak import BleakScanner, BleakClient, discover


def __getDevices__():
    async def run():
        return await BleakScanner.discover()

    loop = asyncio.get_event_loop()
    return loop.run_until_complete(run())


def __selectDevice__():
    devices = []

    async def run():
        return await discover()

    while True:
        loop = asyncio.get_event_loop()
        devices = loop.run_until_complete(run())
        select = 0
        for d in devices:
            print(str(select) + ". " + d.__repr__())
            select += 1
        identifier = input("Select your device or press a to rescan: ").strip()
        if not identifier == 'a':
            identifier = int(identifier)
            break
    return devices[identifier] if identifier < len(devices) else ""


def connectDevice():
    async def run(device):
        async with BleakClient(device) as client:
            # await client.read_gatt_char('e7481d2f-5781-442e-bb9a-fd4e3441dadc')
            intervals = 1000
            intervals = intervals.to_bytes(4, 'big')
            await client.write_gatt_char('53dc9a7a-bc19-4280-b76b-002d0e23b078',
                                         bytearray(b'\x09\x00\x01\x00\x00\x00\x00'))
            continuity = await client.read_gatt_char('047d3559-8bee-423a-b229-4417fa603b90')
            print("Model Number: {0}".format("".join(map(chr, continuity))))

    loop = asyncio.get_event_loop()
    loop.run_until_complete(run(__selectDevice__()))
