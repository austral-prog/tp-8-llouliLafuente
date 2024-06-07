"""Functions to help Azara and Rui locate pirate treasure."""


def get_coordinate(record):
    """Return coordinate value from a tuple containing the treasure name, and treasure coordinate.

    :param record: tuple - with a (treasure, coordinate) pair.
    :return: str - the extracted map coordinate.
    """

    return record[1]
record = ("Scrimshawed Whale Tooth", "2A")
coordinate = get_coordinate(record)
print(coordinate) 

def convert_coordinate(coordinate):
    """Split the given coordinate into tuple containing its individual components.

    :param coordinate: str - a string map coordinate
    :return: tuple - the string coordinate split into its individual components.
    """

    return (coordinate[0], coordinate[1])
coordinate = "2A"
converted_coordinate = convert_coordinate(coordinate)
print(converted_coordinate)

def create_record(azara_record, rui_record):
    """Combine the two record types (if possible) and create a combined record group.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, coordinate, quadrant) trio.
    :return: tuple or str - the combined record (if compatible), or the string "not a match" (if incompatible).
    """

    azara_treasure, azara_coordinate = azara_record
    rui_location, rui_coordinate, rui_quadrant = rui_record

    if azara_coordinate == str(rui_coordinate[0]) + str(rui_coordinate[1]):
        return (azara_treasure, azara_coordinate, rui_location, rui_coordinate, rui_quadrant)
    else:
        return "not a match"
    
azara_record = ("Brass Spyglass", "4B")
rui_record = ("Abandoned Lighthouse", ("4", "B"), "Blue")
combined_record = create_record(azara_record, rui_record)
print(combined_record)  
