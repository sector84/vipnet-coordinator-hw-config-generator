class GeneralData:
    instance = None

    def __init__(self):
        self.input_file_path = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = GeneralData()
        return cls.instance

    def load_params(self, args):
        self.input_file_path = args['file']
