import re

def postCodeVal(post_code):

    pattern = "^[A-Z]{1,2}[0-9][A-Z0-9]? ?[0-9][A-Z]{2}$"
    # special_pattern = "^(([A-Z]{1,2}[0-9][A-Z0-9]?|ASCN|STHL|TDCU|BBND|[BFS]IQQ|PCRN|TKCA) ?[0-9][A-Z]{2}|BFPO ?[0-9]{1,4}|(KY[0-9]|MSR|VG|AI)[ -]?[0-9]{4}|[A-Z]{2} ?[0-9]{2}|GE ?CX|GIR ?0A{2}|SAN ?TA1)$"
    valid = re.match(pattern, post_code)
    if valid:
        post_code = re.sub(r'\s+', '', post_code)
        n = len(post_code) - 3
        outward_code = post_code[0:n]  # get outward code string for formatting
        print(outward_code + " outward_code")
        inward_code = post_code[n:]  # get inward code string for formatting
        print(inward_code + " inward_code")
        string_format = len(inward_code) + 1  # add 1 extra space for formatting eg. SW1W 0NY
        post_code_formatted = outward_code + inward_code.rjust(string_format) # join strings together with spacing
        print("Postal Code Entry Successful " + post_code_formatted)
        valid = "Postal Code Entry Successful " + post_code_formatted
        return valid
    else:
        print(post_code + " Is not a valid UK Postal Code")
        invalid = post_code + " Is not a valid UK Postal Code"
        return invalid
    
