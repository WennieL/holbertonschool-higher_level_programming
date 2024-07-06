#!/usr/bin/python3
import os


def generate_invitations(template, attendees):

    try:
        # check input type
        if not isinstance(template, str):
            raise ValueError("Template should be a string.")
        if not isinstance(attendees, list) or\
                not all(isinstance(attendee, dict) for attendee in attendees):
            raise ValueError("Attendees should be a list of dictionaries.")

        # Handle emput input
        if not template:
            raise ValueError("Template is empty, no output files generated.")
        if not attendees:
            raise ValueError("No data provided, no output files generated.")

        # Initialize index
        idx = 1

        # Process Each Attendee
        for attendee in attendees:
            output_content = template
            for key in ['name', 'event_title', 'event_date', 'event_location']:
                value = attendee.get(
                    key, 'N/A') if attendee.get(key) is not None else 'N/A'
                placeholder = f'{{{key}}}'
                output_content = output_content.replace(placeholder, value)

            # Generate Output File Name
            output_filename = f'output_{idx}.txt'

            # Check if file exists and rename if necessary
            # e.g. output_filename is 'output_1.txt'
            # base becomes 'output_1' / extension becomes '.txt'
            base, extension = os.path.splitext(output_filename)
            counter = 1
            while os.path.exists(output_filename):
                output_filename = f"{base}_{counter}{extension}"
                counter += 1

            # Write the processed template to the output file
            with open(output_filename, 'w') as output_file:
                output_file.write(output_content)
            print(f"Generated {output_filename}")

            # Increment index
            idx += 1

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
