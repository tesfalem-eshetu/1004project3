def read_market_data(filename):
    zip_to_markets = {}
    town_to_zip = {}

    with open(filename, 'r') as file:
        for line in file:
            fields = line.strip().split('@')

            if len(fields) != 7:
                continue

            state, market_name, street_address, city, zip_code, _, _ = fields

            if not zip_code or not city or not market_name or not street_address:
                continue

            market_tuple = (state, market_name, street_address, city, zip_code)

            if zip_code not in zip_to_markets:
                zip_to_markets[zip_code] = []
            zip_to_markets[zip_code].append(market_tuple)

            city_lower = city.lower()
            if city_lower not in town_to_zip:
                town_to_zip[city_lower] = set()
            town_to_zip[city_lower].add(zip_code)

    return zip_to_markets, town_to_zip


def format_market_data(market_tuple):
    state, market_name, street_address, city, zip_code = market_tuple
    return f"{market_name}\n{street_address}\n{city}, {state} {zip_code}"


def main():
    zip_to_markets, town_to_zip = read_market_data("markets.txt")

    while True:
        user_input = input("Enter a zip code or a town name (or 'quit'): ").strip().lower()

        if user_input == "quit":
            break

        if user_input.isdigit():
            if user_input in zip_to_markets:
                for market in zip_to_markets[user_input]:
                    print(format_market_data(market), "\n")
            else:
                print("Not found.")
        else:
            if user_input in town_to_zip:
                for zip_code in town_to_zip[user_input]:
                    for market in zip_to_markets[zip_code]:
                        print(format_market_data(market), "\n")
            else:
                print("Not found.")


if __name__ == "__main__":
    main()
