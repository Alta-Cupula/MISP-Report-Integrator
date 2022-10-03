# Default execution
python main.py -f samples/iocs.pdf

# Add custom information
python main.py -f samples/hive.pdf --distribution 1 --info "DEMO Event" --analysis 2

# Add all custom information
python main.py -f samples/blackbasta.pdf --distribution 1 --info "DEMO Event" --tag color:white --analysis 0 --threat-level 3

# Add published event
python main.py -f samples/test2.pdf --distribution 1 --info "DEMO Event" --tag color:red --analysis 2 --threat-level 1 --published

# Add event with custom orgname
python main.py -f samples/test.pdf --orgc AltaCupula