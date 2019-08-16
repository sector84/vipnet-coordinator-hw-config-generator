from .params import GeneralData
from .utils import convert_mask_to_str

general_params = GeneralData.get_instance()

__all__ = [
    'general_params',
    'convert_mask_to_str',
]
