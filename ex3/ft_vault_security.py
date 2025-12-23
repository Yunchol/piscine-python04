def main():
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")
    print("Initiating secure vault access...")

    # --- SECURE EXTRACTION (read) ---
    print("Vault connection established with failsafe protocols")
    print("SECURE EXTRACTION:")

    try:
        with open("classified_data.txt", "r") as file:
            data = file.read()
            print(data.strip())
    except FileNotFoundError:
        print("{[}CLASSIFIED{]} No classified data found")

    # --- SECURE PRESERVATION (write) ---
    print("SECURE PRESERVATION:")

    with open("secure_archive.txt", "w") as file:
        file.write("{[}CLASSIFIED{]} New security protocols archived\n")
        print("{[}CLASSIFIED{]} New security protocols archived")

    print("Vault automatically sealed upon completion")
    print("All vault operations completed with maximum security.")


if __name__ == "__main__":
    main()
