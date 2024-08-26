
class Hubspot:
    def __init__(self) -> None:
        True

    def process_json(self,json_object):
        try:
            required_fields = ["first_name","last_name","phone"]
            return_object = {}

            for field in required_fields:
                value = json_object.get(field)

                if not value:
                    continue
                new_key = f"hs_{field}"
                return_object[new_key] = value

            return return_object
        except Exception as e:
            raise e
    
