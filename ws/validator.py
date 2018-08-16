class Validator:

    # Validates json input
    def validate_json(self, request):
        if ("name" in request and "price" in request and "isbn" in request):
            return True
        else:
            return False
