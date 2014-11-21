from uiuc import UIUCSelfService
import getpass


def notify(query):
    print "Attn: " + query['crn'] + " is now available!"


def main():

    username = raw_input("Username: ")
    password = getpass.getpass()

    while getpass.getpass("Reenter password: ") != password:
        print "Password does not match. Try again."
        password = getpass.getpass()

    term = raw_input("Term: ")
    queries = list()

    print "Type in your major, course and crn to monitor the class."
    print "Type 'X' to indicate that your are done at any point."

    while 1:
        major = raw_input("Major (example ECE): ")

        if major == "X":
            break

        course = raw_input("Course (example 391): ")

        if course == "X":
            break

        crn = raw_input("CRN (example 54321: ")

        if crn == "X":
            break

        queries.append({"major": major, "course": course, "crn": crn})

    print "Starting..."

    ss = UIUCSelfService()
    ss.term = term
    ss.login(username=username, password=password)

    completed = list()

    while len(completed) != len(queries):
        for query in queries:
            classes = \
                ss.get_classes(major=query['major'], course=query['course'])

            print query['crn'] + ": " + str(classes[query['crn']])

            if classes[query['crn']]:
                notify(query)
                completed.append(query)

    print "Done!"


if __name__ == "__main__":
    main()