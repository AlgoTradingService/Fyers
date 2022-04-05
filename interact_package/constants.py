success_response_codes = (200,)
error_response_codes = (400, 401, 403, 429, 500)
response_code_values = {
    200: "Request was successful",
    400: "Bad request. The request is invalid or certain other errors",
    401: "Authorization error. User could not be authenticated",
    403: "Permission error. User does not have the necessary permissions",
    429: "Rate limit exceeded. Users have been blocked for exceeding the rate limit.",
    500: "Internal server error."
}

error_access_response = (-8,)