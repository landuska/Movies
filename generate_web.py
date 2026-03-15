def load_html(file_path):
    """ Load a HTML file """

    try:
        with open(file_path, "r") as file:
            return file.read()

    except FileNotFoundError:
        print("HTML file not found")
        return ""

    except PermissionError:
        print("Permission error")
        return ""

    except OSError as e:
        print(f"File error: {e}")
        return ""


def save_html(file_path, content):
    """ Save a HTML file """

    try:
        with open(file_path, "w") as file:
            file.write(content)

    except PermissionError:
        print("Cannot write file (permission denied)")

    except OSError as e:
        print(f"File error: {e}")


def serialize_movie(title, year, image):
    """ Serialize a movie """

    output_string = ''
    output_string += '<li>'
    output_string += '<div class="movie">\n'
    output_string += f'<img class="movie-poster" src="{image}">\n'
    output_string += f'<div class="movie-title">{title}</div>\n'
    output_string += f'<div class="movie-year">{year}</div>\n'
    output_string += '</div>\n'
    output_string += '</li>\n'
    return output_string
