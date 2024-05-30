def parse_address(address):
    split_address = address.split(', ')
    address_dict = {
        'address_line_1': split_address[0],
        'address_line_2': '',
        'city': split_address[-3],
        'state': split_address[-2],
        'zipcode': split_address[-1]
    }
    
    # Parse address line 2 if provided
    # if len(split_address) == 5:
    #     address_dict['address_line_2'] = split_address[1]
    
    return address_dict