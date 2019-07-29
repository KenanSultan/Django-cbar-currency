import xml.etree.ElementTree as ET
from datetime import datetime, timedelta
import requests
import json
from django.conf import settings

class Currency:

    @staticmethod
    def get_list_from_cbar(day):
        url = "https://www.cbar.az/currencies/"+day+".xml"
        result = requests.get(url)

        if result.status_code == 200:
            content = ET.fromstring(result.text)

            return content[1]

        return False

    @staticmethod
    def get_currency_difference(yesterdayList, todayList):
        difference_list = list()
        for index, value in enumerate(todayList):
            valyuta = value[1].text
            kod = value.attrib['Code']
            kurs = value[2].text
            nominal = value[0].text
            exact_difference = float(value[2].text) - float(yesterdayList[index][2].text)
            if exact_difference > 0:
                difference = 'ex_up'
            elif exact_difference < 0:
                difference = 'ex_down'
            else:
                difference = 'ex_same'

            difference_list.append({
                'name' : valyuta,
                'kod' : kod,
                'kurs' : kurs,
                'nominal': nominal,
                'difference' : difference
            })

        return difference_list

    @staticmethod
    def write_difference_to_file(difference, file_name):
        with open("/".join(settings.CBAR_CURRENCY_ROOT, file_name), 'w') as file:
            file.write(json.dumps(difference))

    @staticmethod
    def read_file(file_name):
        with open("/".join(settings.CBAR_CURRENCY_ROOT, file_name), 'r') as file:
            content = file.read()
        
        return json.loads(content)

    @staticmethod
    def get_list():
        try:
            return Currency.read_file('currency_difference.txt')
        except:
            return []

    @staticmethod
    def get_specific_currencies(specific_currencies):
        all_currencies = Currency.get_list()
        for currency in all_currencies:
            if currency['kod'] in specific_currencies:
                specific_currencies.insert(specific_currencies.index(currency['kod']), currency)
                specific_currencies.remove(currency['kod'])

        return specific_currencies

    @staticmethod
    def get_currencies_by_priority(priority_names):
        all_currencies = Currency.get_list()
        for currency in all_currencies:
            if currency['kod'] in priority_names:
                all_currencies.remove(currency)
                all_currencies.insert(priority_names.index(currency['kod']), currency)

        return all_currencies

    @staticmethod
    def cron_script():
        yesterday = datetime.strftime(datetime.now() - timedelta(1),"%d.%m.%Y")
        today = datetime.strftime(datetime.now(),"%d.%m.%Y")

        try:
            yesterdayXml = Currency.get_list_from_cbar(yesterday)
            todayXml = Currency.get_list_from_cbar(today)

            currencyDifference = Currency.get_currency_difference(yesterdayXml, todayXml)

            Currency.write_difference_to_file(currencyDifference, 'currency_difference.txt')
        except:
            pass
