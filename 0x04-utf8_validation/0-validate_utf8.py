def validUTF8(data):
    num_bytes_to_follow = 0

    for num in data:
        # Check if the most significant bit (MSB) is 1
        if num & 0x80:
            if num_bytes_to_follow == 0:
                # Determine the number of bytes to follow based on the first byte
                if num & 0xE0 == 0xC0:
                    num_bytes_to_follow = 1
                elif num & 0xF0 == 0xE0:
                    num_bytes_to_follow = 2
                elif num & 0xF8 == 0xF0:
                    num_bytes_to_follow = 3
                else:
                    # Invalid UTF-8 sequence
                    return False
            else:
                # Check if the byte is a continuation byte (starts with 10)
                if num & 0xC0 != 0x80:
                    # Invalid UTF-8 sequence
                    return False
                num_bytes_to_follow -= 1
        else:
            if num_bytes_to_follow > 0:
                # Invalid UTF-8 sequence
                return False

    # If there are still bytes to follow, it's an incomplete sequence
    return num_bytes_to_follow == 0
