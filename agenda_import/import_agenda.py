# import pandas as pd
import sys
from db_table import db_table
import xlrd
import uuid


# store the file name in a variable
filename = sys.argv[1]

# create the schema
schema = {"id": "integer", "date": "text", "time_start": "text", "time_end": "text",
          "session": "text", "session_title": "text", "location": "text", "description": "text", "speakers": "text"}

sq = db_table("Agenda", schema)

id = 0

#
# Format the the item by replacing ' with ''
# If it's a sub session, then store it with the same id as the parent session.
# otherwise increment the id by 1.
# Create a dictionary in the same format as the one needed for schema
#


def formatItem(item):
    global id
    for i in range(len(item)):
        if "'" in item[i]:
            item[i] = item[i].replace("'", "''")

    # if it's a session then increment the id by 1
    if item[3] == "Session":
        id += 1

    # create an item dictionary in the same format as required by the insert function
    itemDict = {"id": id, "date": item[0], "time_start": item[1], "time_end": item[2], "session": item[3],
                "session_title": item[4], "location": item[5], "description": item[6], "speakers": item[7]}

    return itemDict

#
# Open the excel sheet
# call format item on each row
# insert the formatted item into the database
#


def main():
    # open the excel book and sheet
    book = xlrd.open_workbook(filename)
    sheet = book.sheet_by_name('Agenda')

    # The loop starts with 14 since the excel files says that the data starts at 14
    for i in range(14, sheet.nrows):
        sq.insert(formatItem(sheet.row_values(i)))


if __name__ == "__main__":
    main()
