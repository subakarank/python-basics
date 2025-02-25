import pprint


def timeComplexity(value, desc):
    result = f'\n 🕒 Time Complexity: Approximately {value}'

    if (desc):
        result += f'\n    Description: {desc}'
    print(result)


def spaceComplexity(value, desc):
    result = f' 💾 Space Complexity: Approximately {value}'

    if (desc):
        result += f'\n    Description: {desc}'
    print(result)


def print_h1(text):
    print(f"\n{'=' * 40}\n{text}\n{'=' * 40}")


def print_h2(text):
    print(f"\n{'-' * 35}\n{text}\n{'-' * 35}")


def print_h3(text):
    print(f"\n{text}\n{'-' * 30}")


def print_h4(text):
    print(f"\n{text}\n{'-' * 25}")


def print_h5(text):
    print(f"\n{text}\n{'-' * 20}")


def print_h6(text):
    print(f"\n{text}\n{'-' * 15}")


def print_ordered_list(items):
    for i, item in enumerate(items, start=1):
        print(f"{i}. {item}")


def print_bullet_list(items, bullet_char='*'):
    for item in items:
        print(f"{bullet_char} {item}")


def print_blockquote(items, indent_char='> ', emoji='💬', new_line = False):
    if (new_line):
        print('\n')
    for item in items:
        print(f"{emoji} {indent_char}{item}")


def pretty_json(input):
    pprint.pprint(input, width=50, indent=2)


def print_tabular_list(data, col_widths = [15, 45]):
    """
    Print data in a tabular format with horizontal lines, differentiating the header.

    :param data: List of tuples, where each tuple represents a row.
    :param col_widths: List of integers representing the width of each column.
    """
    def print_divider():
        # Create and print a divider line with '+'
        line = "+" + "+".join("-" * width for width in col_widths) + "+"
        print(line)

    def print_header_divider():
        # Create and print a simple divider line without '+' for the header
        line = "-" * (sum(col_widths) + len(col_widths) - 1)
        print(line)

    # Print the header row
    print_divider()
    header = data[0]
    formatted_header = "|".join(
        f"{item:<{col_widths[i]}}" for i, item in enumerate(header))
    print("|" + formatted_header + "|")
    print_header_divider()

    # Print the rest of the rows
    for row in data[1:]:
        formatted_row = "|".join(
            f"{item:<{col_widths[i]}}" for i, item in enumerate(row))
        print("|" + formatted_row + "|")
        print_header_divider()
