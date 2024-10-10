# CoinCount v1.5
*By Peter Cakebread 2023*

CoinCount is a simple Python-based application designed to help volunteers track and count coins, calculate accuracy, and store data persistently for further reference.

## Features
- **Coin Counting**: Automatically calculates the correct number of coins in a bag based on weight.
- **Volunteer Tracking**: Stores the data of volunteers, including how many bags they counted and their accuracy rate.
- **Stats Overview**: View individual or collective statistics of all volunteers, including total amount counted and accuracy.
- **Data Persistence**: Saves volunteer data to a file (`coincount.txt`) and retrieves it when the program is restarted.
- **Formatting Option**: Allows for resetting all stored data.

## How It Works

1. **coin_index(cointype)**: This function returns the index of a specific coin type (e.g. £2, 50p) from the list of possible coins.
2. **count()**: The core function where volunteers input the type of coins and the bag’s weight. The system then checks if the weight is correct for the given number of coins and records the result.
3. **stats()**: Displays either individual volunteer statistics or stats for all volunteers, including accuracy and total money counted.
4. **save()**: Writes the current state of the data to `coincount.txt` to ensure persistence.
5. **format_dat()**: This function allows for wiping all data from the system.

## File Structure
- **coincount.txt**: A file where all user data is stored in JSON format. The file is read and updated as volunteers count coins and their stats are tracked.

## How to Use

1. **Run the Program**: 
   - You can start the program by running the Python file.
   
2. **Select an Option**:
   - You will be prompted to choose from:
     - `count`: Begin counting coins.
     - `stats`: View volunteer statistics.
     - `format`: Wipe all stored data.
     - `exit`: Save and exit the program.

### Example Workflow:

- **Counting Coins**:
   - The volunteer inputs their name, the type of coin, and the bag’s weight.
   - If the weight matches the expected weight for the coin type, the bag is counted as correct. If not, the program will tell the volunteer how many coins to add or remove.
   
- **Viewing Stats**:
   - Select the `stats` option to see individual or overall stats, including the total counted amount and accuracy percentage for each volunteer.

- **Formatting Data**:
   - If you wish to reset all data, choose the `format` option. You will be asked to confirm before all volunteer data is erased.

## Dependencies

This program requires:
- **Python 3.x**
- **json**: The built-in JSON library is used for saving and loading volunteer data.

## Installation and Setup

1. Ensure Python 3.x is installed on your system.
2. Clone or download this repository.
3. Place `coincount.txt` in the same directory as the Python script.

## License
This project is licensed under the MIT License.

