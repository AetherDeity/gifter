"""Auto-generated file, do not edit by hand. GM metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_GM = PhoneMetadata(id='GM', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='1\\d{1,2}', possible_number_pattern='\\d{2,3}', possible_length=(2, 3)),
    toll_free=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    premium_rate=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    emergency=PhoneNumberDesc(national_number_pattern='1?1[678]', possible_number_pattern='\\d{2,3}', example_number='117', possible_length=(2, 3)),
    short_code=PhoneNumberDesc(national_number_pattern='1?1[678]', possible_number_pattern='\\d{2,3}', example_number='117', possible_length=(2, 3)),
    standard_rate=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    carrier_specific=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    short_data=True)
