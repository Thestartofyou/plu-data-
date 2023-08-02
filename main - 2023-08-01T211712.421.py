def detect_agricultural_practice(plu_number):
    plu_data = {
        '4011': 'Conventional',
        '94011': 'Organic',
        '84011': 'GMO',
        '3000': 'Conventional',
        '93000': 'Organic',
        # Add more PLU data here as needed
    }

    if plu_number in plu_data:
        return plu_data[plu_number]
    else:
        return 'Unknown'

if __name__ == "__main__":
    # Assuming the user enters the PLU number
    plu_number = input("Enter the PLU number of the fruit or vegetable: ")
    agricultural_practice = detect_agricultural_practice(plu_number)

    if agricultural_practice == 'Unknown':
        print("Agricultural practice for this PLU number is not available.")
    else:
        print(f"PLU {plu_number} corresponds to {agricultural_practice} produce.")
