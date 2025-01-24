import logging

import aiohttp


logger = logging.getLogger(__name__)


class IMEICheckService(object):
    url: str = "https://api.imeicheck.net/v1/checks/"

    def __init__(self, api_token: str, imei: str):
        self.imei = imei
        self.headers = {"Authorization": f"Bearer {api_token}"}

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    async def check_imei(self) -> dict | None:
        async with aiohttp.ClientSession() as session:
            async with session.post(
                    self.url,
                    headers=self.headers,
                    data={"deviceId": self.imei, "serviceId": 22}
            ) as response:
                if response.status != 201:
                    logger.warning(response)
                    return None
                return await response.json()
