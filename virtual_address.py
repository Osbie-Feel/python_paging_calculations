hex_address = "5A7DC9EB"

exp_page_size = 11

# convert hex to binary and pad with zeros to 32 bit string
bin_address = "{0:032b}".format(int(hex_address, 16))

bin_page_number = bin_address[:len(bin_address)-exp_page_size]

bin_offset = bin_address[len(bin_address)-exp_page_size:]

hex_page_number = '%0*X' % ((len(bin_page_number) + 3) // 4, int(bin_page_number, 2))

hex_offset = '%0*X' % ((len(bin_offset) + 3) // 4, int(bin_offset, 2))

# Print the results
print("Page number in hex:  ", hex_page_number)

print("Offset in hex:       ", hex_offset)

# print("Address in binary:       ", bin_address)
# print("Page number in binary:    ", bin_page_number)
# print("Offset in binary:        ", bin_offset)




