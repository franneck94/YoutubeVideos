import enum


# Country Codes
class CountryCodes(enum.Enum):
    GERMANY = 0
    AUSTIRA = 1


# Taxes by country
TAXES_BY_COUNTRY = {
    CountryCodes.GERMANY: 1.19,
    CountryCodes.AUSTIRA: 1.16
}


def add_taxes(price_without_taxes: float, country_code: CountryCodes):
    # multiplies the price with the tax rate of the country
    return price_without_taxes * TAXES_BY_COUNTRY[country_code]


if __name__ == "__main__":
    price = 20.0  # in euro
    price_with_taxes = add_taxes(price, CountryCodes.GERMANY)
