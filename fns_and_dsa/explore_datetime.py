from datetime import datetime,timedelta

def display_current_datetime():
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(current_date)

def calculate_future_date(days):
    current_date = datetime.now()

    future_date = current_date + timedelta(days=days)
    return future_date.strftime("%Y-%m-%d")


def main():
    days_count = int(input("Enter the number of days to add to the current date: "))
    display_current_datetime()
    print(f"Future date: {calculate_future_date(days_count)}")


if __name__ == "__main__":
    main()
