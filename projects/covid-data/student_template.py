import sys



def parse_nyt_data(file_path=''):
    """
    Parse the NYT covid database and return a list of tuples. Each tuple describes one entry in the source data set.
    Date: the day on which the record was taken in YYYY-MM-DD format
    County: the county name within the State
    State: the US state for the entry
    Cases: the cumulative number of COVID-19 cases reported in that locality
    Deaths: the cumulative number of COVID-19 death in the locality

    :param file_path: Path to data file
    :return: A List of tuples containing (date, county, state, cases, deaths) information
    """
    # data point list
    data=[]

    # open the NYT file path
    try:
        fin = open(file_path)
    except FileNotFoundError:
        print('File ', file_path, ' not found. Exiting!')
        sys.exit(-1)

    # get rid of the headers
    fin.readline()

    # while not done parsing file
    done = False

    # loop and read file
    while not done:
        line = fin.readline()

        if line == '':
            done = True
            continue

        # format is date,county,state,fips,cases,deaths
        (date,county, state, fips, cases, deaths) = line.rstrip().split(",")

        # clean up the data to remove empty entries
        if cases=='':
            cases=0
        if deaths=='':
            deaths=0

        # convert elements into ints
        try:
            entry = (date,county,state, int(cases), int(deaths))
        except ValueError:
            print('Invalid parse of ', entry)

        # place entries as tuple into list
        data.append(entry)


    return data

def first_question(data):
    """
    # Write code to address the following question: Use print() to display your responses.
    # When was the first positive COVID case in Rockingham County?
    # When was the first positive COVID case in Harrisonburg?
    :return:
    """

    # your code here

    # for rockingham:
    # iterate through the list and create a new list with only rockingham county
    rockingham_county_data = list()  # creating empty list to store rockingham county data
    for line in data:  # iterating through data list
        if line[1] == 'Rockingham' and line[2] == 'Virginia':  # finding the values in data list that are in rockingham, virginia
            rockingham_county_data.append(line)  # add the data lines in rockingham virginia into the list

    # iterate through rockingham county data list and find the first
    rockingham_date_first_covid_case = 0  # set an empty variable to hold the date of the first covid case in rockingham county
    for line in rockingham_county_data:  # iterating through rockingham data list
        if line[3] > 0:  # if the covid case number is greater than 0, that is a covid case
            rockingham_date_first_covid_case = line[0]  # set the date from the line with the covid case as the first date
        break  # stop the iteration to keep the first instance where the covid cases are more than 0 as the first date


    # for harrisonburg:
    # iterate through the list and create a new list with only harrisonburg county
    harrisonburg_county_data = list()    # creating empty list to store harrisonburg data
    for line in data:      # iterating through data list
        if line[1] == 'Harrisonburg city' and line[2] == 'Virginia':   # finding the values in data list that are in harrisonburg, virginia
            harrisonburg_county_data.append(line)   # add the data lines in harrisonburg, virginia into the list

    # iterate through harrisonburg county data list and find the first
    harrisonburg_date_first_covid_case = 0  # set an empty variable to hold the date of the first covid case in harrisonburg county
    for line in harrisonburg_county_data:   # iterate through harrisonburg data list
        if line[3] > 0:    # determine if covid case number is greater than 0
            harrisonburg_date_first_covid_case = line[0]   # set the date variable to the date of the line associated with the covid case greater than 0
        break  # break the iteration to keep first instance of a covid case more than 0 as the first date


    return rockingham_date_first_covid_case, harrisonburg_date_first_covid_case

