import sys
from db_table import db_table


# store the column name and value
column = sys.argv[1]

# store the value name. Note that the for loop checks if the value is a sentence/longer than one word.
value = ""
for k in range(2, len(sys.argv)):
    value = value + " "+sys.argv[k]
value = value.strip()

# open/create the database with the desired schema and table name.
schema = {"id": "integer", "date": "text", "time_start": "text", "time_end": "text",
          "session": "text", "session_title": "text", "location": "text", "description": "text", "speakers": "text"}

sq = db_table("Agenda", schema)

#
# First get the rows that have the desired value
# then use the id's to get the sub session of the rows
# Finally displays the subssions and the sessions
#


def main():

    # an array to contain the final results
    result = []
    # get the parent id based on column and value
    rows = sq.select(None, {column: value})

    # get the id of the parent sessions and call sq select to get sub sessions also
    for row in rows:
        result.append(sq.select(None, {"id": row["id"]}))
    # display the result.
    for res in result:
        print(res, "\n")


if __name__ == "__main__":
    main()
