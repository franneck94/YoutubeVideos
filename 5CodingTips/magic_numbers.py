def add_taxes(price_without_taxes, country_code):
    if country_code == 0:
        return price_without_taxes * 1.19
    elif country_code == 1:
        return price_without_taxes * 1.16


if __name__ == "__main__":
    price = 20.0  # in euro
    price_with_taxes = add_taxes(price, 0)