def second_question(data):
    """
    # Write code to address the following question: Use print() to display your responses.
    # What day was the greatest number of new daily cases recorded in Harrisonburg?
    # What day was the greatest number of new daily cases recorded in Rockingham County?
    :return:
    """
    # for harrisonburg
    # create a new list with only harrisonburg data
    harrisonburg_county_data = list()  # creating empty list to store harrisonburg county data
    for line in data:  # iterating through data list
        if line[1] == 'Harrisonburg city' and line[2] == 'Virginia':  # finding the values in data list that are in harrisnoburg, virginia
            harrisonburg_county_data.append(line)  # add the data lines in harrisonburg city, virginia into the list

    # finding day with largest number of new cases
    harrisonburg_greatest_new_cases = 0  # set cases variable as empty
    cases1 = 0  # set cases variable as empty
    harrisonburg_greatest_new_cases_date = 0
    for line in harrisonburg_county_data:  # iterating through harrisonburg data list
        cases_of_line1 = line[3]  # set cases of line variable to cases in line
        delta_cases1 = cases_of_line1 - cases1  # finding the delta of cases between two lines(dates)
        cases1 = cases_of_line1  # rewriting cases to be the last line iterated through
        if delta_cases1 > harrisonburg_greatest_new_cases:  # comparing new cases between lines
            harrisonburg_greatest_new_cases = delta_cases1  # setting the greatest number of cases to value
            harrisonburg_greatest_new_cases_date = line[0]  # setting the date for greatest new cases

    # for rockingham
    # create a new list with only rockingham data
    rockingham_county_data = list()  # creating empty list to store rockingham county data
    for line in data:  # iterating through a data list
        if line[1] == 'Rockingham' and line[2] == 'Virginia':  # finding the values that are in rockingham county, virginia
            rockingham_county_data.append(line)  # add the data lines in rockingham, virginia into the list

    # finding day with largest number of new cases
    rockingham_greatest_new_cases = 0  # set cases variable as empty
    cases2 = 0  # set cases variable as empty
    rockingham_greatest_new_cases_date = 0
    for line in rockingham_county_data:  # iterating through rockingham county data
        cases_of_line2 = line[3]  # set cases of line variable to cases in line
        delta_cases2 = cases_of_line2 - cases2  # finding the delta of cases between two lines (dates)
        cases2 = cases_of_line2  # rewriting cases to be the last line iterated through
        if delta_cases2 > rockingham_greatest_new_cases:
            rockingham_greatest_new_cases = delta_cases2  # setting the greatest number of cases to the delta value
            rockingham_greatest_new_cases_date = line[0]  # setting the date for greatest new cases

    # your code here
    return harrisonburg_greatest_new_cases_date, rockingham_greatest_new_cases_date

def third_question(data):
    # Write code to address the following question:Use print() to display your responses.
    # What was the worst 7-day period in either the city and county for new COVID cases?
    # This is the 7-day period where the number of new cases was maximal.
    # for harrisonburg
    # create a new list with only harrisonburg data
    harrisonburg_county_data = list()  # creating empty list to store harrisonburg county data
    for line in data:  # iterating through data list
        if line[1] == 'Harrisonburg city' and line[2] == 'Virginia':  # finding the values in data list that are in harrisnoburg, virginia
            harrisonburg_county_data.append(line)  # add the data lines in harrisonburg city, virginia into the list

    # find the worst seven-day period
    largest_weekly_cases_h = 0  # set variable for largest weekly cases in harrisonburg as empty
    first_day_week_largest_cases_h = 0  # set variable for the first day of the seven day period with largest weekly cases
    seventh_day_week_largest_cases_h = 0  # set variable for the seventh day of the seven day period with the largest weekly cases
    for i in range(0, (len(harrisonburg_county_data) - 6)):  # iterate through harrisonburg data using a range to look at two lines of data simultaneously
        first_day_h = harrisonburg_county_data[i]  # setting first day line of data
        seventh_day_h = harrisonburg_county_data[i + 6]  # setting seventh day line of data
        first_day_cases_h = first_day_h[3]  # setting number of cases on first day to variable
        seventh_day_cases_h = seventh_day_h[3]  # setting number of cases on seventh day to variable
        new_weekly_cases_h = seventh_day_cases_h - first_day_cases_h  # finding number of new cases occuring during that sevent day window
        if new_weekly_cases_h > largest_weekly_cases_h:  # comparing number of new weekly cases to the largest number of weekly cases (initially 0)
            largest_weekly_cases_h = new_weekly_cases_h  # largest weekly cases variable is set to the largest of the new weekly cases values as the code iterates through the list
            first_day_week_largest_cases_h = first_day_h[0]  # first day of the seven day period with most new weekly cases is assigned
            seventh_day_week_largest_cases_h = seventh_day_h[0]  # last day of the seven day period with the most new weekly cases is assigned

    # for rockingham
    # create a new list with only rockingham data
    rockingham_county_data = list()  # creating empty list to store rockingham county data
    for line in data:  # iterating through a data list
        if line[1] == 'Rockingham' and line[2] == 'Virginia':  # finding the values that are in rockingham county, virginia
            rockingham_county_data.append(line)  # add the data lines in rockingham, virginia into the list

    # finding week (7 day period) of worst new cases in rockingham
    largest_weekly_cases_r = 0  # set variable for largest weekly cases in rockingham as empty
    first_day_week_largest_cases_r = 0  # set variable for the seventh day of the seven day period with the largest weekly cases
    seventh_day_week_largest_cases_r = 0  # set variable for the seventh day of the seven day period with the largest weekly cases
    for i in range(0, (len(rockingham_county_data) - 6)):  # iterate through rockingham data using a range to look at two lines of data simultaneously
        first_day_r = rockingham_county_data[i]  # setting first day line of data
        seventh_day_r = rockingham_county_data[i + 6]  # setting seventh day line of data
        first_day_cases_r = first_day_r[3]  # setting number of cases on first day to variable
        seventh_day_cases_r = seventh_day_r[3]  # setting number of cases on seventh day to variable
        new_weekly_cases_r = seventh_day_cases_r - first_day_cases_r  # finding number of new cases occuring during that sevent day window
        if new_weekly_cases_r > largest_weekly_cases_r:  # comparing number of new weekly cases to the largest number of weekly cases (initially 0)
            largest_weekly_cases_r = new_weekly_cases_r  # largest weekly cases variable is set to the largest of the new weekly cases values as the code iterates through the list
            first_day_week_largest_cases_r = first_day_r[0]  # first day of the seven day period with most new weekly cases is assigned
            seventh_day_week_largest_cases_r = seventh_day_r[0]  # last day of the seven day period with the most new weekly cases is assigned

    # for overall
    # setting emtpy variables
    city_worst_seven_day_period = 0  # setting empty variable for which city, rockingham or harrisonburg had worst seven-day-period
    first_day_seven_day_period = 0  # setting the variable for the first day of the seven day period
    last_day_seven_day_period = 0  # setting variable for last day of the seven day period
    number_of_worst_new_cases_weekly = 0  # setting the variable for the number of cases during the worst seven day period

    # comparing the rockingham and harrisonburg data
    if largest_weekly_cases_h > largest_weekly_cases_r:  # finding which number of worst cases is largest between rockingham and harrisonburg
        # assigning variables based on results from comparison if harrisonburg numbers are larger
        number_of_worst_new_cases_weekly = largest_weekly_cases_h
        city_worst_seven_day_period = 'Harrisonburg'
        first_day_seven_day_period = first_day_week_largest_cases_h
        last_day_seven_day_period = seventh_day_week_largest_cases_h
    else:
        # assigning variables based on results from comparison if rockingham numbers are larger
        number_of_worst_new_cases_weekly = largest_weekly_cases_r
        city_worst_seven_day_period = 'Rockingham'
        first_day_seven_day_period = first_day_week_largest_cases_r
        last_day_seven_day_period = seventh_day_week_largest_cases_r

    return number_of_worst_new_cases_weekly, city_worst_seven_day_period, first_day_seven_day_period, last_day_seven_day_period

