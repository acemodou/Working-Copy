import webbrowser
import sys 

#   address = sys.argv[1]
if len(sys.argv) > 1:
    url = " ".join(sys.argv[1:])
webbrowser.open_new(url)
