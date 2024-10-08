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
    print(rockingham_county_data)  # print as a check

    # iterate through rockingham county data list and find the first
    rockingham_date_first_covid_case = 0  # set an empty variable to hold the date of the first covid case in rockingham county
    for line in rockingham_county_data:  # iterating through rockingham data list
        if line[3] > 0:  # if the covid case number is greater than 0, that is a covid case
            rockingham_date_first_covid_case = line[0]  # set the date from the line with the covid case as the first date
        break  # stop the iteration to keep the first instance where the covid cases are more than 0 as the first date
    print(rockingham_date_first_covid_case)  # print as a check


    # for harrisonburg:
    # iterate through the list and create a new list with only harrisonburg county
    harrisonburg_county_data = list()    # creating empty list to store harrisonburg data
    for line in data:      # iterating through data list
        if line[1] == 'Harrisonburg city' and line[2] == 'Virginia':   # finding the values in data list that are in harrisonburg, virginia
            harrisonburg_county_data.append(line)   # add the data lines in harrisonburg, virginia into the list
    print(harrisonburg_county_data)   # print as a check

    # iterate through harrisonburg county data list and find the first
    harrisonburg_date_first_covid_case = 0  # set an empty variable to hold the date of the first covid case in harrisonburg county
    for line in harrisonburg_county_data:   # iterate through harrisonburg data list
        if line[3] > 0:    # determine if covid case number is greater than 0
            harrisonburg_date_first_covid_case = line[0]   # set the date variable to the date of the line associated with the covid case greater than 0
        break  # break the iteration to keep first instance of a covid case more than 0 as the first date
    print(harrisonburg_date_first_covid_case)  # print as a check


    return rockingham_date_first_covid_case, harrisonburg_date_first_covid_case

def second_question(data):
    """
    # Write code to address the following question: Use print() to display your responses.
    # What day was the greatest number of new daily cases recorded in Harrisonburg?
    # What day was the greatest number of new daily cases recorded in Rockingham County?
    :return:
    """

    # your code here
    return

def third_question(data):
    # Write code to address the following question:Use print() to display your responses.
    # What was the worst 7-day period in either the city and county for new COVID cases?
    # This is the 7-day period where the number of new cases was maximal.

    return

if __name__ == "__main__":
    data = parse_nyt_data('us-counties.csv')

    # uncomment later
    #for (date, county, state, cases, deaths) in data:
        #print('On ', date, ' in ', county, ' ', state, ' there were ', cases, ' cases and ', deaths, ' deaths')


    # write code to address the following question: Use print() to display your responses.
    # When was the first positive COVID case in Rockingham County?
    # When was the first positive COVID case in Harrisonburg?
    first_question_answer = first_question(data)  # setting answer to variable
    print(first_question_answer) # print to check format of answer
    print('The first positive COVID case in Rockingham County, Virginia was on' + ' ' + str(first_question_answer[0]) + '.')  # final print statement to display the answer for part a
    print('The first positive COVID case in Harrisonburg, Virginia was on' + ' ' + str(first_question_answer[1]) + '.') # final print statement to display the answer for part b

    # write code to address the following question: Use print() to display your responses.
    # What day was the greatest number of new daily cases recorded in Harrisonburg?
    # What day was the greatest number of new daily cases recorded in Rockingham County?
    second_question_answer = second_question(data)

    # for harrisonburg
    # create a new list with only harrisonburg data
    for line in data: #iterating through data list
        harrisonburg_county_data = list()  # creating empty list to store rockingham county data
        for line in data:  # iterating through data list
            if line[1] == 'Harrisonburg city' and line[2] == 'Virginia':  # finding the values in data list that are in rockingham, virginia
                harrisonburg_county_data.append(line)  # add the data lines in rockingham virginia into the list

    # finding day with largest number of cases
    harrisonburg_greatest_number_cases = 0
    harrisonburg_date_greatest_number_cases = 0
    for line in harrisonburg_county_data: # iterating through harrisonburg data
        if line[3] > harrisonburg_greatest_number_cases:
            harrisonburg_greatest_number_cases = line[3]
            harrisonburg_date_greatest_number_cases = line[0]

    # for rockingham
    # create a new list with only rockingham data
    for line in data:



    # write code to address the following question:Use print() to display your responses.
    # What was the worst seven day period in either the city and county for new COVID cases?
    # This is the 7-day period where the number of new cases was maximal.
    third_question(data)


