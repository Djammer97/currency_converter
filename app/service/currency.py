import xmltodict

from app.core.config import settings
from app.core.exceptions import InvalidCurrencyCode
from app.uow.uow import IUnitOfWork


class CurrencyService:
    def __init__(self, uow: IUnitOfWork):
        self.uow = uow

    async def get_full_currency_data(self):
        async with self.uow as uow:
            response = await uow.session.get(settings.all_currency_http_address)
            result = xmltodict.parse(await response.text())["ValCurs"]["Valute"]
            result = list(
                map(
                    lambda one_data: {
                        "@ID": one_data["@ID"],
                        "Name": one_data["Name"],
                        "CharCode": one_data["CharCode"],
                        "VunitRate": one_data["VunitRate"].replace(",", "."),
                    },
                    result,
                )
            )

            result.append({"@ID": 0, "Name": "Российский рубль", "CharCode": "RUB", "VunitRate": "1"})

            # result = list(map(lambda one_data: one_data["VunitRate"].replace(",", "."), result))

        return result

    async def currency_convert(self, code_from: str, code_to: str, value_from: float):
        data = await self.get_full_currency_data()

        try:
            from_data = list(filter(lambda one_data: one_data["CharCode"] == code_from, data))[0]
        except IndexError:
            raise InvalidCurrencyCode

        try:
            to_data = list(filter(lambda one_data: one_data["CharCode"] == code_to, data))[0]
        except IndexError:
            raise InvalidCurrencyCode

        messege = f"{value_from} - "
        messege += from_data["Name"] + " "
        messege += str(round(value_from * float(from_data["VunitRate"]) / float(to_data["VunitRate"]), 2))
        messege += f' - {to_data["Name"]}'

        return {"messege": messege}