if __name__ == "__main__":
    data = parse_nyt_data('us-counties.csv')

    # uncomment later
    #for (date, county, state, cases, deaths) in data:
        #print('On ', date, ' in ', county, ' ', state, ' there were ', cases, ' cases and ', deaths, ' deaths')


    # write code to address the following question: Use print() to display your responses.
    # When was the first positive COVID case in Rockingham County?
    # When was the first positive COVID case in Harrisonburg?
    first_question_answer = first_question(data)  # setting answer to variable
    print('The answer to the first question is:')
    print('The first positive COVID case in Rockingham County, Virginia was on' + ' ' + str(first_question_answer[0]) + '.')  # final print statement to display the answer for part a
    print('The first positive COVID case in Harrisonburg, Virginia was on' + ' ' + str(first_question_answer[1]) + '.') # final print statement to display the answer for part b

    # write code to address the following question: Use print() to display your responses.
    # What day was the greatest number of new daily cases recorded in Harrisonburg?
    # What day was the greatest number of new daily cases recorded in Rockingham County?
    second_question_answer = second_question(data) # setting answer to a variable
    print('The answer to the second question is:')
    print('The day with the greatest number of new daily cases recorded in Harrisonburg, VA was on' + ' ' + str(second_question_answer[0])) # final print statement to display answer for part a
    print('The day with the greatest number of new daily cases recorded in Rockingham, VA was on'+ ' ' + str(second_question_answer[1])) # final print statement to display the answer for part b


    # write code to address the following question:Use print() to display your responses.
    # What was the worst seven-day period in either the city and county for new COVID cases?
    # This is the 7-day period where the number of new cases was maximal.
    third_question_answer = third_question(data) # assigning the output of the function to a variable
    print('The answer to the third question is:')
    print(str(third_question_answer[1]) + ' ' + 'had' + ' ' + str(third_question_answer[0]) + ' new cases in the seven day period from ' + str(third_question_answer[2]) + ' to ' + str(third_question_answer[3]) + '.') # final print statement to answer question 3
