
import asyncio

from bleak import BleakScanner, BleakClient
mac = ''


async def main():
    devices = await BleakScanner.discover()
    print('Discovered Devices: ')
    #print(len(devices))
    i = 0
    for d in devices:
        print('['+ str(i) + '] '+ str(d))
        i += 1

    print()
    num = input('Choose a device by entering its number indicated by square brackets...')

    target = devices[int(num)]
    print('You chose: ' + str(target)[0:17])
    mac = str(target)[0:17]

    async with BleakClient(mac) as client:
        print('connected')
        for service in client.services:
            print(service)   
        
asyncio.run(main())

