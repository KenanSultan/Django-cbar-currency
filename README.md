# Getting currencies and differencies from CBAR

    ## How to install
        1. Install pip package
            ```
            pip install Django-cbar-currency
            ```
        2. Configure directory for file
            In settings.py file set a directory
            ```
            CBAR_CURRENCY_ROOT = os.path.join(BASE_DIR, 'media', 'cbar')
            ```

    ## How to import
        ```
        from cbar_currency import Currency
        ```

    ## Functions
        1. Currency.cron_script()
            This function gets currency list with their values, differences and right them to file

        2. Currency.get_list()
            This function reads currency file and returns all currencies with their values and differencies as list

        3. Currency.get_specific_currencies(currencyList)
            This function returns specific currencies list which you give
            You should give currency names as list, for example  ['USD', 'EUR', 'RUB']

        4. Currency.get_currencies_by_priority(currencyList)
            This function returns all currencies list but currencies which you give will stay at the top of the list
            You should give currency names as list, for example  ['USD', 'EUR', 'RUB']

        5. Currency.get_list_from_cbar(date)
            This function returns all currencies list without differencies for the specific date

