import asyncio
from bleak import BleakClient

address = "C8:7F:41:4B:1D:F4"

async def run(address):    
    async with BleakClient(address) as client:
        print('connected')
        # 연결한 장치의 서비스 정보 얻기
        services = await client.get_services()
        # 리턴 받은 services의 타입 확인
        print("Services:", type(services))
        # 루프를 돌면서 출력
        for service in services:
            print(service)
    print('disconnect')

loop = asyncio.get_event_loop()
loop.run_until_complete(run(address))
print('done')