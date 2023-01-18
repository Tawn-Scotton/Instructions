import csv
import os

# global variable to get the current directory path 
curr_path = os.path.dirname(__file__) 

# global variable - use the current path to get Resources folder and the file we want to open
csv_file = curr_path + "\\Resources\\budget_data.csv"

# this function finds the total number of months for the csv file
def total_number_months():
    # this variable will hold the number of months
    total_number_months = 0

    # opening the CSV file - using with open since it automatically closes the file when done
    with open(csv_file, mode ='r') as file:
        # reading the CSV file
        csv_reader = csv.reader(file) 
        # convert to list for easy counter
        csv_list = list(csv_reader)
        # count the rows of the CSV file wile open
        for i in range(len(csv_list)):
            total_number_months = i    
    return total_number_months

# this function finds the total profits/losses for the whole time period
def total_profits():
    # this variable will hold the total profit/loss
    total_profit_value = 0

    # opening the CSV file - using with open since it automatically closes the file when done
    with open(csv_file, mode ='r') as file:
        # reading the CSV file using dictionary reader
        csv_dict_reader = csv.DictReader(file) 

        # loop through the dictionary reader
        for row in csv_dict_reader:
            total_profit_value += int(row["Profit/Losses"])
    return total_profit_value

# this function finds the average change for the entire period
def average_change():
    # this variable will count the months
    month_counter = 0    
    # this variable will hold the previous row value
    previous_value = 0
    # this variable will hold the current row value
    current_value = 0
    # this variable will hold the monthly change between 2 months
    monthly_change = 0
    # this variable will hold the total change
    total_change = 0
    # this variable will hold the average change
    average_change_value = 0

    # opening the CSV file - using with open since it automatically closes the file when done
    with open(csv_file, mode ='r') as file:
        # reading the CSV file using dictionary reader
        csv_dict_reader = csv.DictReader(file) 
        for col in csv_dict_reader:
            # skip the first row for monthly change
            if month_counter > 0:
                # get the current row value
                current_value = int(col["Profit/Losses"])
                # find the difference between the current month profit/loss and the previous month
                monthly_change = current_value - previous_value
                # add the monthly change to the total
                total_change += monthly_change
                # set the current value to the previous value for the next iteration
                previous_value = current_value
            else:
                # set the row value to the previous row that will be used above
                previous_value = int(col["Profit/Losses"])  
            month_counter += 1
    # subtract 1 from the monthly counter since we skipped the first month as a current month
    month_counter -= 1
    # get the average
    average_change_value = total_change / month_counter
    # round the average to 2 decimal places
    average_change_value = round(average_change_value, 2)
    return average_change_value

# this function will return a dictionary containing the greatest increase and associated month
def greatest_increase():
     # this variable will count the months
    month_counter = 0    
    # this variable will hold the previous row value
    previous_value = 0
    # this variable will hold the current row value
    current_value = 0
    # this variable will hold the monthly change between 2 months
    monthly_change = 0   
    # this variable will hold the greatest monthly increase between 2 months
    greatest_monthly_increase = 0
    # this variable will store the month with the greatest increase
    month_with_greatest_increase = ""    

    # opening the CSV file - using with open since it automatically closes the file when done
    with open(csv_file, mode ='r') as file:
        # reading the CSV file using dictionary reader
        csv_dict_reader = csv.DictReader(file) 
        for col in csv_dict_reader:
            # skip the first row for monthly change
            if month_counter > 0:
                # get the current row value
                current_value = int(col["Profit/Losses"])
                # find the difference between the current month profit/loss and the previous month
                monthly_change = current_value - previous_value

                # find the greatest monthly increase and associated month
                if monthly_change > greatest_monthly_increase:
                    greatest_monthly_increase = monthly_change
                    month_with_greatest_increase = col["Date"]
               
                # set the current value to the previous value for the next iteration
                previous_value = current_value
            else:
                # set the row value to the previous row that will be used above
                previous_value = int(col["Profit/Losses"])  
            month_counter += 1

    # add the month and the greatest monthly increase to a dictionary to return
    greatest_increase_dict = {"month": month_with_greatest_increase, "increase": greatest_monthly_increase}   
    return greatest_increase_dict

# this function will return a dictionary containing the greatest decrease and associated month
def greatest_decrease():
     # this variable will count the months
    month_counter = 0    
    # this variable will hold the previous row value
    previous_value = 0
    # this variable will hold the current row value
    current_value = 0
    # this variable will hold the monthly change between 2 months
    monthly_change = 0   
    # this variable will hold the greatest monthly increase between 2 months
    greatest_monthly_decrease = 0
    # this variable will store the month with the greatest increase
    month_with_greatest_decrease = ""    

    # opening the CSV file - using with open since it automatically closes the file when done
    with open(csv_file, mode ='r') as file:
        # reading the CSV file using dictionary reader
        csv_dict_reader = csv.DictReader(file) 
        for col in csv_dict_reader:
            # skip the first row for monthly change
            if month_counter > 0:
                # get the current row value
                current_value = int(col["Profit/Losses"])
                # find the difference between the current month profit/loss and the previous month
                monthly_change = current_value - previous_value

                # find the greatest monthly decrease and associated month
                if monthly_change < greatest_monthly_decrease:
                    greatest_monthly_decrease = monthly_change
                    month_with_greatest_decrease = col["Date"]
               
                # set the current value to the previous value for the next iteration
                previous_value = current_value
            else:
                # set the row value to the previous row that will be used above
                previous_value = int(col["Profit/Losses"])  
            month_counter += 1

    # add the month and the greatest monthly decrease to a dictionary to return
    greatest_decrease_dict = {"month": month_with_greatest_decrease, "decrease": greatest_monthly_decrease}   
    return greatest_decrease_dict

# this function displays and writes to a file the financial results
def display_financial_results():
    # get the greatest increase as a dictionary with month and increase
    greatest_increase_dict = greatest_increase()
    # get the greatest decrease as a dictionary with month and decrease
    greatest_decrease_dict = greatest_decrease()
    financial_result = ( "Financial Analysis\n" +
                        "-------------------------\n" +
                        "Total Months: " + str(total_number_months()) + "\n" +
                        "Total: " + "$" + str(total_profits()) + "\n" +
                        "Average Change: " + "$" + str(average_change()) + "\n" +
                        "Greatest Increase in Profits: " + greatest_increase_dict.get("month") + " ($" + str(greatest_increase_dict.get("increase")) + ")\n" +
                        "Greatest Decrease in Profits: " + greatest_decrease_dict.get("month") + " ($" + str(greatest_decrease_dict.get("decrease")) + ")")
    
    print(financial_result)
    with open(curr_path + "\\analysis\\financial_results.txt", mode ='w') as file:
        file.write(financial_result)

# Call main function to display and write to file financial results
display_financial_results()

    