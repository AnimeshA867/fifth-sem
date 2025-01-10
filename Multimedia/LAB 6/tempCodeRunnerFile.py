def justify_text(text, width):
    words = text.split()
    lines = []
    current_line = []
    current_length = 0

    for word in words:
        if current_length + len(word) + len(current_line) <= width:
            current_line.append(word)
            current_length += len(word)
        else:
            for i in range(width - current_length):
                current_line[i % (len(current_line) - 1 or 1)] += ' '
            lines.append(''.join(current_line))
            current_line = [word]
            current_length = len(word)

    lines.append(' '.join(current_line).ljust(width))
    return '\n'.join(lines)

if __name__ == "__main__":
    user_text = input("Enter the text to be justified: ")
    column_width = int(input("Enter the column width: "))
    justified_text = justify_text(user_text, column_width)
    print("\nJustified Text:\n")
    print(justified_text)
