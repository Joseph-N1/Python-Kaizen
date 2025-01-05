import pandas as pd
from datetime import datetime  # Importing datetime class from datetime module

def Holiday_package():
    user = {}

    print ("Welcome to our holidays package service!")
    while True:
        looking_vacation = input ("Are you looking to plan a vacation soon (YES/NO)? :").lower()
        if looking_vacation == "YES":
            user["looking_vacation"] = looking_vacation
            while True:
                planning_month = input ("Great! May I know in which month you are planning your vacation? :"). lower()
                if planning_month in lower_months:
                    user["planning_month"]= planning_month
                    break
                else:
                    print("Enter proper month like 'January' or 'Jan' ")
            break
        elif looking_vacation =="No".lower():
            user["looking_vacation"] = looking_vacation 
            print("Thanks for visiting us, Let me know when you plan for vacation.")
            break

        else:
             print("Enter your answer in YES or NO only")


    while True:
        if looking_vacation == "NO".lower():
            break
        else:
             Destination_type= input( "What type of destination are you interested in for your holiday? (e.g., Beach, Mountains, City, Hill area): ").lower()
             if Destination_type in valid_destination:
                user['Destination_type'] = Destination_type
                break
             else:
                print("Your Destination is not listed, Please choose from listed ones available (e.g, Beach, Mountains, City, 'hill area')")
    while True:
        if looking_vacation == "NO".lower():
            break
        else:
            person= input("How many people will be traveling with you on this vacation? : ")
            if person.isdigit():
                user["person"]= person
                break
            else:
                print("Please enter only in no.digit")
    while True:
        if looking_vacation == "NO".lower():
            break
        else:
            Plan_date =input ("What are your preferred travel dates or timeframe for this trip? (YYYY-MM-DD) :" )
           
            if is_valid_date(Plan_date):
                user["Plan_date"]= Plan_date
                break
            else:
                print("Invalid date, Please enter in (YYYY-MM-DD) format.")

    while True:
        if looking_vacation =="NO".lower():
            break
        else:
             activity = input("Do you have any specific activities or experinences in mind for your holiday? ").lower()
             if activity == "YES":
                user["activity"]= activity
                while True:
                     activity_name =input ( "What kind of activities would you like (e.g., swimming, boating, paragliding)? :").lower()
                     if activity_name in activity_list:
                         user["activity_name"]= activity_name
                         break
                     else:
                         print("Your activity is not listed, Please choose from the list above")
                break
             elif activity =="NO":
                 user["activity"]=activity 
                 break
             else:
                 print("Please answer using 'YES' or 'NO' only: ")

    while True:
        if looking_vacation =="NO".lower():
            break
        else:
            budget = input("What is your budget for this vacation package?: ")
            if budget.isdigit():
                user["budget"]= budget
                break
            else:
                print("Please enter budget only in numbers: ")
                
    while True:
        if looking_vacation =="NO".lower():
            break
        else:
            planned = input ( "Have you planned any particular destinations or countries? : ").lower()
            if planned =="YES":
                user["planned"]=planned
                destination= input("May I know which destinations or countries you have planned? : ")
                if destination.isdigit():
                    print("only number cant be destination or country name, Please enter proper destinations or country name: ")
                else:
                    user["destination"]=destination
                    break
            elif planned =="NO":
                user["planned"]=planned
                break
            
            else:
                print("Please answer in 'YES' or 'NO' only")


    while True:
        if looking_vacation =="NO".lower():
            break
        else:
            package_type = input("Would you prefer a pre-planned package or a custom itinerary tailored to your prefernces? :")
            user["package_type"]= package_type
            break

    while True:
        if looking_vacation =="NO".lower():
            break
        else:
            share_ask= input("Is there anything else you would like to share or ask about regarding your holiday plans? :")
            user["ask"]= share_ask
        break

    while True:
        new_user= input("If you want to enter more information, press 'Y'; otherwise, press 'N'. : ")
        if new_user == "Y":
            Holiday_package()
            break
        elif new_user =="N":
            print ("Thanks for visiting us!")
            break
        else:
            print("Press only 'Y' or 'N' to continue: ")
            
            
            valid_destination=['beach', 'mountains','city','hill area','hill']
activity_list=["swimming","boating","paragliding","para"]
valid_months=['January','Febuary','March', 'April', 'May','June','July','August','September','October','November','December',
              'Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct', 'Nov', 'Dec']
lower_months= [item.lower() for item in valid_months]

   

def is_valid_date(date_text, date_format='%Y-%m-%d'):
    """
    This function checks if the date_text conforms to the given date_format.
    :param date_text: str, the date in string form to be checked.
    :param date_format: str, the format against which to check the date_text.
    :return: bool, True if date_text conforms to date_format, False otherwise.
    """
    try:
        datetime.strptime(date_text, date_format)  # strptime is used to parse a date string into a datetime object.
        return True
    except ValueError:
        return False


# Function to collect data in a DataFrame
def collect_data():
    user_data = Holiday_package()
    return pd.DataFrame([user_data])

# Call the function to display DataFrame
print(collect_data())