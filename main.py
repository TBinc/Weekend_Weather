# main.py
import argparse
import os
from weather_api import get_weather_data, get_printable_forecast
from diagram import empty_diagram, filled_diagram


def main() -> None:
    """
    Main function to execute the program. It parses command-line arguments and makes the necessary function calls.
    """
    # Create a parser and define its arguments
    parser = argparse.ArgumentParser(description="Weather forecast for the weekend.")
    parser.add_argument("--zip", type=int, help="ZIP Code to forecast.", required=True)
    parser.add_argument("--forecast", action="store_true", help="Print forecast.")
    parser.add_argument(
        "--agg", action="store_true", help="Aggregated instead of three hour forecast."
    )
    parser.add_argument(
        "--diag", action="store_true", help="Generate a flowchart diagram."
    )
    parser.add_argument(
        "--with_data", action="store_true", help="Calls API to show results in diagram."
    )

    # Parse the arguments provided by the user
    args = parser.parse_args()

    # Get weather data for the provided ZIP code
    data = get_weather_data(args.zip)

    # If the --forecast argument is provided, print the forecast
    if args.forecast:
        res = get_printable_forecast(data, aggregated=args.agg)
        print(res)
    # If the --diag argument is provided, generate the diagram
    if args.diag:
        if args.with_data:
            # If --with_data is provided, generate the diagram with the weather data
            filled_diagram(
                args.zip, aggregated=args.agg, data=data, path=os.path.abspath("./html")
            )
        else:
            # If --with_data is not provided, generate an empty diagram
            empty_diagram(path=os.path.abspath("./html"))


if __name__ == "__main__":
    main()
