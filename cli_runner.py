import offeringsParser

response = ''
done = False

while(done == False):
    response = input("Please input (DEPT ABBR) (COURSE NUM):\n")
    if response == 'done':
        done = True
    else:
        response = response.split(" ")
        offerings = offeringsParser.get_courses_by_dept_num('Spring 2024', response[0], response[1])
        for offering in offerings:
            print(offering)

    