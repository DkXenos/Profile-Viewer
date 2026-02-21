import os
import webbrowser
from pick import pick

def main():
    items = {
        "Youtube": "https://www.youtube.com",
        "Github": "https://www.github.com",
        "Linkedin": "https://www.linkedin.com",
        "Gemini": "https://gemini.google.com",
        "Safari": "https://www.apple.com/safari/",
        "Google": "https://www.google.com",
        "GDocs": "https://docs.google.com",
        "Visual Studio Code": "Visual Studio Code",
        "Xcode": "Xcode",
        "Unity Hub": "Unity Hub"
    }

    options = list(items.keys())
    title = 'Select what you want to open:'
    option, index = pick(options, title, indicator='>', default_index=0)

    selection = items[option]

    if selection.startswith("http"):
        print(f"Opening browser to {option}...")
        webbrowser.open(selection)
    else:
        print(f"Launching {selection}...")
        os.system(f'open -a "{selection}"')

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting...")