'''match-case Statement '''
# --- USE: match-case Statement ---
HTTP_STATUS_CODE = 403 # Try 200, 500, 999
STATUS_MEANING = ""

match HTTP_STATUS_CODE:
    case 200|201:
        STATUS_MEANING = "OK - Request successful."
    case 301:
        STATUS_MEANING = "Moved Permanently - Resource has a new URL."
    case 403:
        STATUS_MEANING = "Forbidden - You don't have permission."
    case 404:
        STATUS_MEANING = "Not Found - The resource doesn't exist."
    case 500:
        STATUS_MEANING = "Internal Server Error - Something went wrong on our end."
    # case 301:
    #     status_meaning = "Moved Permanently - Resource has a new URL."
    case _: # Default case
        STATUS_MEANING = "Unknown or unhandled status code."


print(f"Status {HTTP_STATUS_CODE}: {STATUS_MEANING}")


# match-case (3b): Add a new case for http_status_code 301 that sets status_meaning
# to "Moved Permanently - Resource has a new URL."

# match-case (3b): How could you make case 200 and case 201
#   (Created) both lead to a similar "Success" message,
# perhaps by setting a common variable or using |? (e.g., case 200 | 201: status_type = "Success")
