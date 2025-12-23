def main():
    filename = "ancient_fragment.txt"

    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    print(f"Accessing Storage Vault: {filename}")

    try:
        file = open(filename, "r")
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")
        return

    print("Connection established...")
    print("RECOVERED DATA:")

    data = file.read()
    print(data.strip())

    file.close()
    print("Data recovery complete. Storage unit disconnected.")


if __name__ == "__main__":
    main()
