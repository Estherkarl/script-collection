# Script: configuration_utility.py

# Function to read configuration settings from a file
def read_configuration(filename):
    config = {}
    with open(filename, 'r') as file:
        for line in file:
            key, value = line.strip().split('=')
            config[key.strip()] = value.strip()
    return config

# Function to write configuration settings to a file
def write_configuration(filename, config):
    with open(filename, 'w') as file:
        for key, value in config.items():
            file.write(f"{key} = {value}\n")

# Example usage
if __name__ == "__main__":
    # Read configuration from file
    config_file = 'config.txt'
    config_data = read_configuration(config_file)
    print("Current configuration:")
    for key, value in config_data.items():
        print(f"{key}: {value}")

    # Update configuration
    config_data['server'] = 'example.com'
    config_data['port'] = '8080'

    # Write updated configuration to file
    write_configuration(config_file, config_data)
    print("Updated configuration saved.")
