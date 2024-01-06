def log_writer(mac_address: str, date: str) -> None:
    print("Arp spoofed\nGenerating log in log.txt for address", mac_address)
    with open("log.txt", "a", encoding="utf-8") as f:
        f.write(
            "Arp Spoofed!\n"
            + "The address is: "
            + mac_address
            + "\nDate: "
            + str(date)
            + "\n\n"
        )
        f.close()
