import re

def write_gcode_to_file(gcode_text, filename):
    try:
        with open(filename, 'w') as gcode_file:
            # Split the G-code text into lines, strip newline characters, and write to the file
            lines = [line.strip() for line in gcode_text.split('\n') if line.strip()]
            gcode_file.write('\n'.join(lines))
        print(f"G-code written to {filename}")
    except IOError as e:
        print(f"Error writing to {filename}: {e}")

def parse_gcode(gcode_text):
    # Initialize coordinates to zero
    x_coord = 0.0
    y_coord = 0.0
    z_coord = 0.0

    # Initialize empty lists to store coordinates
    x_coords = []
    y_coords = []
    z_coords = []

    # Split the G-code text into lines and process each line
    lines = gcode_text.split('\n')

    for line in lines:
        # Remove leading and trailing whitespace
        line = line.strip()

        # Ignore empty lines
        if not line:
            continue

        # Ignore comments (lines starting with a semicolon)
        if line.startswith(';'):
            continue

        # Extract X, Y, and Z values using regular expressions
        matches = re.findall(r'X(-?\d+\.\d+)|Y(-?\d+\.\d+)|Z(-?\d+\.\d+)', line)

        # Update coordinates based on matches
        for match in matches:
            if match[0]:
                x_coord = float(match[0])
            if match[1]:
                y_coord = float(match[1])
            if match[2]:
                z_coord = float(match[2])

        # Append the coordinates to their respective lists
        x_coords.append(x_coord)
        y_coords.append(y_coord)
        z_coords.append(z_coord)

    return x_coords, y_coords, z_coords


