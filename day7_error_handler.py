# Day 7: Defensive Programming - Enterprise Exception Handling

try:
    # Attempting to scan a highly protected data directory stream
    with open("secret_vault.txt", "r") as file:
        for line in file:
            print(line.strip())

except FileNotFoundError:
    # Catching missing data paths or broken network directory streams
    print("System Notice: 'secret_vault.txt' is missing. Initiating fallback protocols.")

except PermissionError:
    # Catching security clearance locks or permission denials
    print("Security Alert: Access denied. Administrative privileges are required to open this file.")

except Exception as e:
    # Universal catch-all backup shield for unexpected system corruption
    print("An unexpected error occurred:", e)

finally:
    # Guaranteed clean-up routine to release system resources and memory frames
    print("System Log: Error evaluation routine complete. Cleaning memory frames.")

print("Program continues executing smoothly...")
