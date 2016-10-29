"""Auto-generated file, do not edit by hand. BR metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_BR = PhoneMetadata(id='BR', country_code=55, international_prefix='00(?:1[245]|2[1-35]|31|4[13]|[56]5|99)',
    general_desc=PhoneNumberDesc(national_number_pattern='[1-46-9]\\d{7,10}|5(?:[0-4]\\d{7,9}|5(?:[2-8]\\d{7}|9\\d{7,8}))', possible_number_pattern='\\d{8,11}', possible_length=(8, 9, 10, 11), possible_length_local_only=(8,)),
    fixed_line=PhoneNumberDesc(national_number_pattern='(?:[14689][1-9]|2[12478]|3[1-578]|5[1-5]|7[13-579])[2-5]\\d{7}', possible_number_pattern='\\d{8,11}', example_number='1123456789', possible_length=(10,), possible_length_local_only=(8,)),
    mobile=PhoneNumberDesc(national_number_pattern='1[1-9](?:7|9\\d)\\d{7}|(?:2[12478]|3[1-578]|[4689][1-9]|5[1-5]|7[13-579])(?:[6-8]|9\\d?)\\d{7}', possible_number_pattern='\\d{8,11}', example_number='11961234567', possible_length=(10, 11), possible_length_local_only=(8,)),
    toll_free=PhoneNumberDesc(national_number_pattern='800\\d{6,7}', possible_number_pattern='\\d{8,11}', example_number='800123456', possible_length=(9, 10)),
    premium_rate=PhoneNumberDesc(national_number_pattern='(?:300|[59]00\\d?)\\d{6}', possible_number_pattern='\\d{8,11}', example_number='300123456', possible_length=(9, 10)),
    shared_cost=PhoneNumberDesc(national_number_pattern='(?:300\\d(?:\\d{2})?|40(?:0\\d|20))\\d{4}', possible_number_pattern='\\d{8,10}', example_number='40041234', possible_length=(8, 10)),
    personal_number=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voip=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    pager=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    uan=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voicemail=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='(?:300\\d|40(?:0\\d|20))\\d{4}', possible_number_pattern='\\d{8}', example_number='40041234', possible_length=(8,)),
    national_prefix='0',
    national_prefix_for_parsing='0(?:(1[245]|2[1-35]|31|4[13]|[56]5|99)(\\d{10,11}))?',
    national_prefix_transform_rule='\\2',
    number_format=[NumberFormat(pattern='(\\d{4})(\\d{4})', format='\\1-\\2', leading_digits_pattern=['[2-9](?:[1-9]|0[1-9])'], national_prefix_formatting_rule='\\1'),
        NumberFormat(pattern='(\\d{5})(\\d{4})', format='\\1-\\2', leading_digits_pattern=['9(?:[1-9]|0[1-9])'], national_prefix_formatting_rule='\\1'),
        NumberFormat(pattern='(\\d{3,5})', format='\\1', leading_digits_pattern=['1[125689]'], national_prefix_formatting_rule='\\1'),
        NumberFormat(pattern='(\\d{2})(\\d{5})(\\d{4})', format='\\1 \\2-\\3', leading_digits_pattern=['(?:[14689][1-9]|2[12478]|3[1-578]|5[1-5]|7[13-579])9'], national_prefix_formatting_rule='(\\1)', domestic_carrier_code_formatting_rule='0 $CC (\\1)'),
        NumberFormat(pattern='(\\d{2})(\\d{4})(\\d{4})', format='\\1 \\2-\\3', leading_digits_pattern=['[1-9][1-9]'], national_prefix_formatting_rule='(\\1)', domestic_carrier_code_formatting_rule='0 $CC (\\1)'),
        NumberFormat(pattern='(\\d{4})(\\d{4})', format='\\1-\\2', leading_digits_pattern=['(?:300|40(?:0|20))']),
        NumberFormat(pattern='([3589]00)(\\d{2,3})(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['[3589]00'], national_prefix_formatting_rule='0\\1')],
    intl_number_format=[NumberFormat(pattern='(\\d{2})(\\d{5})(\\d{4})', format='\\1 \\2-\\3', leading_digits_pattern=['(?:[14689][1-9]|2[12478]|3[1-578]|5[1-5]|7[13-579])9']),
        NumberFormat(pattern='(\\d{2})(\\d{4})(\\d{4})', format='\\1 \\2-\\3', leading_digits_pattern=['[1-9][1-9]']),
        NumberFormat(pattern='(\\d{4})(\\d{4})', format='\\1-\\2', leading_digits_pattern=['(?:300|40(?:0|20))']),
        NumberFormat(pattern='([3589]00)(\\d{2,3})(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['[3589]00'])],
    mobile_number_portable_region=True)
