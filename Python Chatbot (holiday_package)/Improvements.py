import pandas as pd
from datetime import datetime

def Holiday_package():
    user = {}
    print("Welcome to our holidays package service!")

    while True:
        looking_vacation = input("Are you looking to plan a vacation soon (YES/NO)? :").lower()
        if looking_vacation == "yes":
            user["looking_vacation"] = looking_vacation
            while True:
                planning_month = input("Great!, May I know in which month you are planning the vacation for ? :").lower()
                if planning_month in lower_months:
                    user["planning_month"] = planning_month
                    break
                else:
                    print("Enter proper month like 'January' or 'Jan' ")
            break
        elif looking_vacation == "no":
            user["looking_vacation"] = looking_vacation
            print("Thanks for visiting us, let me know when you plan for a vacation.")
            break
        else:
            print("Enter your answer in YES or NO only")

    while looking_vacation == "yes":
        destination_type = input("What type of destination are you interested in for your Holiday? (e.g., Beach, Mountains, City, 'hill area'): ").lower()
        if destination_type in valid_destination:
            user['Destination_type'] = destination_type
            break
        else:
            print("Your Destination is not listed, Please choose from listed ones available (e.g., Beach, Mountains, City, 'hill area')")

    while looking_vacation == "yes":
        person = input("How many people will be travelling with you on this vacation?: ")
        if person.isdigit():
            user["person"] = person
            break
        else:
            print("Please enter only in no. digit")

    while looking_vacation == "yes":
        plan_date = input("What are your preferred travel dates or timeframe for this trip? (YYYY-MM-DD): ")
        if is_valid_date(plan_date):
            user["Plan_date"] = plan_date
            break
        else:
            print("Invalid date, Please enter in (YYYY-MM-DD) format.")

    while looking_vacation == "yes":
        activity = input("Do you have any specific activities or experiences in mind for your holiday? ").lower()
        if activity == "yes":
            user["activity"] = activity
            while True:
                activity_name = input("What kind of activities would you like (swimming, boating, paragliding,...)? ").lower()
                if activity_name in activity_list:
                    user["activity_name"] = activity_name
                    break
                else:
                    print("Your activity is not listed, Please choose from the list above")
            break
        elif activity == "no":
            user["activity"] = activity
            break
        else:
            print("Please answer using 'YES' or 'NO' only: ")

    while looking_vacation == "yes":
        budget = input("What is your budget for this vacation package?: ")
        if budget.isdigit():
            user["budget"] = budget
            break
        else:
            print("Please enter budget only in numbers: ")

    while looking_vacation == "yes":
        planned = input("Are you planned for any particular destinations or countries?: ").lower()
        if planned == "yes":
            user["planned"] = planned
            destination = input("May I know which destinations or countries you planned?: ")
            if destination.isdigit():
                print("Only number can't be destination or country name, Please enter proper destinations or country name: ")
            else:
                user["destination"] = destination
                break
        elif planned == "no":
            user["planned"] = planned
            break
        else:
            print("Please answer in 'YES' or 'NO' only")

    while looking_vacation == "yes":
        package_type = input("Would you prefer a pre-planned package or a custom itinerary tailored to your preferences? :")
        user["package_type"] = package_type
        break

    while looking_vacation == "yes":
        share_ask = input("Is there anything else you would like to share or ask about regarding your holiday plans? :")
        user["ask"] = share_ask
        break

    new_user = input("If you want to continue to enter more users then press 'Y', if not then press 'N' : ")
    if new_user.lower() == "y":
        Holiday_package()
    elif new_user.lower() == "n":
        print("Thanks for visiting us!")
    else:
        print("Press only 'Y' or 'N' to continue: ")

    return user

# Variables must be declared in the global scope
valid_destination = ['beach', 'mountains', 'city', 'hill area', 'hill']
activity_list = ["swimming", "boating", "paragliding", "para"]
valid_months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December',
                'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
lower_months = [item.lower() for item in valid_months]

def is_valid_date(date_text, date_format='%Y-%m-%d'):
    try:
        datetime.strptime(date_text, date_format)
        return True
    except ValueError:
        return False

# Function to collect data in a DataFrame
def collect_data():
    user_data = Holiday_package()
    return pd.DataFrame([user_data])

# Call the function to display DataFrame
print(collect_data())
